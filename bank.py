
class BankAccount:
    def __init__(self, customer_id, name, starting_balance):
        self.customer_id = customer_id  # Unique customer ID
        self.name = name                  # Variable to hold name
        self.balance = starting_balance    # Variable to hold balance
        self.transactions = {}             # Dictionary to hold transactions

    def print_account_info(self):
        """Prints the account information."""
        print("Customer ID: " + str(self.customer_id))
        print("Name: " + self.name)
        print("Balance: $" + str(format(self.balance, '.2f')))

    def deposit(self, amount):
        """Deposits money into the account."""
        if amount > 0:
            self.balance += amount
            if "deposit" in self.transactions:
                self.transactions["deposit"] += amount
            else:
                self.transactions["deposit"] = amount
            print("Deposited: $" + str(format(amount, '.2f')))
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Withdraws money from the account."""
        if 0 < amount <= self.balance:
            self.balance -= amount
            if "withdrawal" in self.transactions:
                self.transactions["withdrawal"] += amount
            else:
                self.transactions["withdrawal"] = amount
            print("Withdrew: $" + str(format(amount, '.2f')))
        else:
            print("Withdrawal amount must be positive and less than or equal to balance.")

    def print_transactions(self):
        """Prints all transactions."""
        print("Transactions for " + self.name + " (ID: " + str(self.customer_id) + "):")
        for transaction_type, amount in self.transactions.items():
            print(transaction_type + ": $" + str(format(amount, '.2f')))


# Example usage
if __name__ == "__main__":
    # Creating an instance of BankAccount
    account1 = BankAccount(101, "John Doe", 500.0)

    # Printing account information
    account1.print_account_info()

    # Making some deposits
    account1.deposit(150.0)
    account1.deposit(50.0)

    # Making a withdrawal
    account1.withdraw(200.0)

    # Trying to withdraw more than the balance
    account1.withdraw(500.0)

    # Printing transactions
    account1.print_transactions()

    # Printing final account information
    account1.print_account_info()
class BankAccount:
    def __init__(self, customer_id, name, starting_balance):
        self.customer_id = customer_id  # Unique customer ID
        self.name = name                  # Variable to hold name
        self.balance = starting_balance    # Variable to hold balance
        self.transactions = {}             # Dictionary to hold transactions

    def print_account_info(self):
        """Prints the account information."""
        print("Customer ID: " + str(self.customer_id))
        print("Name: " + self.name)
        print("Balance: $" + str(format(self.balance, '.2f')))

    def deposit(self, amount):
        """Deposits money into the account."""
        if amount > 0:
            self.balance += amount
            if "deposit" in self.transactions:
                self.transactions["deposit"] += amount
            else:
                self.transactions["deposit"] = amount
            print("Deposited: $" + str(format(amount, '.2f')))
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Withdraws money from the account."""
        if 0 < amount <= self.balance:
            self.balance -= amount
            if "withdrawal" in self.transactions:
                self.transactions["withdrawal"] += amount
            else:
                self.transactions["withdrawal"] = amount
            print("Withdrew: $" + str(format(amount, '.2f')))
        else:
            print("Withdrawal amount must be positive and less than or equal to balance.")

    def print_transactions(self):
        """Prints all transactions."""
        print("Transactions for " + self.name + " (ID: " + str(self.customer_id) + "):")
        for transaction_type, amount in self.transactions.items():
            print(transaction_type + ": $" + str(format(amount, '.2f')))
            if "withdrawal" in self.transactions:
                self.transactions["withdrawal"] += amount
            else:
                self.transactions["withdrawal"] = amount
            print("Withdrew: $" + str(format(amount, '.2f')))
        else:
            print("Withdrawal amount must be positive and less than or equal to balance.")

    def print_transactions(self):
            if "withdrawal" in self.transactions:
                self.transactions["withdrawal"] += amount
            else:
                self.transactions["withdrawal"] = amount
            print("Withdrew: $" + str(format(amount, '.2f')))
        else:
            print("Withdrawal amount must be positive and less than or equal to balance.")

    def print_transactions(self):
            if "withdrawal" in self.transactions:
                self.transactions["withdrawal"] += amount
            else:
                self.transactions["withdrawal"] = amount
            print("Withdrew: $" + str(format(amount, '.2f')))
        else:
            print("Withdrawal amount must be positive and less than or equal to balance.")

    def print_transactions(self):
            if "withdrawal" in self.transactions:
                self.transactions["withdrawal"] += amount
            else:
                self.transactions["withdrawal"] = amount
            print("Withdrew: $" + str(format(amount, '.2f')))
        else:
            print("Withdrawal amount must be positive and less than or equal to balance.")

    def print_transactions(self):
            if "withdrawal" in self.transactions:
                self.transactions["withdrawal"] += amount
            else:
                self.transactions["withdrawal"] = amount
            print("Withdrew: $" + str(format(amount, '.2f')))
        else:
            print("Withdrawal amount must be positive and less than or equal to balance.")


