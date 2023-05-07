# list = [1,2,3,4,5,6,7,8,9]
# for x in list:
#     a = list[-x]
#     list1 = []
#     list1.append(a)
#     print(list1)
# my_list = ["red","blue", "green"]
# list = []
# a = input("")
# for x in my_list:
#     if a == x:
#         z = a.upper()
#         my_list.append(z)
#         print(my_list,z)
    # elif a not in x:
    #     list.append(x)
    #     print(list)
# my_list = ["red","blue", "green"]
# # listcopy = my_list
# # print(listcopy)
# list_copy = [x for x in my_list if "b" in x]
# print(list_copy.upper())
list1 = ["BMW,",  "Merscedez,", "Lamborghini,", "Tesla,", "BYD,","Gucci.", "Louis Vitton.", "Dolce Gabbanna.", "Prada.", "Pandora.","Fortnite_", "Toys_", "Disney_", "Cartoons_", "Minecraft_"]
a = input("Who are you? ").upper()
list = []
for x in list1:
    if a == "DAD":
        if "," in x:
            print("Dad's category:",x)
            list.append(x)
    elif a == "MOM":
        if "," in x:
            print("Mom's category:",x)
            list.append(x)
    elif a == "ADULT" or a == "CHILD":
        if "_" in x:
            print("Adult's category:",x)
            list.append(x)
listnum = [1,2,3,4,5]
counter1 = 0
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
            print("What have you bought so far from the listTes?")
            print(list)
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







































