def menu_func(menu,listnum):
    for x in listnum:
        if x == 1:
            print("\tPrint 2 to register")
        if x == 3:
            print("\tPrint 3 to quit")
def menu_all_function(a,b,name):
    while True:
        m = int(input(""))
        if m == 1:
            new = input(f"Enter your new {name}: ")
            
            print(a)
            break
        elif m == 2:
            newl = input("Enter your login: ")
            newp = input("Enter your password: ")
            b.append(newl)
            b.append(newp)
            print(b)
            break
        elif m == 3:
            break
        break
def check_function(entpassw,passw,entusername,usernamedict):
    