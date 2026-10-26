
# Lab 3 - Task 1: BankAccount and Custom Exception


class InsufficientFundsError(Exception):
    """Raised when a withdrawal exceeds the available balance."""
    pass


class BankAccount:
    """Represent a bank account with deposit and withdrawal methods."""

    def __init__(self, account_number, owner, balance=0):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        """Add a positive amount to the account balance."""
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")

        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        """Withdraw money when the amount is valid and funds are sufficient."""
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")

        if amount > self.balance:
            raise InsufficientFundsError(
                f"Cannot withdraw ${amount:.2f} from account "
                f"{self.account_number}; insufficient funds."
            )

        self.balance -= amount
        return self.balance

    def __str__(self):
        """Return a readable description of the account."""
        return (
            f"Account {self.account_number} - Owner: {self.owner}, "
            f"Balance: ${self.balance:.2f}"
        )


if __name__ == "__main__":
    # Create an account and demonstrate a successful deposit and withdrawal.
    account = BankAccount("12345", "Alice", 500)
    print("Initial account:", account)

    account.deposit(200)
    print("After deposit:", account)

    account.withdraw(100)
    print("After withdrawal:", account)

    # Attempt to withdraw more than the available balance.
    try:
        account.withdraw(1000)
    except InsufficientFundsError as error:
        print("Insufficient funds error:", error)

    # Demonstrate that a non-positive deposit is rejected.
    try:
        account.deposit(0)
    except ValueError as error:
        print("Deposit error:", error)
