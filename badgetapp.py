class Category:
    def __init__(self,name,ledger=None):
        self.name = name
        if ledger is None:
            self.ledger = []
        else:
            self.ledger = ledger
    def deposit(self,amount,description=''):  
        self.ledger.append({"amount": float(amount), "description": description})        

    def withdraw(self,amount,description=''):
        if self.check_funds(amount):
            self.ledger.append({"amount": float(-amount), "description": description})
            return True
        else:
            return False 

    def get_balance(self): 
        total = 0
        for item in self.ledger:
            total += item['amount']
        return total    

    def check_funds(self,amount):
        if amount <= self.get_balance():
            return True
        else:
            return False     
    def transfer(self,amount,category):
        if self.withdraw(amount, f"Transfer to {category.name}"):
            category.deposit(amount,f"Transfer from {self.name}")
            return True
        else:
            return False    
    def __str__(self):
        title = self.name.center(30, '*') + '\n'
        items = '' 
        for category in self.ledger:
            descr = category['description'][:23] 
            amt = f"{category['amount']:.2f}"
            items += f"{descr:<23}{amt:>7}\n"
        total = f"Total: {self.get_balance()}" 
        return title + items + total   
def create_spend_chart(categories):
    title = "Percentage spent by category\n"

    # Get total withdrawals per category
    spent = []
    total_spent = 0

    for cat in categories:
        cat_spent = 0
        for item in cat.ledger:
            if item['amount'] < 0:
                cat_spent += -item['amount']
        spent.append(cat_spent)
        total_spent += cat_spent

    # Convert to percentages (rounded down to nearest 10)
    percentages = [(int((s / total_spent) * 100) // 10) * 10 for s in spent]

    # Build chart
    chart = title
    for i in range(100, -1, -10):
        line = f"{i:>3}| "
        for p in percentages:
            if p >= i:
                line += "o  "
            else:
                line += "   "
        chart += line + "\n"

    # Horizontal line
    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    # Vertical names
    max_len = max(len(cat.name) for cat in categories)

    for i in range(max_len):
        line = "     "
        for cat in categories:
            if i < len(cat.name):
                line += cat.name[i] + "  "
            else:
                line += "   "
        chart += line.rstrip() + "\n"

    return chart.rstrip()
food = Category('Food')
food.deposit(1000, 'initial deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
print(food)

print(create_spend_chart([food,clothing]))

