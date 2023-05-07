# myset = {"Red", "Blue", "Green"}
# print(myset)
# for x in myset:
    # print(myset)
# numbers = range(0,11)
# my_list = list(numbers)
# new_list = []
# for x in my_list:
#     x = str(x)
#     new_list.append(x)
# new_set = set(new_list)
# print(new_set)

# myset = {"Red", "Blue", "Green"}
# myset.add("Vanilla")
# print(myset)
# myset = {1,2,3,4,5,6,7}
# myset2 = {"Red", "Blue", "Green"}
# myset.update(myset2)
# print(myset)

# myset = ["fruit", "drinks", "foods", "Vanilla"]
# myset2 = {"Choco", "Strawberry", "Vanilla"}
# myset2.update(myset)
# print(myset2)

# myset = {1,2,3,4,5, "Vanilla"}
# myset2 = {"Choco", "Red", "Vanilla", "Cherry"}
# myset2.intersection_update(myset)
# print(myset2)
# myset = {1,2,3,4,5, "Vanilla"}
# myset2 = {"Choco", "Red", "Vanilla", "Cherry"}
# myset2.symmetric_difference_update(myset)
# print(myset2)

# myset = {"a", "b", "c", "d", "e"}
# newps = []
# newset = {'1', '2', '3', '4'}
# newset2 = myset.update(newset)
# count = 0
# for x in myset:
#     count += 1
#     newps.append(x)
#     if count == 4:
#         break
# j = ""
# join = j.join(newps)
# print(join)

numbers = range(0,100)
mylist = list(numbers)
newlist = []
for x in mylist:
    x = str(x)
    newlist.append(x)
newset = set(newlist)
count = 0
for z in newset:
    count += 1
    if count == 1:
        num1 = z
num = int(num1)
print(num)
count2 = 0
for x in range(0,10):
    count2 += 1
    a = int(input("Type your guess: "))
    if a == num:
        print("You won!")
        break
    elif a > num:
        if count2 == 10:
            print("You lost")
            break
        print("The number is lower")
    elif a < num:
        if count2 == 10:
            print("You lost")
            break
        print("The number is higher")
    else:
        print("You lost!")
 










