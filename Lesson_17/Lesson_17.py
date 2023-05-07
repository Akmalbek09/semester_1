# def aki():
#     print("Hello")
# aki()
# def aki(name):
#     print(f"Hello {name}")
# a = input("")
# aki(a)

# def args(*name):
#     print(f"{name}")
#     print(type(name))
# args("Akmalbek", "Abdurakhmonov", 13)
# list1 = []
# def name_catch(name):
#     list1.append(name)
# r = input("Enter your name: ")
# name_catch(r)
# print(list1)
# nums = range(0,10)
# listnum = list(nums)
# listodd = []
# listeven = []
# def num(list):
#     for x in list:
#         if x % 2:
#             listodd.append(x)
#         else:
#             listeven.append(x)
# num(nums)
# print(listodd)
# print(listeven)

# list1 = []
# def my_function(a):
#     list1.append(a)
# r = input("")
# my_function(r)
# print(list1)

# def value(job = "Jobless"):
#     print("My occupation is ",job)
# value()
# value("Programmer")
# value("Web-designer")

# def list_function(lists):
#     for x in lists:
#         print(x)

# list1 = [1,2,3,4,5,6,7]
# list2 = ("Apple", "Banana", "Cherry")
# list_function(list1)
# list_function(list2)
# def p(content):
#     print(content)

# mydict = dict(sweets = ["oreo","bounty","chocopie"], s_price = [4,5,3])
# print(mydict)
# menu = input("Menu: ")
# list_korzinka = []
# def add_item(item):
#     list_korzinka.append(item)
# if menu == "1":
#     categor = input("Choose your categor: ")
#     p(mydict[categor])
#     item = input("choose item")
#     add_item(item)
# if menu == "2":
#     print(list_korzinka)

# def upper_funct(uptxt):
#     for x in uptxt:
#         x = str(x).upper()
# def akmal_function(text):
#     listglas = 'aeiou'
#     consonants = "bcdfghjklmnpqrstvwxyz"
#     count1 = 0
#     count2 = 0
#     for x in text:
#         if x in consonants:
#             count1 += 1
#     print("Soglasniy:",count1)
#     for y in text:
#         if y in listglas:
#             count2 += 1
#     print("Glasniy:",count2)
#     count = 0
#     for a in text:
#         count += 1
#     print("Length:", count)
# t = input("").lower()
# akmal_function(t)

# def perimetr(a,b):
#     per = (a + b) * 2
#     return per

# def ploshad(a,b):
#     plosh = a * b
#     return plosh

# def objem(a,b,h):
#     obj = a * b * h
#     return obj

# one = int(input("Perimetr first side: "))
# two = int(input("Perimetr second side:" ))
# print("Perimetr",perimetr(one,two))

# a = int(input("Ploshad first side:"))
# b = int(input("Ploshad second side:"))
# print("Ploshad", ploshad(a,b))

# a = int(input("Type your first value "))
# b = int(input("Type your second value: "))
# h = int(input("Type your height: "))
# print(objem(a,b,h))

# def percent_function(x,y):
#     pers = (x * 100) / y
#     return pers
# x = int(input("Type your digit: "))
# y = int(input("Type your percentage of your digit(%): "))
def priyamo_function(a,b):
    diagonal = (((a**2) + (b**2)))**1/2
    return diagonal
def square_function(a):
    diag = (a * 2)**1/2
    return diag
n = input("What shape is it: ")
if n == "square":
    a = int(input("Type your value: "))
    print(square_function(a))
elif n == "rectangular":
    c = int(input("Type your first value: "))
    b = int(input("Type your second value: "))
    print(priyamo_function(c,b))















