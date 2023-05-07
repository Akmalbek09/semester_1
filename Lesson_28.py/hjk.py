import csv
with open("Python Akmalbek\semester_1\Lesson_28.py\eggs.csv", 'a', newline='') as csv_file:
    app = csv.writer(csv_file)
    list1 = [["asdf","asdfg"],["dfghjk","fghjk"]]
    print(list1)
    for x in list1:
        app.writerow(x)