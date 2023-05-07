import csv
import datetime
import random
index = dict(index = 0)
othindex = dict(index = 0)
def atm_balance():
    atm_list = []
    with open("Lesson_33\data_atm.csv", "r")as csv_file:
        read = csv.reader(csv_file)
        for x in read:
            atm_list.append(x)
        big_balance = float(atm_list[len(atm_list)-1][1])
        return big_balance
big_balance = atm_balance()
atm_csv = ["0000", big_balance,"86000000", 0, 0, 0, 0]
# from Funct import *
# for x in menu(3):
#     print(x)
def show_atm():
    with open("Lesson_33\data_atm.csv", "a", newline='')as csv_file:
        read = csv.writer(csv_file)
        read.writerow(atm_csv)
        csv_file.close()
def check_log(a):
    chl = 0
    counter = 0
    with open("Lesson_33\log_data.csv", "r") as csv_file:
        reader = csv.reader(csv_file)
        for x in reader:
            if x[0] == a:
                chl = 1
                index["index"] = counter
                othindex["index"] = counter
            counter += 1
        if chl == 1:
            chl = True
        else:
            chl = False
        csv_file.close()
        return chl
def check_psw(a):
    chl = 0
    with open("Lesson_33\log_data.csv", "r") as csv_file:
        reader = csv.reader(csv_file)
        for x in reader:
            if x[1] == a:
                chl = 1
        if chl == 1:
            chl = True
        else:
            chl = False
        csv_file.close()
        return chl
def restorepasw(a):
    aplist = []
    with open("Lesson_33\log_data.csv", "r") as csv_file:
        reader = csv.reader(csv_file)
        for x in reader:
            aplist.append(x)
    csv_file.close()
    counter = 0
    for z in aplist:
        if z[0] == a:
            t = 3
            att = 0
            while att < 3:
                att += 1
                print(f"Answer the question: {str(z[2])}")
                answer = input("Answer: ")
                question = str(z[3])
                if answer == question:
                    newpasw = input("Enter a new pasword: ")
                    z[1] = newpasw
                    aplist[counter] = z
                    csv_file.close()
                    return aplist
                else:
                    t -=1
                    print(f"Wrong answer, attempts left: {t}")
        counter += 1
def register(pasw, quest, ans, name):
    def randomizer(typec):
        num1 = str(random.randint(0,9))
        num2 = str(random.randint(0,9))
        num3 = str(random.randint(0,9))
        num4 = str(random.randint(0,9))
        cardnum = num1+num2+num3+num4
        return typec+cardnum
    print("UZCARD:\n\tCARD_NO(e.g): 2009 xxxx\n\tEXPIRY_DATE: 5 years\n\tSERVICE_CHARGE: 1%\n\tPRICE: 2.9$")
    print("VISA:\n\tCARD_NO(e.g): 1987 xxxx\n\tEXPIRY_DATE: 4 years\n\tSERVICE_CHARGE: 2.5%\n\tPRICE: 1.9$")
    print("MASTERCARD:\n\tCARD_NO(e.g): 1983 xxxx\n\tEXPIRY_DATE: 4 years\n\tSERVICE_CHARGE: 3%\n\tPRICE: 1.4$")
    cardtype = input("Enter card type: ")
    typec = 0
    if cardtype == "uzcard":
        typec = "2009"
    if cardtype == "visa":
        typec = "1987"
    if cardtype == "mastercard":
        typec = "1983"
    while True:
        card_num = randomizer(typec)
        if check_log(card_num) == False:
            break
    aplist = [card_num,pasw,quest,ans]
    with open("Lesson_33\log_data.csv", "a", newline='') as csv_file:
        write = csv.writer(csv_file)
        write.writerow(aplist)
        csv_file.close()
    aplist2 = [card_num, name, "0", "0", "0"]
    with open("Lesson_33\data_store.csv", "a", newline='') as csv_file:
        write = csv.writer(csv_file)
        write.writerow(aplist2)
        csv_file.close()
