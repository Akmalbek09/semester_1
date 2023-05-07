# # x = "Akmalbek"
# # a = 7.5
# # print(type(x))
# # print(type(a))

# # a = "Russia"
# # def myfunc():
# #     print("Language is  " + x)
# # myfunc()

# # for x in "Ramziddin":
#     # print(x)

# # a = "I am uzbek"
# # print(len(a))

# # txt = "I will"
# # print("will" in txt)
# # print("will" not in txt)

# age = 36,'years old'
# txt = "My name is Akmalbek I am {0}"
# print(txt.format(age))

# a = input("Type your amount: ")
# b = input("Type your item: ")
# c = input("Type your price: ")
# myorder = f"I wanna pay {c} dollars for {a} pieces of item {b}"
# print(myorder)



# HW


# 1
# a = "I am bad boy"
# print(a.replace("bad", "good"))


# 2
curr1 = input("Enter your currency (USD / UZS / EUR): ").upper()
curr2 = input("Enter your transfer-currency (USD / UZS / EUR): ").upper()
value = float(input("Enter value: "))
if curr1 == "USD" and curr2 == "UZS":
    print('%.2f' % (value * 11000), "sum")
elif curr1 == "USD" and curr2 == "EUR":
    print('%.2f' % (value * 0.92), "€")
elif curr1 == "UZS" and curr2 == "USD":
    print("$",'%.2f' % ( value / 11000))
elif curr1 == "UZS" and curr2 == "EUR":
    print('%.2f' % (value / 12000), "€")
elif curr1 == "EUR" and curr2 == "USD":
    print("$", '%.2f' % (value / 0.92))
elif curr1 == "EUR" and curr2 == "UZS":
    print('%.2f' % (value * 12000), "sum")
else:
    print("Wrong currency, try again!")






