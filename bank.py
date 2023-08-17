class Bank:
    def __init__(self):
        self.name = ""
        self.add = ""
        self.balance = 0
        self.amount = 0

    def open_account(self):
        print("Enter your full name:")
        self.name = input()
        print("Enter your address:")
        self.add = input()
        print("What type of account do you want to open (saving 's' or current 'c'):")
        self.y = input()
        print("Enter amount for deposit:")
        self.balance = int(input())
        print("Your account is created")

    def deposit_money(self):
        print("Enter how much money you want to deposit:")
        a = int(input())
        self.balance += a
        print("Your total deposit amount:", self.balance)

    def display_account(self):
        print("Name:", self.name)
        print("Address:", self.add)
        print("Type of account:", self.y)
        print("Balance:", self.balance)

    def withdraw_money(self):
        print("Enter the amount you want to withdraw:")
        self.amount = int(input())
        self.balance -= self.amount
        print("Now your total amount is left:", self.balance)


if __name__ == "__main__":
    bank_obj = Bank()

    while True:
        print("\n1) Open account")
        print("2) Deposit money")
        print("3) Withdraw money")
        print("4) Display account")
        print("5) Exit")
        choice = int(input("Please select an option: "))

        if choice == 1:
            bank_obj.open_account()
        elif choice == 2:
            bank_obj.deposit_money()
        elif choice == 3:
            bank_obj.withdraw_money()
        elif choice == 4:
            bank_obj.display_account()
        elif choice == 5:
            print("Exit")
            break
        else:
            print("This is not a valid option. Please try again.")
