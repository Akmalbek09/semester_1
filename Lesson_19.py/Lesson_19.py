def max_num(b):
    counter = 0
    max = b[0]
    for x in b:
        if max < x:
            max = b[counter]
        else:
            pass
        counter += 1
    print(max)
def min_num(b):
    counter = 0
    min = b[0]
    for x in b:
        if min > x:
            min = b[counter]
        else:
            pass
        counter += 1
    print(min)

num = [23,45,34,99,78,34]
min_num(num)
max_num(num)

def num_sort(a):
    list1 = []
    for x in a:

num = [23,45,34,99,78,34]
num_sort(num)


# num = lambda a : a * 5
# print(num(5))

listglas = 'aeiou'
consonants = "bcdfghjklmnpqrstvwxyz"
txt = input("Enter your text: ").lower()
count = 0
count2 = 0
name = ""
for x in txt:
    if x in listglas:
        count += 1
        name = name + x.upper()
    if x in consonants:
        count2 += 1
        name = name + x
print("Glasniy: ",count,txt)
print("Soglasniy: ",count2)
print(name)



















