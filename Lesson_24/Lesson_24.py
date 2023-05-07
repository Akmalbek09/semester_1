# my_list = [1,2,3,4,5,6]
# my_iter = iter(my_list)
# print(next(my_iter))
# myit = len(my_list)
# print(myit)

# try:
#     num > 3
# except:
#     print("oops error")
#     num = 3
# print(num,"This is num")

# try:
#     a = input("")
#     a is int
# except:
#     print("oops error")
# finally:
#     a = int(a)
#     print("Did you mean integer: ",a)

mail = input("Enter your address: ")
mylist = []
count = 0
for x in mail:
    if x == "@":
        mylist.append(mail[count+1:])
    count += 1
print(mylist)




















