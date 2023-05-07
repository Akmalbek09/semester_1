from Functions import*
balance = float(input("Enter balance to the card: "))
history = []
sonhistory = []
sisterhistory = []
sister2history = []
money = Centralcard(balance,history)
while True:
    user = {
        "dad" : "0000",
        "mom" : "1111",
        "son" : "2222",
        "sister1" : "3333",
        "sister2" : "4444"
    }
    entlogin = input("Enter login: ")
    entpasw = input("Enter password: ")
    for x in user:
        if x == entlogin and user[x] == entpasw:
                if x == "dad":
                    print("Assalomu aleykum, Adajon!")
                    dad1 = userdad(balance,history)
                    while True:
                        print("\tPress 1 to show the balance")
                        print("\tPress 2 to deposit money")
                        print("\tPress 3 to withdraw money")
                        print("\tPress 4 to show the history")
                        print("\tPress 5 to quit")
                        m = int(input())
                        if m == 1:
                            print(dad1)
                        elif m == 2:
                            print("Balance: $",dad1.deposit())
                        elif m == 3:
                            print(dad1.withdraw())
                        elif m == 4:
                            print("The history: ",history)
                        elif m == 5:
                            break
                elif x == "mom":
                    print("Assalomu aleykum, Oyijon!")
                    mom1 = usermom(balance,history)
                    while True:
                        print("\tPress 1 to show the balance")
                        print("\tPress 2 to deposit money")
                        print("\tPress 3 to withdraw money")
                        print("\tPress 4 to show the history")
                        print("\tPress 5 to quit")
                        m = int(input())
                        if m == 1:
                            print(mom1)
                        elif m == 2:
                            print("Balance: $",mom1.deposit())
                        elif m == 3:
                            print(mom1.spend())
                        elif m == 4:
                            print("History: ",history)
                        elif m == 5:
                            break
                elif x == "son":
                    print("Assalomu aleykum, Akmalbek!")
                    son1 = userson(balance,history,sonhistory)
                    while True:
                        print("\tPress 1 to withdraw money")
                        print("\tPress 2 to show the history")
                        print("\tPress 3 to quit")
                        m = int(input())
                        if m == 1:
                            print(son1.spend())
                        elif m == 2:
                            print("History: ",sonhistory)
                        elif m == 3:
                            break
                elif x == "sister1":
                    print("Assalomu aleykum, Fotima!")
                    sister1 = usersister(balance,history,sisterhistory)
                    while True:
                        print("\tPress 1 to withdraw money")
                        print("\tPress 2 to show the history")
                        print("\tPress 3 to quit")
                        m = int(input())
                        if m == 1:
                            print(sister1.spend())
                        elif m == 2:
                            print("History: ",sisterhistory)
                        elif m == 3:
                            break
                elif x == "sister2":
                    print("Assalomu aleykum, Zukhra!")
                    sister2 = usersister2(balance,history,sister2history)
                    while True:
                        print("\tPress 1 to withdraw money")
                        print("\tPress 2 to show the history")
                        print("\tPress 3 to quit")
                        m = int(input())
                        if m == 1:
                            print(sister2.spend())
                        elif m == 2:
                            print("History: ",sister2history)
                        elif m == 3:
                            break





            
            

