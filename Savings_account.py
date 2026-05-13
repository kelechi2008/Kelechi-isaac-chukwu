from Account import Account


class SavingsAccount(Account):
    def __init__(self, owner, balance=0, interest_rate=0.02, withdraw_limit=100):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate
        self.withdraw_limit = withdraw_limit

    def withdraw(self, amount):
        if amount > self.withdraw_limit:
            print(f"Withdrawal denied: Savings account limit is ${self.withdraw_limit}.")
            return

        super().withdraw(amount)

    def apply_interest(self):
        interest = self.get_balance() * self.interest_rate
        self.deposit(interest)
        print(f"Interest of ${interest} applied.")

print("--- Savings Account ---")
savings = SavingsAccount("Alice", 1000)
savings.withdraw(1000)
savings.apply_interest()
