import budget
from budget import create_spend_chart

expected = "Percentage spent by category\n100|          \n 90|          \n 80|          \n 70|    o     \n 60|    o     \n 50|    o     \n 40|    o     \n 30|    o     \n 20|    o  o  \n 10|    o  o  \n  0| o  o  o  \n    ----------\n     B  F  E  \n     u  o  n  \n     s  o  t  \n     i  d  e  \n     n     r  \n     e     t  \n     s     a  \n     s     i  \n           n  \n           m  \n           e  \n           n  \n           t  "
print(repr(expected))

business = budget.Category("Business")
food = budget.Category("Food")
entertainment = budget.Category("Entertainment")

business.deposit(900, "initial deposit")
food.deposit(900, "initial deposit")
entertainment.deposit(900, "initial deposit")

business.withdraw(10.99)
entertainment.withdraw(33.40)
food.withdraw(105.5)

print(repr(create_spend_chart([business, food, entertainment])))

