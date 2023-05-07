# import csv
# with open("Python Akmalbek\semester_1\Lesson_30\lessondata.csv", "r") as csv_file:
#     reader = csv.reader(csv_file)
#     counter = 0
#     newlist = []
#     list123 = []
#     for x in reader:
#         if x[0] == "ID":
#             continue
#         newlist.append(x)
#     for z in newlist:
#         c = int(z[3])
#         if c > 27:
#             old = "Old people"
#             z.append(old)
#         elif c < 27:
#             ad = "Adults"
#             z.append(ad)
# csv_file.close()
# with open("Python Akmalbek\semester_1\Lesson_30\lessondata.csv", "w", newline='')as csv_file:
#     write = csv.writer(csv_file)
#     write.writerows(newlist)

import datetime
today = datetime.datetime.now()
hour = int(today.strftime("%H"))
minute = int(today.strftime("%M"))
print(hour, minute)
# td = list(today)
# print(td)



















