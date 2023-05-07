import csv
import datetime
newqnt = 0
list123 = []
def delete_prd(list123):
    delet = input("Enter id to delete the product: ")
    count = 0
    for x in list123:
        if x[0] == delet:
            del list123[count]
        count += 1
def change(list123):
    change_prd = input("Enter id to change the product: ")
    for x in list123:
        if x[0] == change_prd:
            prd = input("Enter the new product: ")
            x[1] = prd
def addprd(list123):
    ch = 0
    fruits = []
    drinks = []
    veges = []
    name = input("Enter your product: ")
    for x in list123:
        if "f" in x[0]:
            fruits.append(x)
        if "f" in x[0]:
            drinks.append(x)
        if "v" in x[0]:
            veges.append(x)
        elif x[1] == name:
            ch = 1
    if ch == 0:
        category = input("Enter product type: ")
        exdate = input("Enter expiry date: ")
        qty = input("Enter the quantity: ")
        prc = float(input("Enter the price: "))
        if category[0] == "f":
            id = category[0]+str(len(fruits)+1)
        elif category[0] == "d":
            id = category[0]+str(len(drinks)+1)
        elif category[0] == "v":
            id = category[0]+str(len(veges)+1)
        list123.append([id, name, exdate, qty, prc])
    elif ch == 1:
        print(f"The product {name} already exists")
def expdate(date):
    counter = 0
    counter2 = 0
    for x in date:
        if x == "-":
            day1 =  date[counter+1:]
            break
        counter += 1
    for z in day1:
        if z == "-":
            expday = int(date[0:counter])
            expmonth = int(day1[0:counter2])
            expyear = int(day1[counter2+1:])
            if expyear == year:
                if expmonth > month:
                    print("Not expired")
                elif expmonth == month and expday > day:
                    print("Not expired")
            elif expyear > year:
                print("Not expired")
            else:
                print("Expired")
        counter2 += 1
def pay(qnt,price,product):
    check = 0
    newqnt = qnt
    am = int(input("How much do you want: "))
    if qnt > am:
        check = 1
        newprice = am * price
        newqnt = qnt - am
        print(f"Cheque:\nProduct:\t{product}\nAmount:\t{am}\nPrice:\t${price}\nCheque:\t{newprice}")
    return newqnt
def store_data(lists):
    users = []
    admins = []
    for x in lists:
        if "u" in x[0]:
            users.append(x)
        if "a" in x[0]:
            admins.append(x)
    if ident[0] == "u":
        print(users)
        amu = ident[0] + str(len(users)+1)
        return amu
    if ident[0] == "a":
        print(admins)
        ama = ident[0] + str(len(admins)+1)
        return ama
def date(enterh,enterm,exith,exitm):
    intervalh = exith - enterh
    intervalm = exitm - enterm
    return f"{str(intervalh)}:{str(intervalm)}"
ch = 0
ident = input("Who are you: ")
if ident == "admin":
    ch = 1
    print("Welcome ADMIN")
    entera = datetime.datetime.now()
    hourenta = int(entera.strftime("%H"))
    minutenta = int(entera.strftime("%M"))
    with open("Python Akmalbek\semester_1\Lesson_31\prdct_data.csv", "r", newline='')as csv_file:
        csv_reader = csv.reader(csv_file)
        for x in csv_reader:
            list123.append(x)
        while True:
            menu = input("Enter action: ")
            if menu == "1":
                addprd(list123)
            elif menu == "2":
                delete_prd(list123)
            elif menu == "3":
                change(list123)
            else:
                exita = datetime.datetime.now()
                hourexa = int(exita.strftime("%H"))
                minuteexa = int(exita.strftime("%M"))
                with open("Python Akmalbek\semester_1\Lesson_31\prdct_data.csv", "w", newline='')as csv_file:
                    writer = csv.writer(csv_file)
                    writer.writerows(list123)
                csv_file.close()
                break
    csv_file.close()
elif ident == "user":
    listus = []
    ch = 2
    print("Welcome USER")
    enteru = datetime.datetime.now()
    hourentu = int(enteru.strftime("%H"))
    minutentu = int(enteru.strftime("%M"))
    year = int(enteru.strftime("%y"))
    month = int(enteru.strftime("%m"))
    day = int(enteru.strftime("%d"))
    with open("Python Akmalbek\semester_1\Lesson_31\prdct_data.csv", "r", newline='')as csv_file:
        csv_reader = csv.reader(csv_file)
        for x in csv_reader:
            print(x)
            listus.append(x)
        prd = input("What do you want: ")
        for x in listus:
            if x[1] == prd:
                date = x[2]
                expdate(date)
                price = float(x[4])
                newqnt = pay(int(x[3]), price,x[1])
                x[3] = newqnt
        exitu = datetime.datetime.now()
        hourexu = int(exitu.strftime("%H"))
        minuteexu = int(exitu.strftime("%M"))
    csv_file.close()
    with open("Python Akmalbek\semester_1\Lesson_31\prdct_data.csv", "w", newline='') as csv_file:
        write = csv.writer(csv_file)
        write.writerows(listus)
    csv_file.close()
lists = []
with open("Python Akmalbek\semester_1\Lesson_31\store_data.csv", "r") as csv_file:
    read = csv.reader(csv_file)
    for x in read:
        lists.append(x)
csv_file.close()
with open("Python Akmalbek\semester_1\Lesson_31\store_data.csv", "w", newline='') as csv_file:
    write = csv.writer(csv_file)
    am = store_data(lists)
    if ch == 1:
        enta = f"{str(hourenta)}:{str(minutenta)}"
        exta = f"{str(hourexa)}:{str(minuteexa)}"
        intervala = date(hourenta,minutenta,hourexa,minuteexa)
        datesa = [am,enta,exta,intervala]
        lists.append(datesa)
    elif ch == 2:
        entu = f"{hourentu}:{minutentu}"
        extu = f"{hourexu}:{minuteexu}"
        intervalh = str(hourexu - hourentu)
        intervalm = str(minuteexu - minutentu)
        intervalu = intervalh + ":" + intervalm
        dates = [am,entu,extu,intervalu]
        lists.append(dates)
    write.writerows(lists)
csv_file.close()
