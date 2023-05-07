import csv
# with open("Python Akmalbek\semester_1\Lesson_27\s_data.csv", "r") as csv_file:
#     to_read = csv.reader(csv_file)
#     # print(to_read)
#     countbrazil = 0
#     countusa = 0
#     countitaly = 0
#     for x in to_read:
#         # if x[1] == "Salary":
#         #     continue
#         # if int(x[1]) > 50000:
#         #     print(x)
#         if x[2] == "Brazil":
#             countbrazil += 1
#         elif x[2] == "USA":
#             countusa += 1
#         elif x[2] == "Italy":
#             countitaly += 1
    # print("USA: ",countusa, "Brazil: ", countbrazil, "Italy: ", countitaly)
    # csv_file.close()
# list1 = []
# with open("Python Akmalbek\semester_1\Lesson_27\s_data.csv", "r") as csv_file:
#     to_read = csv.reader(csv_file)
#     for x in to_read:
#         list1.append(x)
#     for g in list1:
        
#             # g[0] == "Akmalbek"
# csv_file.close()
# with open("Python Akmalbek\semester_1\Lesson_27\s_data.csv", "w") as csv_file:
#     to_write = csv.writer(csv_file)
#     to_write.writerow(list1)
# csv_file.close()
def login(newlog, newpasw):
    ch = 0 
    with open("Python Akmalbek\semester_1\Lesson_27\s_data.csv", "r") as csv_file:
        toread = csv.reader(csv_file)
        for x in toread:
            if x[0] ==  newlog and x[1] == newpasw:
                ch = 1
                break
    csv_file.close()
    return ch
while True:
    regsign = input("signup or login or change: ")
    if regsign == "signup":
        login = input("Enter your username: ")
        pasw = input("Enter your password: ")
        c = 0
        with open("Python Akmalbek\semester_1\Lesson_27\s_data.csv", "r") as csv_file:
            toread = csv.reader(csv_file)
            for x in toread:
                if x[0] == login and x[1] == pasw:
                    c = 1
                    break
            if c == 0:
                print("Wrong login, Try again!")
            elif c == 1:
                print("Welcome to the system")
        csv_file.close()
    elif regsign == "login":
        list1 = []
        newlog = input("Enter the username: ")
        newpasw = input("Enter the password: ")
        ch = login(newlog, newpasw)
        if ch == 1:
            print("Username and password already exists, Try again!")
        elif ch == 0:
            with open("Python Akmalbek\semester_1\Lesson_27\s_data.csv", "a", newline='') as csv_file:
                toappend = csv.writer(csv_file)
                list1.append(newlog)
                list1.append(newpasw)
                # for x in list1:
                toappend.writerow()
    elif regsign == "change":
        with open("Python Akmalbek\semester_1\Lesson_27\s_data.csv", "r") as csv_file:
            list1 = []
            read = csv.reader(csv_file)
            toread2 = csv.reader(csv_file)
            entusername = input("Enter your username: ")
            entpasw = input("Enter your password: ")
            for x in read:
                if x[0] == entusername and x[1] == entpasw:
                    change = input("What do you want to change: ")
                    if change == "username":
                        curruser = input("Enter your new username: ")
                        for g in toread2:
                            print(g)
                            list1.append(g)
                        for z in list1:
                            if z[0] == entusername and z[1] == entpasw:
                                z[0] = curruser
                        print(list1)
            csv_file.close()
        with open("Python Akmalbek\semester_1\Lesson_27\s_data.csv", "w") as csv_file:
            write = csv.writer(csv_file)
            write.writerow(list1)



