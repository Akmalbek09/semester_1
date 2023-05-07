amount = int(input("How many do you want: "))
product = []
sum = 0
for x in range(0,amount):
    pro = input("Fruit: ")
    quantity = int(input("Type the quantity: "))
    p = quantity * 1.78
    product.append(pro)
if amount > 1:
    sum = p + p
else:
    sum = p
mydict = {
    "Products" : product,
    "Total price" : f"${sum}"
}
print(mydict)
change = input("Do you want a change?(yes/no): ")
if change == "yes":
    listnum = [1,2,3]
    for i in listnum:
        if i == 1:
            print("\tPress",i, "to add an item into the list")
        if i == 2:
            print("\tPress",i, "to remove an item from the list")
        if i == 3:
            print("\tPress",i, "to delete the list")
    num = int(input())
    if num == 1:
        add1 = input("Type your product: ")
        add = list(mydict["Products"])
        add.append(add1)
        mydict["Products"] = add
    if num == 2:
        remove = input("Type to remove: ")
        rem = list(mydict["Products"])
        if remove in rem:
            rem.remove(remove)
        mydict["Products"] = rem
    if num == 3:
        del mydict    
print(mydict)











