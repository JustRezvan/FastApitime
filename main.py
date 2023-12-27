import tkinter as tk

# Создание главного окна
window = tk.Tk()
window.title("Banking App")
window.geometry("500x400")

# Класс для банковского аккаунта
class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
        self.transaction_history = []

    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append(f"Депозит: +{amount} руб.")
        self.display_balance()

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.transaction_history.append(f"Снятие: -{amount} руб.")
        else:
            self.transaction_history.append("Недостаточно средств")
        self.display_balance()

    def display_balance(self):
        balance_label.config(text=f"Текущий баланс: {self.balance} руб.")

    def display_history(self):
        history_window = tk.Toplevel(window)
        history_window.title("История транзакций")

        scrollbar = tk.Scrollbar(history_window)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        history_text = tk.Text(history_window, yscrollcommand=scrollbar.set)
        history_text.pack()

        for transaction in self.transaction_history:
            history_text.insert(tk.END, f"{transaction}\n")

        scrollbar.config(command=history_text.yview)

# Создание экземпляра класса BankAccount
account = BankAccount("Иванов Иван", 1000)

# Элементы интерфейса
label_title = tk.Label(window, text="Банковский аккаунт", font=("Arial", 18))
label_title.pack(pady=10)

frame_buttons = tk.Frame(window)
frame_buttons.pack(pady=20)

def open_deposit_window():
    deposit_window = tk.Toplevel(window)
    deposit_window.title("Пополнить счет")

    label_deposit = tk.Label(deposit_window, text="Введите сумму:")
    label_deposit.pack()

    entry_deposit = tk.Entry(deposit_window)
    entry_deposit.pack()

    def deposit():
        amount = float(entry_deposit.get())
        account.deposit(amount)
        deposit_window.destroy()

    button_deposit = tk.Button(deposit_window, text="Пополнить", command=deposit)
    button_deposit.pack()

def open_withdraw_window():
    withdraw_window = tk.Toplevel(window)
    withdraw_window.title("Снять со счета")

    label_withdraw = tk.Label(withdraw_window, text="Введите сумму:")
    label_withdraw.pack()

    entry_withdraw = tk.Entry(withdraw_window)
    entry_withdraw.pack()

    def withdraw():
        amount = float(entry_withdraw.get())
        account.withdraw(amount)
        withdraw_window.destroy()

    button_withdraw = tk.Button(withdraw_window, text="Снять", command=withdraw)
    button_withdraw.pack()

button_deposit = tk.Button(frame_buttons, text="Пополнить счет", width=15, command=open_deposit_window)
button_deposit.pack(side=tk.LEFT, padx=10)

button_withdraw = tk.Button(frame_buttons, text="Снять со счета", width=15, command=open_withdraw_window)
button_withdraw.pack(side=tk.LEFT, padx=10)

button_history = tk.Button(window, text="История транзакций", width=15, command=account.display_history)
button_history.pack()

balance_label = tk.Label(window, text="")
balance_label.pack()

# Отображение начального баланса
account.display_balance()

# Запуск приложения
window.mainloop()
