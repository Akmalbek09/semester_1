# alllist = []
# list = []
# for x in mytxt:
#     list.append(x)
# alllist.append(list[1])

# mytxt2 = open("Python Akmalbek\semester_1\Lesson_26/data2.txt", "r")
# list1 = []
# for x in mytxt2:
#     list1.append(x)
# alllist.append(list1[0])
# print(alllist)

# mytxt = open("Python Akmalbek\semester_1\Lesson_26/data.txt", "r")
# list1 = []
# for x in mytxt:
#     list1.append(x)
# print(list1)
# no = input("Enter number: ")
# name = input("Enter name: ")
# age = input("Enter age: ")
# pasw = input("Enter password: ")
# if no in list1[0] and name in list1[1] and age in list1[2] and pasw in list1[3]:
#     print("Welcome to system")
def login_pasw_check(entusername):
    signtxt = open("Python Akmalbek\semester_1\Lesson_26\data_log.txt","r")
    count2 = 0
    mylist = []
    for x in signtxt:
        if entusername in x:
            for b in x:
                if b == "/":
                    mylist.append(x[0:count2])
                    mylist.append(x[count2+1:])
                count2 += 1
    signtxt.close()
    return mylist
while True:
    print("Press 1 to login")
    print("Press 2 to signup")
    print("Press 3 to change")
    regsign = int(input())
    if regsign == 1:
        logintxt = open("Python Akmalbek\semester_1\Lesson_26\data_log.txt", "a")
        entusername = input("Enter your username: ")
        entpasw = input("Enter your password: ")
        entname = input("Enter your name: ")
        entage = input("Enter your age: ")
        logintxt.write(f"\n{entusername}/{entpasw}")
        logintxt.close()
        log2txt = open("Python Akmalbek\semester_1\Lesson_26\data_log.txt","r")
        counter = 0
        count = 0
        list1 = []
        for x in log2txt:
            if entusername in x:
                for z in x:
                    if z == "/":
                        newuser = x[0:count]
                        nametxt = open("Python Akmalbek\semester_1\Lesson_26\data_name.txt","a")
                        nametxt.write(f"\n{newuser}/{entname}/{entage}")
                    count += 1
            counter += 1
    elif regsign == 2:
        login = input("Enter your username: ")
        pasword = input("Enter your password: ")
        userpasw = login_pasw_check(login)
        newl = userpasw[0]
        newp = userpasw[1]
        print(newl,newp)
        if pasword == newp and login == newl:
            count = 0
            count2 = 0
            signname = open("Python Akmalbek\semester_1\Lesson_26\data_name.txt", "r")
            for a in signname:
                if userpasw[0] in a:
                    for z in a:
                        if z == "/":
                            name = a[count+1:]
                            break
                        count += 1
                    for g in name:
                        if g == "/":
                            print(f"username: {userpasw[0]}\npassword: {userpasw[1]}\nname: {name[0:count2]}\nage: {name[count2+1:]}")
                            break
                        count2 += 1
    elif regsign == 3:
        curruser = input("Enter the current username: ")
        currpasw = input("Enter the password: ")
        check = login_pasw_check(curruser)
        # if curruser == check[0] and currpasw == check[1]:
        change = input("What would you like to change: ")
        if change == "username":
            newus = input("Enter your new username: ")
            confus = input("Confirm the username: ")
            if newus == confus:
                changetxt = open("Python Akmalbek\semester_1\Lesson_26\data_log.txt", "r")
                for x in changetxt:
                    if newus in x:
                        changetxt = open("Python Akmalbek\semester_1\Lesson_26\data_log.txt", "w")
                        changetxt.write(a[count])
                    count += 1