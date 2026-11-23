import json
import os
import threading
import time
import tkinter as tk
from tkinter import messagebox, ttk


class ExpenseTrackerApp:
    def __init__(self, root: tk.Tk):
        # 1. ГЛАВНОЕ ОКНО
        self.root = root
        self.root.title("Трекер расходов (MVC + Async)")
        self.root.geometry("540x480")
        self.root.resizable(False, False)

        # Путь к отдельному файлу базы данных
        self.db_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "database.json"
        )
        self.expenses = self.load_data()

        self.setup_ui()
        self.update_table()

    def load_data(self) -> list:
        if not os.path.exists(self.db_path):
            return []
        with open(self.db_path, "r", encoding="utf-8") as file:
            return json.load(file).get("expenses", [])

    def setup_ui(self):
        # 10. КОМПОНОВКА (жесткая табличная сетка grid внутри Frame)
        main_frame = tk.Frame(self.root, padx=16, pady=16)
        main_frame.pack(fill="both", expand=True)
        main_frame.columnconfigure(1, weight=1)

        # 2. ТЕКСТОВЫЕ ЭЛЕМЕНТЫ (Label)
        title_lbl = tk.Label(
            main_frame, text="Учет личных расходов", font=("Arial", 14, "bold")
        )
        title_lbl.grid(row=0, column=0, columnspan=2, pady=(0, 12))

        tk.Label(main_frame, text="Покупка / услуга:").grid(
            row=1, column=0, sticky="w", pady=5
        )
        # 3. ПОЛЕ ВВОДА (Entry) — название
        self.item_entry = tk.Entry(main_frame)
        self.item_entry.grid(row=1, column=1, sticky="ew", pady=5)

        tk.Label(main_frame, text="Сумма (руб.):").grid(
            row=2, column=0, sticky="w", pady=5
        )
        # 3. ПОЛЕ ВВОДА (Entry) — числовое значение
        self.amount_entry = tk.Entry(main_frame)
        self.amount_entry.grid(row=2, column=1, sticky="ew", pady=5)

        # 5. ВЫБОР ПАРАМЕТРОВ (Combobox + Radiobutton)
        tk.Label(main_frame, text="Категория:").grid(
            row=3, column=0, sticky="w", pady=5
        )
        self.category_combo = ttk.Combobox(
            main_frame,
            values=["Еда", "Транспорт", "Учеба", "Развлечения", "Другое"],
            state="readonly",
        )
        self.category_combo.current(0)
        self.category_combo.grid(row=3, column=1, sticky="ew", pady=5)

        tk.Label(main_frame, text="Способ оплаты:").grid(
            row=4, column=0, sticky="w", pady=5
        )
        pay_frame = tk.Frame(main_frame)
        pay_frame.grid(row=4, column=1, sticky="w", pady=5)

        self.payment_var = tk.StringVar(value="Карта")
        tk.Radiobutton(
            pay_frame, text="Карта", variable=self.payment_var, value="Карта"
        ).pack(side="left", padx=(0, 12))
        tk.Radiobutton(
            pay_frame,
            text="Наличные",
            variable=self.payment_var,
            value="Наличные",
        ).pack(side="left")

        # 4. КНОПКА ОТПРАВКИ ДАННЫХ + 7. ОБРАБОТКА СОБЫТИЙ
        self.add_btn = tk.Button(
            main_frame,
            text="Записать расход",
            bg="#2e7d32",
            fg="white",
            font=("Arial", 10, "bold"),
            command=self.handle_submit,
        )
        self.add_btn.grid(row=5, column=0, columnspan=2, sticky="ew", pady=10)

        # Событие нажатия клавиши Enter
        self.root.bind("<Return>", lambda event: self.handle_submit())

        # Строка статуса и итоговая сумма
        info_frame = tk.Frame(main_frame)
        info_frame.grid(row=6, column=0, columnspan=2, sticky="ew", pady=(0, 6))

        self.status_lbl = tk.Label(info_frame, text="Статус: готово", fg="#555")
        self.status_lbl.pack(side="left")

        self.total_lbl = tk.Label(
            info_frame, text="Итого: 0.00 руб.", font=("Arial", 10, "bold")
        )
        self.total_lbl.pack(side="right")

        # 6. РЕЗУЛЬТАТЫ (таблица Treeview из модулей ttk)
        columns = ("item", "category", "payment", "amount")
        self.tree = ttk.Treeview(
            main_frame, columns=columns, show="headings", height=8
        )
        self.tree.heading("item", text="Название")
        self.tree.heading("category", text="Категория")
        self.tree.heading("payment", text="Оплата")
        self.tree.heading("amount", text="Сумма (руб.)")

        self.tree.column("item", width=180)
        self.tree.column("category", width=110)
        self.tree.column("payment", width=90)
        self.tree.column("amount", width=100, anchor="e")

        self.tree.grid(row=7, column=0, columnspan=2, sticky="nsew")
        main_frame.rowconfigure(7, weight=1)

    def handle_submit(self):
        # 8. ПРОВЕРКА ДАННЫХ (Валидация текста и числа)
        item_name = self.item_entry.get().strip()
        raw_amount = self.amount_entry.get().strip().replace(",", ".")

        if not item_name:
            # 9. ДИАЛОГОВОЕ ОКНО (ошибка пустого поля)
            messagebox.showerror("Ошибка ввода", "Введите название покупки!")
            return

        try:
            amount = float(raw_amount)
            if amount <= 0:
                raise ValueError
        except ValueError:
            # 9. ДИАЛОГОВОЕ ОКНО (ошибка формата числа)
            messagebox.showerror(
                "Ошибка суммы", "Введите корректное число больше нуля!"
            )
            return

        record = {
            "item": item_name,
            "amount": round(amount, 2),
            "category": self.category_combo.get(),
            "payment": self.payment_var.get(),
        }

        # Асинхронная запись в фоне, чтобы окно не зависало 
        self.add_btn.config(state="disabled")
        self.status_lbl.config(text="Статус: запись в базу...")

        worker = threading.Thread(
            target=self.save_record_async, args=(record,), daemon=True
        )
        worker.start()

    def save_record_async(self, record: dict):
        # Имитация задержки работы с диском/сетью без заморозки окна
        time.sleep(0.4)

        self.expenses.append(record)
        with open(self.db_path, "w", encoding="utf-8") as file:
            json.dump(
                {"expenses": self.expenses}, file, ensure_ascii=False, indent=4
            )

        # Возвращаем обновление интерфейса обратно в главный поток
        self.root.after(0, self.finish_saving, record)

    def finish_saving(self, record: dict):
        self.add_btn.config(state="normal")
        self.status_lbl.config(text="Статус: готово")
        self.item_entry.delete(0, tk.END)
        self.amount_entry.delete(0, tk.END)
        self.update_table()

        # 9. ДИАЛОГОВОЕ ОКНО (подтверждение)
        messagebox.showinfo(
            "Сохранено",
            f"Расход «{record['item']}» на {record['amount']} руб. добавлен.",
        )

    def update_table(self):
        # Очищаем таблицу перед перерисовкой
        for row in self.tree.get_children():
            self.tree.delete(row)

        total_sum = 0.0
        for exp in self.expenses:
            total_sum += exp["amount"]
            self.tree.insert(
                "",
                tk.END,
                values=(
                    exp["item"],
                    exp["category"],
                    exp["payment"],
                    f"{exp['amount']:.2f}",
                ),
            )

        self.total_lbl.config(text=f"Итого: {total_sum:.2f} руб.")


if __name__ == "__main__":
    root = tk.Tk()
    app = ExpenseTrackerApp(root)
    root.mainloop()
