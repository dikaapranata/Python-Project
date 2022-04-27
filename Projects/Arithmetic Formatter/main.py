import re

def arithmetic_arranger(arithmetics, answer=False):
    # error check 1 (list length)
    if len(arithmetics) > 5:
        return "Error: Too many problems."
    
    firstLine = ""
    secondLine = ""
    thirdLine = ""
    if (answer):
        fourthLine = ""

    for num, arithmetic in enumerate(arithmetics):
        # jika bukan loop pertama, tambahkan 4 spasi di setiap baris
        if (num != 0):
            firstLine = firstLine + "    "
            secondLine = secondLine + "    "
            thirdLine = thirdLine + "    "
            if (answer):
                fourthLine = fourthLine + "    "

        splittedArithmetic = re.split(" ", arithmetic)
        num1 = splittedArithmetic[0]
        num2 = splittedArithmetic[2]
        operator = splittedArithmetic[1]

        # error check 2 (operator)
        if (operator != '+' and operator != '-'):
            return "Error: Operator must be '+' or '-'."
        
        # error check 3 (number must contain only digit)
        if (not num1.isnumeric() or not num2.isnumeric()):
            return "Error: Numbers must only contain digits."

        # error check 4
        if (len(num1) > 4 or len(num2) > 4):
            return "Error: Numbers cannot be more than four digits."
        
        # turning into formatted
        if (len(num1) > len(num2)):
            width = len(num1) + 2
        else:
            width = len(num2) + 2
        
        firstLine = firstLine + num1.rjust(width)
        secondLine = secondLine + operator + num2.rjust(width - 1)
        thirdLine = thirdLine + '-'*width

        if (answer):
            if (operator == '+'):
                sum = int(num1) + int(num2)
            else:
                sum = int(num1) - int(num2)
            fourthLine = fourthLine + str(sum).rjust(width)
        # end of loop

    if (answer):
        return firstLine + "\n" + secondLine + "\n" + thirdLine + "\n" + fourthLine
    else:
        return firstLine + "\n" + secondLine + "\n" + thirdLine


print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True))