counter1 = 0
counter2 = 0
for all in range(0,3):
    counter2 += 1
    counter1 = counter1 + 1
    print("List №:",counter2)
    list = []
    b = int(input("How many purchases you have: "))
    for x in range(0,b):
        a = input("Type your purchases: ")
        list.append(a)
        if a.isdigit():
            print("List dont contain any digits")
            a = input("Type your purchases: ")
            list.append(a)
    listnum = [1,2,3,4,5]
    for i in listnum:
        if i == 1:
            print("\tPress",i, "to show the list")
        if i == 2:
            print("\tPress",i, "to remove an item from the list")
        if i == 3:
            print("\tPress",i, "to add an item into the list")
        if i == 4:
            print("\tPress",i, "to delete the list")
        if i == 5:
            print("\tPress",i, "to quit from the app")
    for range in range(0,100):
        num = int(input())
        if num == 1:
            print("Your list: ",list)
            continue
        if num == 2:
            print("What have you bought so far?")
            c = input("")
            if c in list:
                list.remove(c)
                print("The rest: ",list)
                continue
            else:
                print("It is not in your list")
                continue
        if num == 3:
            add = input("Add to list: ")
            list.append(add)
            print("Your list",list)
            continue
        if num == 4:
            finale = input("Are you done? ")
            if finale == "yes":
                del list
                break
        if num == 5:
            break
    print("New list?")
    end = input("")
    if end == "yes":
        continue
    elif end == "no":
        break

