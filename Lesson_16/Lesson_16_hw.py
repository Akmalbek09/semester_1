def akmalbek_function(passw):
        for p in passw:
                for syms in symbols:
                    syms = str(syms)
                    if syms in passw:
                        if len(passw)-1 < 8:
                            print("Password status: Medium")
                            break
                        elif len(passw)-1 > 8:
                            print("Password status: Strong")
                            break
                for nums in numbers1:
                    nums = str(nums)
                    if nums in passw:
                        if len(passw)-1 < 8:
                            print("Password status: Medium")
                            break
                        elif len(passw)-1 > 8:
                            print("Password status: Strong")
                            break
                if syms not in passw and nums not in passw:
                    print("Password status: Weak")
                    break
                break

symbols = ["!", "@", "#", "$", "%", "&", ",", ".", "/"]

symbols2 = ["!", "@", "#", "$", "%", "&", ",", ".", "/"]
list1 = []
list2 = []
key = {
    "Password" : list1,
    "Login" : list2
}
i = 0
n = 0
count = 0
numbers1 = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

numbers2 = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
while i < 1:
    i += 1
    pasw = input("Password(more than 8 letters required): ")
    akmalbek_function(pasw)
    dict1 = list(key["Password"])
    dict1.append(pasw)
    login = input("Login: ")
    key["Password"] = dict1
    dict2 = list(key["Login"])
    dict2.append(login)
    key["Login"] = dict2
    print(key)
    while n < 1:
        n += 1
        new = input("New user?")
        if new == "yes":
            pasw = input("Password(more than 8 letters required): ")
            login = input("Login")
            dict1 = list(key["Login"])
            dict2 = list(key["Password"])
            if pasw in dict2 and login in dict1:
                print("Welcome to the system")
                key["Login"] = dict1
                key["Password"] = dict2
                print(key)
                while True:
                    print("""
            Press 1 to change the settings
            Press 2 to quit
                    """)
                    while True:
                        change = input("")
                        if change.isdigit():
                            break
                        elif not change.isdigit():
                            continue
                    if change == "1":
                        ch = input("What do you want to change: ")
                        if ch == "password":
                            dict2 = list(key["Password"])
                            chpasw = input("Enter your new password: ")
                            akmalbek_function(chpasw)
                            dict2.pop(0)
                            dict2.append(chpasw)
                            key["Password"] = dict2
                            print(key)
                        elif ch == "login":
                            dict1 = list(key["Login"])
                            chl = input("Type your new login: ")
                            dict1.pop(0)
                            dict1.append(chl)
                            key["Login"] = dict1
                            print(key)
                    if change == "2":
                        break
        elif new == "no":
            while True:
                    print("""
            Press 1 to change the settings
            Press 2 to quit
                    """)
                    while True:
                        change = input("")
                        if change.isdigit():
                            break
                        elif not change.isdigit():
                            continue
                    if change == "1":
                        ch = input("What do you want to change: ")
                        if ch == "password":
                            chpasw = input("Enter your new password: ")
                            akmalbek_function(chpasw)
                            dict2 = list(key["Password"])
                            dict2.pop(0)
                            dict2.append(chpasw)
                            key["Password"] = dict2
                            print(key)
                        elif ch == "login":
                            dict1 = list(key["Login"])
                            chl = input("Type your new login: ")
                            dict1.pop(0)
                            dict1.append(chl)
                            key["Login"] = dict1
                            print(key)
                    if change == "2":
                        break