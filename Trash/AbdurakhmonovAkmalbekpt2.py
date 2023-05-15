import csv
def splitter(z):
    newlist = []
    other = []
    counter = 0
    for x in z:
        if x == "/":
            newrow = z[counter+1:]
            newlist.append(z[0:counter])
            lastvaluable = z[counter+1:]
            counter = -1
            z = newrow
        counter += 1
    newlist.append(lastvaluable)
    return newlist
with open("Python Akmalbek\semester_1\work_1.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file)
    listcsv = []
    lists = []
    counter2 = 0
    for x in csv_reader:
        listcsv.append(x)
    for v in listcsv:
        for z in v:
            row = splitter(z)
            lists.append(row)
csv_file.close()
with open("Python Akmalbek\semester_1\work_1.csv", "w", newline="")as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerows(lists)
def sort_function(my_list):
    aki_list = []
    while my_list:
        min = my_list[0]
        for x in my_list:
            if x < min:
                min = x
        aki_list.append(min)
        my_list.remove(min)
    return aki_list
listnum = [1,23,45,29,36,96]
sorted = sort_function(listnum)
print(sorted)
if len(sorted) % 2 == 0:
    lenlist = int(len(sorted) / 2)
    median = (sorted[lenlist] + sorted[lenlist-1]) / 2
    print(median)
else:
    lenlist = int(len(sorted) / 2)
    print(sorted[lenlist])