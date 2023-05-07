import csv
def signup():
    with open("Python Akmalbek\semester_1\Lesson_28.py\s_data.csv", "r") as csv_file:
        reader = csv.reader(csv_file)
        entlog = input("Enter username: ")
        entpasw = input("Enter pasw: ")
        listcheck = []
        for x in reader:
            if x[0] == entlog and x[1] == entpasw:
                listcheck.append(entlog)
                listcheck.append(entpasw)
    csv_file.close()
    return listcheck
def login(newuser, newpasw):
    with open("Python Akmalbek\semester_1\Lesson_28.py\s_data.csv", "r") as csv_file:
        r = csv.reader(csv_file)
        check = 0
        for x in r:
            if x[0] == newuser and x[1] == newpasw:
                check = 1
    csv_file.close()
    return check
menu = input("sign up or login or change: ")
if menu == "signup":
    list1 = signup()
    newlist = []
    with open("Python Akmalbek\semester_1\Lesson_28.py\s_info_data.csv", "r") as csv_file:
        reader = csv.reader(csv_file)
        for x in reader:
            if x[0] == list1[0]:
                print("Welcome to the system!")
                print(x)
    csv_file.close()
elif menu == "login":
    newuser = input("Enter the new username: ")
    newpasw = input("Enter the new password: ")
    ch = login(newuser, newpasw)
    if ch == 1:
        print("Username and password already exists")
    elif ch == 0:
        with open("Python Akmalbek\semester_1\Lesson_28.py\s_data.csv", "a",newline='') as csv_file:
            appender = csv.writer(csv_file)
            appender.writerow([newuser,newpasw])
        csv_file.close()
        with open("Python Akmalbek\semester_1\Lesson_28.py\s_info_data.csv", "a", newline='')as csv_file:
            ap = csv.writer(csv_file)
            salary = input("Enter your salary: ")
            country = input("Enter your country: ")
            ap.writerow([newuser,salary,country])
        csv_file.close()
elif menu == "change":
    list123 = []
    with open("Python Akmalbek\semester_1\Lesson_28.py\s_data.csv", "r") as csv_file:
        reader = csv.reader(csv_file)
        user = input("Enter your user: ")
        pasw = input("Enter your password: ")
        for x in reader:
            list123.append(x)
        change = input("What do you want to change: ")
        if change == "username":
            chuser = input("Enter your new username: ")
            for x in list123:
                if x[0] == user:
                    x[0] = chuser
    csv_file.close()
    with open("Python Akmalbek\semester_1\Lesson_28.py\s_data.csv", "w",newline='') as csv_file:
        ap = csv.writer(csv_file)
        ap.writerow(" ")
    csv_file.close()
    with open("Python Akmalbek\semester_1\Lesson_28.py\s_data.csv", "w",newline='') as csv_file:
        app = csv.writer(csv_file)
        app.writerows(list123)