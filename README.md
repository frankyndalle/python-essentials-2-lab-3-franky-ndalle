
# Python Essentials 2 — Lab 3
## Object-Oriented Programming

**Author:** Franky Ndalle

## Task 1: BankAccount

**File:** `bank.py`

Implements the `BankAccount` class with the `account_number`, `owner`, and `balance` attributes. The class supports deposits, withdrawals, and a readable string representation. Deposits and withdrawals must be positive amounts, and withdrawals cannot exceed the available balance.

The custom `InsufficientFundsError` exception is raised when a withdrawal exceeds the account balance. The test code demonstrates successful transactions and exception handling.

## Task 2: SavingsAccount

**File:** `savings.py`

Implements `SavingsAccount` as a subclass of `BankAccount`. It uses `super().__init__()` to initialize inherited attributes, adds an `interest_rate` attribute, and provides `apply_interest()` to add interest to the balance. Its overridden `__str__()` method displays the interest rate.

The test code demonstrates inherited deposits and withdrawals, interest calculation, and insufficient-funds handling.

## Task 3: Custom Exception

The optional `InsufficientFundsError` class is defined in `bank.py`. It inherits from Python's built-in `Exception` class and is caught specifically in both test programs.

## Sample Output Evidence

The `outputs` folder contains text logs demonstrating both programs:

- `outputs/bank_output.txt`
- `outputs/savings_output.txt`

## How to Run

Run these commands from the project folder:

```bash
python bank.py
python savings.py
```

## Requirements

- Python 3
- No third-party packages required