def transfer(tax, card, balance, othbalance, card_no):
    print(f"The card is {card}")
    balances = []
    while True:
        print(f"Balance: {balance}")
        money = float(input("Enter money for transfer: "))
        if check_log(card_no) == False:
            service_charge = money * tax
            if money + service_charge <= balance:
                balance = balance - money - service_charge
                othbalance = othbalance + money - service_charge
                atm_csv[6] = atm_csv[6] + service_charge
                atm_csv[5] = money - service_charge
                atm_csv[1] = big_balance - money - service_charge
                balances.append(balance)
                balances.append(othbalance)
                print(f"Successfully transferred, your balance: {balance}")
                return balances
            else:
                print(print("The money is exceeding your balance, Try again!"))
        else:
            if money <= balance:
                balance = balance - money
                othbalance = othbalance + money
                atm_csv[5] = atm_csv[5] + money
                balances.append(balance)
                balances.append(othbalance)
                print(f"Successfully transferred, your balance: {balance}")
                return balances
            else:
                print(print("The money is exceeding your balance, Try again!"))
def pay(card, balance, othbalance):
    if card[0:4] == "2009":
        balances = transfer(0.01, "uzcard", balance, othbalance, card)
    elif card[0:4] == "1987":
        balances = transfer(0.025, "visa", balance, othbalance, card)
    elif card[0:4] == "1983":
        balances = transfer(0.03, "mastercard", balance, othbalance, card)
    return balances
def payment(bonus, balance):
    money = float(input("Enter money: "))
    bonus = money * bonus
    balances = balance - money + bonus
    return balances
def bills(money, chl, card_no):
    dollars = [card_no,0,0,0,0,0,00,00]
    divide1 = [100, 50, 20, 5, 1]
    if chl == 1:
        dollars[6] = money
    elif chl == 0:
        dollars[7] = money
    counter = 0
    counter2 = 1
    while True:
        if money == 0:
            with open("Lesson_33\dollars.csv", "a", newline='') as csv_file:
                write = csv.writer(csv_file)
                write.writerow(dollars)
                csv_file.close()
                return dollars
        else:
            newmoney = str(money / divide1[counter])
            dollars[counter2] = newmoney[0]
            money = money % divide1[counter]
            counter += 1
            counter2 += 1
def show_info(k):
    newlist = []
    with open(k, "r") as csv_file:
        read = csv.reader(csv_file)
        for x in read:
            newlist.append(x)
        csv_file.close()
        return newlist
def sum(a, k, data_list):
    sum = 0
    for x in data_list:
        if x[a] == k:
            continue
        sum = sum + float(x[a])
def aki(a, k, data_list):
    sum = 0
    for x in data_list:
        if x[a] == k:
            continue
        sum = sum + int(x[a])
    return sum
