list1 = ["apple", "banana", "cherry"]
list2 = ["potato", "tomato", "reddish"]
list3 = ["coca-cola", "pepsi", "fanta"]
orders = []
x = int(input("How many purchases do you need: "))
for a in range(0,x):
    a = input("Type your purchase: ")
    b = float(input("Type your quantity: "))
    if a in list1:
        print("Identity: Fruits")
        d = b * 4.83
        orders.append(f"{b} kg {a}s for ${d}")
    elif a in list2:
        c = b * 4.56
        print("Identity: Vagetables")
        orders.append(f"{b} kg {a}es for ${c}")
    elif a in list3:
        e = b * 0.89
        print("Identity: Drinks")
        orders.append(f"{b} {a}s for ${e}")


print("Your list of purchases:", orders)








    # else:
    #     print("Wrong item")
    # x = int(input("Type your quantity "))
    # if a in list1:
    #     print("Purchase:" ,x, a + "s", "for $" ,'%.2f' % (x * 0.69))
    # elif a in list2:
    #     print("Purchase:" ,x, a + "es", "for $" ,'%.2f' % (x * 0.78))
    # elif a in list3:
    #     print("Purchase:" ,x, a + "s", "for $" ,'%.2f' % (x * 0.89))
    # else:
    #     print("Error")







