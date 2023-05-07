def menu_func(menu,listnum):
    for x in listnum:
        if x == 1:
            print(f"\tPrint 1 to restore the {menu}")
        if x == 2:
            print("\tPrint 2 to register")
        if x == 3:
            print("\tPrint 3 to quit")
def menu_all_function(a,b,name):
    while True:
        m = int(input(""))
        if m == 1:
            new = input(f"Enter your new {name}: ")
            a.append(new)
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
def check_function(entpassw,passw,entlogin,login,newlist,newlistall):
    listnum = [1,2,3]
    if entpassw not in passw and entlogin not in login:
        print("Wrong password, Try again!")
        print("Wrong login, Try again!")
        menu_func("password and login",listnum)
        menu_all_function(newlist,newlistall,"password and login")
    else:
        pass
    for x in login:
        if entlogin in login:
            print("Your login is correct")
            newlist.append(entlogin)
            break
        elif entlogin not in login:
            print("Wrong login, Try again!")
            menu_func("login",listnum)
            menu_all_function(newlist,newlistall,"login")
        break
    for z in passw:
        if entpassw in passw:
            print("Your password is correct")
            newlist.append(entpassw)
            break
        elif entpassw not in passw:
            print("Wrong password, Try again!")
            menu_func("password",listnum)
            menu_all_function(newlist,newlistall,"password")
        break