ident = input("User/Admin: ")
if ident == "user":
    while True:
        print("Press 1 to sign in")
        print("Press 2 to sign up")
        print("Press 3 to restore password")
        print("Press 4 to quit")
        menu = int(input(""))
        if menu == 1:
            attempt = 0
            tries = 4
            ch = 0
            while attempt < 3:
                attempt += 1
                print("LOGIN PAGE")
                login = input("Enter your cardnum: ")
                chlogin = check_log(login)
                if chlogin == True:
                    pasw = input("Enter your password: ")
                    chpasw = check_psw(pasw)
                    if chpasw == True:
                        data_list = []
                        with open("Lesson_33\data_store.csv", "r") as csv_file:
                            reader = csv.reader(csv_file)
                            for x in reader:
                                data_list.append(x)
                        print(f"Welcome user")
                        atm_csv[2] = login
                        today = datetime.datetime.today()
                        todays = today.strftime("%Y/%m/%d")
                        atm_csv[0] = todays
                        counters = []
                        balance = float(data_list[index["index"]][4])
                        counters.append(index["index"])
                        while True:
                            print("Press 1 to show BALANCE")
                            print("Press 2 to deposit money")
                            print("Press 3 to transfer money")
                            print("Press 4 for payment")
                            print("Press 5 to withdraw money")
                            print("Press 6 to quit")
                            menu = int(input(""))
                            if menu == 1:
                                print("Your INFO:")
                                print(f"\tName: {data_list[index['index']][1]}\n\tCard number: {data_list[index['index']][0]}\n\tBalance: ${balance}")
                            elif menu == 2:
                                print(f"Balance: ${balance}")
                                deposit = int(input("Enter deposit money: "))
                                bills(deposit,0,login)
                                balance = deposit + balance 
                                big_balance = big_balance + deposit
                                atm_csv[4] = atm_csv[4] + deposit
                                atm_csv[1] = big_balance + deposit
                            elif menu == 3:
                                ch = 1
                                card = input("Enter card number(8 digits required): ")
                                check_log(card)
                                othbalance = float(data_list[othindex["index"]][4])
                                counters.append(othindex["index"])
                                balances = pay(card, balance, othbalance)
                                balance = balances[0]
                                othbalance = balances[1]
                            elif menu == 4:
                                print("Payment page")
                                print("Press 1 for ucell")
                                print("Press 2 for tax")
                                print("Press 3 for communal tax")
                                print("Press 4 for charity")
                                menu = int(input(""))
                                if menu == 1:
                                    balance = payment(0.01, balance)
                                if menu == 1:
                                    balance = payment(0.015, balance)
                                if menu == 1:
                                    balance = payment(0.012, balance)
                                if menu == 1:
                                    balance = payment(0, balance)
                                    print("Your future dream: $1.000.000.000")
                            elif menu == 5:
                                while True:
                                    print(f"Balance: ${balance}")
                                    cash = int(input("Enter money for withdrawal: "))
                                    service_charge = cash * 0.05
                                    if cash + service_charge <= balance:
                                        bills(cash, 1, login)
                                        balance = balance - cash - service_charge
                                        atm_csv[6] = atm_csv[6] + service_charge
                                        atm_csv[3] = cash - service_charge
                                        atm_csv[1] = big_balance - cash - service_charge
                                        print(f"Successfully withdrawn, balance: ${balance}")
                                        break
                                    else:
                                        print("Unsufficient amount of money, Try again!")
                            elif menu == 6:
                                if ch == 0:
                                    data_list[counters[0]][4] = balance
                                elif ch == 1:
                                    data_list[counters[0]][4] = balance
                                    data_list[counters[1]][4] = othbalance
                                csv_file.close()
                                with open("Lesson_33\data_store.csv", "w", newline='')as csv_file:
                                    write = csv.writer(csv_file)
                                    write.writerows(data_list)
                                show_atm()
                                break
                    elif chpasw == False:
                        tries -=1  
                        print(f"Wrong password, attempts: {tries}")
                elif chlogin == False:
                    tries -=1  
                    print(f"Wrong cardnum, attempts: {tries}")
            else:
                print("Sorry, no such user exists")
        elif menu == 2:
            print("REGISTERATION PAGE")
            while True:
                entname = input("Enter your name: ")
                entpas = input("Enter new password: ")
                if len(entpas) >= 8:
                    entques = input("Enter question for recovery: ")
                    entans = input("Enter answer of the question: ")
                    register(entpas, entques, entans, entname)
                    break
        elif menu == 3:
            print("RESTORE PASSWORD")
            login = input("Enter your cardnum: ")
            if check_log(login) == True:
                newlist = restorepasw(login)
            print(newlist)
            with open("Lesson_33\log_data.csv", "w", newline='')as csv_file:
                writer = csv.writer(csv_file)
                writer.writerows(newlist)
        elif menu == 4:
            break
elif ident == "admin":
    print("Welcome admin")
    while True:
        print("Press 1 to show data")
        print("Press 2 to show bills")
        print("Press 3 to quit")
        menu = int(input(""))
        data_list = show_info("Lesson_33\data_atm.csv")
        if menu == 1:
            print("Balance of ATM:", data_list[len(data_list)-1][1])
            print("NO of customers:", len(data_list)-2)
            print("Withdrawn money:", sum(3, "withdrawal_money", data_list))
            print("Deposit money:", sum(4, "deposit_money", data_list))
            print("Service_charge:", sum(6, "service_charge", data_list))
        elif menu == 2:
            dollars = show_info("Lesson_33\dollars.csv")
            deposits = []
            withs = []
            counter = 0 
            for x in dollars:
                if x[0] == "card_no":
                    continue
                if int(x[6]) == 0 and int(x[7]) > 0:
                    deposits.append(x)
                else:
                    withs.append(x)
            print(f"Deposits:\n\t100$: {aki(1, 'card_no', deposits)}\n\t50$: {aki(2, 'card_no', deposits)}\n\t20$: {aki(3, 'card_no', deposits)}\n\t5$: {aki(4, 'card_no', deposits)}\n\t1$: {aki(5, 'card_no', deposits)}")
            print(f"Withdrawals:\n\t100$: {aki(1, 'card_no', withs)}\n\t50$: {aki(2, 'card_no', withs)}\n\t20$: {aki(3, 'card_no', withs)}\n\t5$: {aki(4, 'card_no', withs)}\n\t1$: {aki(5, 'card_no', withs)}")
    