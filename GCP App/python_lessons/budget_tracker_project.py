# Personal Budget Tracker - A Complete Python Project
# This project combines everything you've learned: variables, functions, data structures, and control flow

print("=== PERSONAL BUDGET TRACKER ===")
print("A complete Python project to track your expenses and income")
print()

class BudgetTracker:
    """A simple budget tracking application."""
    
    def __init__(self):
        """Initialize the budget tracker."""
        self.transactions = []
        self.categories = {
            'income': ['salary', 'freelance', 'investment', 'gift', 'other_income'],
            'expense': ['food', 'transportation', 'entertainment', 'utilities', 
                      'healthcare', 'shopping', 'education', 'other_expense']
        }
    
    def add_transaction(self, amount, category, description, transaction_type):
        """
        Add a new transaction (income or expense).
        
        Args:
            amount (float): Amount of money
            category (str): Category of transaction
            description (str): Description of transaction
            transaction_type (str): 'income' or 'expense'
        """
        transaction = {
            'amount': amount,
            'category': category,
            'description': description,
            'type': transaction_type,
            'date': self._get_current_date()
        }
        self.transactions.append(transaction)
        print(f"Added {transaction_type}: ${amount:.2f} for {description}")
    
    def _get_current_date(self):
        """Get current date as string (simplified for this example)."""
        return "2024-12-07"  # In real app, you'd use datetime module
    
    def add_income(self, amount, category, description):
        """Add an income transaction."""
        if category in self.categories['income']:
            self.add_transaction(amount, category, description, 'income')
        else:
            print(f"Invalid income category. Use: {', '.join(self.categories['income'])}")
    
    def add_expense(self, amount, category, description):
        """Add an expense transaction."""
        if category in self.categories['expense']:
            self.add_transaction(amount, category, description, 'expense')
        else:
            print(f"Invalid expense category. Use: {', '.join(self.categories['expense'])}")
    
    def get_balance(self):
        """Calculate current balance (total income - total expenses)."""
        total_income = sum(t['amount'] for t in self.transactions if t['type'] == 'income')
        total_expenses = sum(t['amount'] for t in self.transactions if t['type'] == 'expense')
        return total_income - total_expenses
    
    def get_total_income(self):
        """Get total income."""
        return sum(t['amount'] for t in self.transactions if t['type'] == 'income')
    
    def get_total_expenses(self):
        """Get total expenses."""
        return sum(t['amount'] for t in self.transactions if t['type'] == 'expense')
    
    def get_expenses_by_category(self):
        """Get expenses grouped by category."""
        expense_by_category = {}
        for transaction in self.transactions:
            if transaction['type'] == 'expense':
                category = transaction['category']
                amount = transaction['amount']
                expense_by_category[category] = expense_by_category.get(category, 0) + amount
        return expense_by_category
    
    def get_income_by_category(self):
        """Get income grouped by category."""
        income_by_category = {}
        for transaction in self.transactions:
            if transaction['type'] == 'income':
                category = transaction['category']
                amount = transaction['amount']
                income_by_category[category] = income_by_category.get(category, 0) + amount
        return income_by_category
    
    def show_summary(self):
        """Display a summary of all finances."""
        print("=== BUDGET SUMMARY ===")
        print(f"Total Income: ${self.get_total_income():.2f}")
        print(f"Total Expenses: ${self.get_total_expenses():.2f}")
        print(f"Current Balance: ${self.get_balance():.2f}")
        
        if self.get_balance() >= 0:
            print("✅ You're in the green! Good job managing your budget.")
        else:
            print("⚠️ You're spending more than you earn. Consider reducing expenses.")
        print()
    
    def show_expense_breakdown(self):
        """Show expenses broken down by category."""
        expenses = self.get_expenses_by_category()
        if not expenses:
            print("No expenses recorded yet.")
            return
        
        print("=== EXPENSE BREAKDOWN ===")
        total_expenses = self.get_total_expenses()
        
        for category, amount in sorted(expenses.items(), key=lambda x: x[1], reverse=True):
            percentage = (amount / total_expenses) * 100 if total_expenses > 0 else 0
            print(f"{category.title()}: ${amount:.2f} ({percentage:.1f}%)")
        print()
    
    def show_income_breakdown(self):
        """Show income broken down by category."""
        income = self.get_income_by_category()
        if not income:
            print("No income recorded yet.")
            return
        
        print("=== INCOME BREAKDOWN ===")
        total_income = self.get_total_income()
        
        for category, amount in sorted(income.items(), key=lambda x: x[1], reverse=True):
            percentage = (amount / total_income) * 100 if total_income > 0 else 0
            print(f"{category.title()}: ${amount:.2f} ({percentage:.1f}%)")
        print()
    
    def show_recent_transactions(self, limit=5):
        """Show the most recent transactions."""
        if not self.transactions:
            print("No transactions recorded yet.")
            return
        
        print(f"=== RECENT TRANSACTIONS (Last {limit}) ===")
        recent = self.transactions[-limit:]
        
        for transaction in reversed(recent):
            sign = "+" if transaction['type'] == 'income' else "-"
            print(f"{sign}${transaction['amount']:.2f} | {transaction['category'].title()} | {transaction['description']}")
        print()
    
    def find_largest_expense(self):
        """Find the largest single expense."""
        expenses = [t for t in self.transactions if t['type'] == 'expense']
        if not expenses:
            return None
        
        largest = max(expenses, key=lambda x: x['amount'])
        return largest
    
    def find_largest_income(self):
        """Find the largest single income."""
        income = [t for t in self.transactions if t['type'] == 'income']
        if not income:
            return None
        
        largest = max(income, key=lambda x: x['amount'])
        return largest
    
    def get_spending_insights(self):
        """Provide insights about spending patterns."""
        print("=== SPENDING INSIGHTS ===")
        
        if not self.transactions:
            print("No data available for insights.")
            return
        
        # Largest transactions
        largest_expense = self.find_largest_expense()
        largest_income = self.find_largest_income()
        
        if largest_expense:
            print(f"💸 Largest expense: ${largest_expense['amount']:.2f} for {largest_expense['description']}")
        
        if largest_income:
            print(f"💰 Largest income: ${largest_income['amount']:.2f} from {largest_income['description']}")
        
        # Category insights
        expenses = self.get_expenses_by_category()
        if expenses:
            top_category = max(expenses.keys(), key=lambda x: expenses[x])
            print(f"🏷️ Top spending category: {top_category.title()} (${expenses[top_category]:.2f})")
        
        # Balance insight
        balance = self.get_balance()
        income = self.get_total_income()
        if income > 0:
            savings_rate = (balance / income) * 100
            print(f"📊 Savings rate: {savings_rate:.1f}% of income")
            
            if savings_rate > 20:
                print("🌟 Great job! You're saving more than 20% of your income.")
            elif savings_rate > 10:
                print("👍 Good savings rate. Consider increasing to 20%+ if possible.")
            elif savings_rate > 0:
                print("💡 You're saving money, but try to increase your savings rate.")
            else:
                print("⚠️ You're spending more than you earn. Time to budget!")
        print()


