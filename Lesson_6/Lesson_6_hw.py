# HW
# 1
num1 = float(input("Type your numeral:  "))
oper = input("Type your operator(+, -, *, /):  ").lower()
num2 = float(input("Type your second numeral:  "))
if oper == "+":
    print("%.2f" % (num1 + num2))
elif oper == "-":
    print("%.2f" % (num1 - num2))
elif oper == "*" or oper == "x":
    print("%.2f" % (num1 * num2))
elif oper == "/":
    print("%.2f" % (num1 // num2))
else:
    print("Error, try again!")

