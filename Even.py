class BankAccount:
    balance = 0

    @classmethod
    def deposit(cls, amount):
        cls.balance += amount
        print(f"Amount deposited: {amount}")

    @classmethod
    def withdraw(cls, amount):
        if cls.balance >= amount:
            cls.balance -= amount
            print(f"Amount withdrawn: {amount}")
        else:
            print("Insufficient balance")

    @classmethod
    def display_balance(cls):
        print(f"Current balance: {cls.balance}")


# Example usage
BankAccount.deposit(1000)
BankAccount.display_balance()
BankAccount.withdraw(500)
BankAccount.display_balance()

