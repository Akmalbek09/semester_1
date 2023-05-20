import csv
import datetime
import random
def read(a):
    nlist = []
    with open(a,"r") as csv_file:
        reader = csv.reader(csv_file)
        for x in reader:
            nlist.append(x)
    csv_file.close()
    return nlist
def write(a, nlist):
    with open(a,"w", newline='') as csv_file:
        reader = csv.writer(csv_file)
        reader.writerows(nlist)
def cheque(pizza,size,am,price,hour,minute):
    print(f"\tCheque: \nPizza: {pizza}\nNumber of pizza: {am}\nSize: {size}\nOrder time: {hour}:{minute}\nTotal cheque: {price}")
def delivery(price):
    delivery = price * 0.15
    # cheque()
print("Welcome user")
p = ["peperoni", "cheese", "vegan", "chicken"]
r = read("semester_1\Lesson_35\\archive.csv")
print(r)
for x in r:
    if x[0] in p:
        print(f"\t{x[0]}:\nS: ${x[1]}\nM: ${x[2]}\nL: ${x[3]}")
print("     LARGE        MEDIUM        SMALL")
print("")
print(f"   ********   ")
print(f"  **********      *******  ")
print(f" ************    *********      *******  ")
print(f" ************    *********     *********      ")
print(f" ************    *********     *********  ")
print(f"  **********      *******       ******* ")
print(f"   ********   ")
typep = int(input("one-in-one/two-in-one/custom: "))
if typep == 1:
    order = input("Choose pizza: ")
    size = input("What size do you want(S, M, L): ")
    c1 = 0
    for x in r[0]:
        if x == size:
            break
        c1 += 1
    c = 0
    for x in r:
        if x[0] == order:
            am = int(input("Enter number of pizzas: "))
            print(x[c1])
            price = am * float(x[c1])
            td = int(input("Takeout or delivery:"))
            # if td == 1:  
        c += 1











