# Не изменяемые
# Bool represents a "True" or "False"
 
print(10 < 9)
print(10 > 9)
print(10 == 9)
# 2
a = 100
b = 200
if a > b:
    print("a is bigger than b")
elif a < b:
    print("b is bigger than a")
else:
    print("They\'re both equal")


# Tuple a collection with multiple items which is ordered and unchangeable
thistuple = ("apple", "banana", "cherry")
print((thistuple))
mytuple = ("apple",)#with comma
print(type(mytuple))


# Frozenset an unchangeable list or iterable
mylist = ["Apple", "Banana", "Cherry"]
x = frozenset(mylist)
print(x)
# x[1] = "Peach" error

# Bin
a = bin(0)
b = bin(1)
c = bin(2)
d = bin(3)
x = bin(4)
z = bin(5)
print(a, b, c, d, x)

# Complex
x = complex(5, 10)
print(x)


# Изменяемые List used with multiple items and changeable
thislist = [2, 3, 4]
print(thislist)
mylist = ["appla", "cherry", "banana", "apple", "cherry"]
print(mylist)
print(len(mylist))
mylist[0] = "strawberry"
print(mylist)
list1 = ["apple", "banana", "cherry"]
print(list1)
list2 = [1, 2, 3, 4]
print(list2)
list2[0] = 5
print(list2)
list3 = [True, False, False]
print(list3)

#Dictionary is used to store data and is a collection of changeable non-duplicate items
thisdict = {
    "brand" : "Lamborghini",
    "Model" : "Aventador",
    "Year"  : 2011
}
thisdict2 = {
    "brand" : "Lamborghini",
    "Model" : "Aventador",
    "Year"  : 2011,
    "Year"  : 2009
}
thisdict3 = {
    "brand" : "Lamborghini",
    "Electric" : False,
    "Year"  : 2011,
    "Color"  : ["Grey", "White", "Black"]
}
mydict = dict(name = "John" , age = 13, surname = "Abdurakhmonov")
mydict = dict(brand = "Lamborghini" , Model = "Aventador", Electric = False, Year = 2011)#Same as the others
print(mydict)
print(thisdict)
print(thisdict["brand"])
print(len(thisdict))
print(thisdict2)
print(thisdict3)


# Set is used to store multiple items and is unchangeable, but capable of removing and adding items and non-duplicate
myset = {"apple","banana", "cherry",}
myset2 = {"apple","banana", "cherry","apple","cherry"}
myset3 = {10 < 9, 10 > 9,}
thisset = set(("apple", "banana", "cherry"))
print(myset)
print(myset2)
print(len(myset))
print(myset3)
print(len(myset3))
print(thisset)



