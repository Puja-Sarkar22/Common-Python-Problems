class BankAccount:
    total_deposits = 0
    total_withdrawals = 0
    balance = 0

    @classmethod
    def deposit(cls, amount):
        cls.balance += amount
        cls.total_deposits += amount

    @classmethod
    def withdraw(cls, amount):
        if cls.balance >= amount:
            cls.balance -= amount
            cls.total_withdrawals += amount
        else:
            print("Insufficient funds!")

    @classmethod
    def display(cls):
        print(f"Total Deposits: {cls.total_deposits}")
        print(f"Total Withdrawals: {cls.total_withdrawals}")
        print(f"Balance: {cls.balance}")


while True:
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Display Balance and Transactions")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        amount = float(input("Enter amount to deposit: "))
        BankAccount.deposit(amount)
    elif choice == '2':
        amount = float(input("Enter amount to withdraw: "))
        BankAccount.withdraw(amount)
    elif choice == '3':
        BankAccount.display()
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please try again.")
