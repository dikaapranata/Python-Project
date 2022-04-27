class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = list()
    
    def deposit(self, amount, desc=''):
        self.ledger.append({"amount": amount, "description": desc})

    def withdraw(self, amount, desc=''):
        if (self.check_funds(amount)):
            self.ledger.append({"amount": -amount, "description": desc})
            return True
        else:
            return False
    
    def get_balance(self):
        balance = 0
        for item in self.ledger:
            balance += item["amount"]
        return balance
    
    def transfer(self, amount, category):
        if (self.check_funds(amount)):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        else:
            return False

    def check_funds(self, amount):
        if (amount > self.get_balance()):
            return False
        else:
            return True

    def __str__(self):
        text = self.name.center(30, "*")
        for item in self.ledger:
            text += "\n"+item["description"][0:23].ljust(23)
            text += str(format(float(item["amount"]), '.2f')).rjust(7)
        text += f"\nTotal: {self.get_balance()}"
        return text

def create_spend_chart(categories):
    total_spend = dict()
    for category in categories:
        for item in category.ledger:
            if (item["amount"] < 0):
                total_spend[category.name] = total_spend.get(category.name, 0) - item["amount"]
    
    full_total_spend = sum(total_spend.values())
    
    percentageSpend = dict()
    for k, v in total_spend.items():
        percentageSpend[k] = total_spend[k] / float(full_total_spend) * 100

    lines = "Percentage spent by category\n"
    percentage = 100
    while (percentage >= 0):
        lines += percentage_spent(percentage, percentageSpend)
        percentage -= 10    
    lines += "    " + "-"*(3*len(total_spend)+1) + "\n"

    categoryLength = maxLength(total_spend)
    i = 0
    while (i < categoryLength):
        lines += "    "
        for k in total_spend:
            try:
                lines += " " + k[i] + " "
            except IndexError:
                lines += "   "
        i += 1
        if (i != categoryLength):
            lines += " \n"
        else:
            lines += " "

    return lines


def percentage_spent(percentage, spent):
    line = str(percentage).rjust(3)
    line += "|"
    for k, v in spent.items():
        if v >= percentage:
            line += " o "
        else:
            line += "   "
    line += " \n"
    return line

def maxLength(dictionary):
    maxLen = 0
    for k in dictionary:
        if len(k) > maxLen:
            maxLen = len(k)
    return maxLen
