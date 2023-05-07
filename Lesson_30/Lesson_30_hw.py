import csv
import datetime
ident = input("User/Admin: ")
petrol = {
    "A80" : 6000,
    "A92" : 8000,
    "A95" : 10000,
}
if ident == "user":
    count = 0
    now = datetime.datetime.now()
    hour = int(now.strftime("%H"))
    minute = int(now.strftime("%M"))
    name = input("Enter your name: ")
    carname = input("Enter your carname: ")
    petr = input("Enter your petrol: ")
    cardnum = input("Enter your cardnumber: ")
    with open("Python Akmalbek\semester_1\Lesson_30\infodata.csv", "r", newline='') as csv_file:
        write = csv.writer(csv_file)
        read = csv.reader(csv_file)
        list123 = []
        for x in read:
            
        pay = input("Enter your money: ")
        if pay == price:
            write.writerows([])
            after = datetime.datetime.now()
            hour1 = int(after.strftime("%H"))
            minute1 = int(after.strftime("%M"))
                    
                
                
    