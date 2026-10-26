
# Lab 3 - Task 2: SavingsAccount and Inheritance

from bank import BankAccount, InsufficientFundsError


class SavingsAccount(BankAccount):
    """Represent a savings account that earns annual interest."""

    def __init__(self, account_number, owner, balance=0, interest_rate=5):
        # Initialize the inherited BankAccount attributes.
        super().__init__(account_number, owner, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        """Calculate and add interest based on the current balance."""
        interest = self.balance * (self.interest_rate / 100)
        self.balance += interest
        return self.balance

    def __str__(self):
        """Include the interest rate in the account description."""
        return (
            f"Account {self.account_number} - Owner: {self.owner}, "
            f"Balance: ${self.balance:.2f}, "
            f"Interest Rate: {self.interest_rate}%"
        )


if __name__ == "__main__":
    # Create a savings account with a $1,000 balance and 5% interest.
    savings = SavingsAccount("67890", "Bob", 1000, 5)
    print("Initial savings account:", savings)

    # Demonstrate the inherited deposit method.
    savings.deposit(200)
    print("After deposit:", savings)

    # Demonstrate the inherited withdrawal method.
    savings.withdraw(100)
    print("After withdrawal:", savings)

    # Apply interest to the updated balance.
    savings.apply_interest()
    print("After applying interest:", savings)

    # Confirm that inherited exception handling also works.
    try:
        savings.withdraw(5000)
    except InsufficientFundsError as error:
        print("Insufficient funds error:", error)
