# mydict = {
    # "Fruit":"Apple",
    # "Family":"Mother",
    # "No":1
# }
# mydict = {
#     "Fruit":"Apple",
#     "Family":"Mother",
#     "No":1,
#     "No":2,
#     "Items": ["computer", "phone", "laptop"],
#     "Story":True
# }
# print(mydict["Family"])
# print(len(mydict))
# print(mydict)
# print(mydict["Items"])
# mydict = dict(Cars = "Electric", Car1 = "Tesla", Model = "Model X", Year = 1990)
# print(mydict)
# print(mydict.keys())
# print(mydict.get("Cars"))
# mydict["Car2"] = "BYD"
# print(mydict)
# mydict = dict(Cars = "Electric", Car1 = "Tesla", Model = "Model X", Year = 1990)
# mydict["Year"] = 2009
# print(mydict)
# mydict.update({"Model" : "Model S"})
# print(mydict)
# mydict = dict(Cars = "Electric", Car1 = "Tesla", Model = "Model X", Year = 1990)
# # mydict.clear()

# for x in mydict.values():
#     print(x)
list1 = int(input("Quantity: "))
list3 = []
for r in range(0,list1):
    list2 = input("Fruits: ")
    
    list3.append(list2)
mydict = {
    "Quantity" : list1,
    "Fruits" : list3
}
print(mydict)
change = input("Category: ")
for x in mydict:
    if change == "Fruits":
        fruit = input("Fruit: ")
        mydictlist = list(mydict["Fruits"])
        mydictlist.append(fruit)
        mydict["Fruits"] = mydictlist
    if change == "Quantity":
        amount = input("Amount")
        amountlist = list(mydict["Quantity"])
        amountlist.append(amount)
        mydict["Qunatity"] = amountlist
print(mydict)


















