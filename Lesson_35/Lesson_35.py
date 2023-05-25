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
def cheque(a,pizza,spizza,size,am,top,cheese,dough,fee,price):
    if a == 1:
        return f"\nName: {pizza}\nNumber of pizza: {am}\nSize: {size}\nPrice: ${price}"
    elif a == 3:
        return f"\nName: {pizza}\nDough: {dough}\nToppings: {top}\nCheese: {cheese}\nNumber of pizza: {am}\nSize: {size}\nFee: ${fee}\nPrice: ${price}"
    elif a == 2:
        return f"\nFirst half: {pizza}\nSecond half: {spizza}\nNumber of pizza: {am}\nSize: {size}\nFee: ${fee}\nPrice: ${price}"
def show_menu(r):
    p = ["peperoni", "cheese", "vegan", "chicken"]
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
def show(a):
    for x in a:
        print(x)
def count(size):
    c1 = 0
    for x in r[0]:
        if x == size:
            return c1
        c1 += 1
def aki(pizzas):
    a = []
    for x,y in pizzas.items():
        a.append(f"{x}: {y}")
    return a
def register(a,pizzas,names,date,time,price,dfee):
    namep = input("Enter your name(REQUIRED): ")
    phonenumb = input("Enter your phone number(optional): ")
    if a == 1:
        ls = []
        v = "" 
        for x in names:
            location = input(f"Enter location for \"{x}\" pizza: ")
            v = v + '\n' + f"Location for \"{x}\" pizza: " + location
            ls.append(location)
        b = "" 
        for x in aki(pizzas):
            b = b + "\n" + x
        payment = input("Cash or cardnum: ")
        print(f"Cheque:\n\tName: \n{namep}\n\tphone_number: \n{phonenumb}\n\tdate: \n{date}\n\ttime: \n{time}\n\tDelivery fee: \n${dfee}\n\tPayment: \n{payment}\n\tLOCATION: {v}\n\tPizzas: {b}\n\tTOTAL PRiCE: ${price}")
    else:
        print(f"Cheque:\n\tName: \n{namep}\n\tphone_number: \n{phonenumb}\n\tdate: \n{date}\n\ttime: \n{time}\n\tPizzas:{str(b)}\n\tTOTAL PRiCE: ${price}")
pizzas = dict()
names = []
total_price = 0
r = read("semester_1\Lesson_35\\archive.csv")
print("Welcome user")
p = 0
while True:
    p +=1
    print("Press 1 to give order")
    print("Press 2 to finish order")
    menu = int(input(""))
    if menu == 1:
        today = datetime.datetime.today()
        date = today.strftime("%Y/%m/%d")
        time = today.strftime("%H:%M")
        typep = int(input("one-in-one/two-in-one/custom: "))
        if typep == 1:
            show_menu(r)
            order = input("Choose pizza: ")
            size = input("What size do you want(S, M, L): ")
            c1 = count(size)
            for x in r:
                if x[0] == order:
                    am = int(input("Enter number of pizzas: "))
                    print(x[c1])
                    total = am * float(x[c1])
                    total_price = total_price + total
                    pizzas[f"Pizza {p}"] = cheque(1,order,0,size,am,0,0,0,0,total)
                    names.append(order)
        elif typep == 2:
            show_menu(r)
            opizza = input("Choose first pizza: ")
            show_menu(r)
            spizza = input("Choose second pizza: ")
            size = input("What size do you want(S, M, L): ")
            size_c = count(size)
            am = int(input("Number of pizzas: "))
            for x in r:
                if x[0] == opizza:
                    oprice = float(x[size_c]) / 2
                if x[0] == spizza:
                    sprice = float(x[size_c]) / 2
            fullprice = (oprice + sprice) * am
            percent = fullprice * 0.1
            total = fullprice + percent
            total_price = total_price + total
            pizzas[f"Pizza {p}"] = cheque(2,opizza,spizza,size,am,0,0,0,percent,total)
            names.append(f"{opizza} and {spizza}")
        elif typep == 3:
            name = input("Choose a name for your pizza: ")
            dough = input("Choose a dough(fluffy,thin): ")
            size = input("Choose size(S,M,L): ")
            amo = int(input("Enter quantity: "))
            tops = []
            mlist = ["Toppings: ","black_olives", "mushrooms", "fresh_basil", "choped_tomatoes", "peppers", "onions", "spinach"]
            while True:
                show(mlist)
                top = input("Choose toppings: ")
                if top == "no":
                    break
                mlist.remove(top)
                tops.append(top)
            show(["Cheese: ", "Mozzarella", "Parmesan", "Ricotta"])
            cheese = input("Choose cheese: ")
            customp = {
                "Pizza" : name,
                "Dough" : dough,
                "Toppings" : tops,
                "Cheese" : cheese
            }
            fl = read("semester_1\Lesson_35\ingr.csv")
            price = 0
            c = 0
            for x in tops:
                for z in fl[0]:
                    if x == z:
                        price = price + float(fl[1][c])
                    c += 1
                c = 0
            perc = price * 0.2
            price = price * am
            total_price = total_price + price + perc
            pizzas[f"Pizza {p}"] = cheque(3,name,0,size,amo,tops,cheese,dough,perc,price)
            names.append(name)
    elif menu == 2:
        print(pizzas)
        td = int(input("takeout-1 or delivery-2: "))
        if td == 1:  
            register(2,pizzas,names,date,time,total_price,0)
            break
        elif td == 2:
            delivery = total_price * 0.15
            total_price = total_price + delivery
            register(1,pizzas,names,date,time,total_price,delivery)
            break
    