def demo_budget_tracker():
    """Demonstrate the budget tracker with sample data."""
    print("=== BUDGET TRACKER DEMO ===")
    
    # Create a new budget tracker
    budget = BudgetTracker()
    
    # Add some sample income
    print("Adding income transactions...")
    budget.add_income(3000, 'salary', 'Monthly salary')
    budget.add_income(500, 'freelance', 'Web design project')
    budget.add_income(100, 'gift', 'Birthday money')
    print()
    
    # Add some sample expenses
    print("Adding expense transactions...")
    budget.add_expense(800, 'food', 'Groceries and dining')
    budget.add_expense(1200, 'utilities', 'Rent and utilities')
    budget.add_expense(300, 'transportation', 'Gas and car maintenance')
    budget.add_expense(150, 'entertainment', 'Movies and games')
    budget.add_expense(200, 'shopping', 'Clothes and accessories')
    budget.add_expense(100, 'healthcare', 'Doctor visit')
    print()
    
    # Show various reports
    budget.show_summary()
    budget.show_income_breakdown()
    budget.show_expense_breakdown()
    budget.show_recent_transactions()
    budget.get_spending_insights()


# Interactive functions for user to try
def create_budget_tracker_tutorial():
    """Tutorial for creating your own budget tracker."""
    print("=== CREATE YOUR OWN BUDGET TRACKER ===")
    print("Here's how you can use this budget tracker:")
    print()
    
    print("1. Create a new budget tracker:")
    print("   my_budget = BudgetTracker()")
    print()
    
    print("2. Add income:")
    print("   my_budget.add_income(2500, 'salary', 'Monthly salary')")
    print("   my_budget.add_income(200, 'freelance', 'Side project')")
    print()
    
    print("3. Add expenses:")
    print("   my_budget.add_expense(600, 'food', 'Groceries')")
    print("   my_budget.add_expense(1000, 'utilities', 'Rent')")
    print()
    
    print("4. View reports:")
    print("   my_budget.show_summary()")
    print("   my_budget.show_expense_breakdown()")
    print("   my_budget.get_spending_insights()")
    print()
    
    print("Available income categories:", 
          ['salary', 'freelance', 'investment', 'gift', 'other_income'])
    print("Available expense categories:", 
          ['food', 'transportation', 'entertainment', 'utilities', 
           'healthcare', 'shopping', 'education', 'other_expense'])


if __name__ == "__main__":
    # Run the demo
    demo_budget_tracker()
    
    # Show tutorial
    create_budget_tracker_tutorial()
    
    print("=== PROJECT COMPLETE! ===")
    print("This budget tracker demonstrates:")
    print("✅ Classes and objects (object-oriented programming)")
    print("✅ Functions with parameters and return values")
    print("✅ Dictionaries and lists for data storage")
    print("✅ Loops and conditional statements")
    print("✅ String formatting and user-friendly output")
    print("✅ Data analysis and calculations")
    print()
    print("Try creating your own budget tracker and add more features!")
    print("Ideas for enhancements:")
    print("- Save data to a file")
    print("- Add date filtering")
    print("- Create spending budgets by category")
    print("- Add data visualization with charts")
    print("- Build a web interface")
    print("- Add recurring transactions")