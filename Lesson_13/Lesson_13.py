# num = [1,5,3,6,7,34,6]
# num.sort()
# print(num)
# num = [1,4,3,5,5,2,6,7,9,8]
# list = []
# counter = 0
# for x in num:
#     counter += 1
#     if counter in num:
#         list.append(counter)
#     elif x == counter:
#         list.append(counter)
# print(list)
# listcars = ["BMW", "Merscedez", "Tesla", "Man", "GM"]
# listcars.sort()
# print(listcars)
# listcars.sort(reverse=True)
# print(listcars)
# listcars = ["BMW", "Merscedez", "Tesla", "Man", "GM"]
# listnum = [1,2,3,4,5]
# addlist = listcars + listnum
# print(addlist)
# tuple = ("Ramziddin",)
# print(type(tuple))
# nottuple = ("Ramziddin")
# print(type(nottuple))

# mytuple = ["Father", "Mother", "Me", "Sister"]
# mylist = list(mytuple)
# mylist[3] = "Brother"
# mytuple = tuple(mylist)
# print(mytuple)
mytuple = ("Hacker", "Programmer", "Designer", "Cyber security")
a = input("")
if a == "admin":
    print(mytuple)
    b = (input("Which one edit:"))
    c = input("Edit:")
    if b in mytuple:
        mylist = list(mytuple)
        mylist.remove(b)
        mylist.append(c)
        mytuple = tuple(mylist)
        print(mytuple)
else:
    print("You dont have the access here")



















