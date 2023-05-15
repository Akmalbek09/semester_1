list1 = [1,2,3,4]
list2 = []
for x in list1:
    x = str(x)
    list2.append(x)
list2 = set((list2))
print(list2[0])
