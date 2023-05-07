import datetime
import random
import csv
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
# def finder(txt):
#     counter = 0
#     for x in txt:
#         counter += 1
#     return counter
# num = []
# symbols = [",", ".", "_", "-", "+", "*", "/", "@", "#", "$", "%", "&", "="]
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# for x in range(0,10):
#     x = str(x)
#     num.append(x)
# txt = input("Enter text: ")
# symbsa = []
# lettersa = []
# numsa = []
# for x in txt:
#     if x in symbols:
#         symbsa.append(x)
#     if x in num:
#         numsa.append(x)
#     if x in letters:
#         lettersa.append(x)
# counters = 0
# symbc = finder(symbsa)
# numc = finder(numsa)
# letterc = finder(lettersa)
# print(lettersa)
# print(f"Digits: {numc}{numsa}\nLetters: {letterc}{lettersa}\nSymbols: {symbc}{symbsa}")
# scoreuser = 0
# scoreai = 0
# counter = 0
# winner = 0
# user_name = input("Enter your name: ")
# while True:
#     ai = random.randint(1,3)
#     print(ai)
#     ent = datetime.datetime.now()
#     entm = int(ent.strftime("%M"))
#     ents = int(ent.strftime("%S"))
#     print("1 - rock")
#     print("2 - paper")
#     print("3 - scizzors")
#     user = int(input("Shoot: "))
#     if scoreuser > 200 or scoreai > 200:
#         ext = datetime.datetime.now()
#         extm = int(ext.strftime("%M"))
#         exts = int(ext.strftime("%S"))
#         break
#     else:
#         if user == ai:
#             print("Draw")
#         if user == 1:
#             if ai == 2:
#                 scoreai = scoreai + 100
#             elif ai == 3:
#                 scoreuser = scoreuser + 100
#         if user == 2:
#             if ai == 1:
#                 scoreuser = scoreuser + 100
#             elif ai == 3:
#                 scoreai = scoreai + 100
#         if user == 3:
#             if ai == 1:
#                 scoreai = scoreai + 100
#             elif ai == 2:
#                 scoreuser = scoreuser + 100
#         counter += 1
# if scoreuser > scoreai:
#     print("User wins",scoreuser)
#     winner = "user"
# elif scoreai > scoreuser:
#     print("AI wins",scoreai)
#     winner = "AI"
# intervalm = extm - entm
# intervals = exts - ents
# interval = f"{intervalm}:{intervals}"
# newlist = []
# listuser = []
# listai = []
# with open("Python Akmalbek\semester_1\Lesson_32\date_store.csv", "r") as csv_file:
#     csv_reader = csv.reader(csv_file)
#     for x in csv_reader:
#         newlist.append(x)
#     for z in newlist:
#         if "a" in z[0]:
#             listai.append(x)
#         elif "u" in z[0]:
#             listuser.append(x)
# csv_file.close()
# if winner == "user":
#     newlist.append(["u"+str(len(listuser)+1),user_name, winner, scoreuser, counter, f"{entm}:{ents}", f"{extm}:{exts}", interval])
# elif winner == "AI":
#     newlist.append(["ai"+str(len(listai)+1),user_name, winner, scoreai, counter, f"{entm}:{ents}", f"{extm}:{exts}", interval])
# with open("Python Akmalbek\semester_1\Lesson_32\date_store.csv", "w", newline="") as csv_file:
#     appender = csv.writer(csv_file)
#     appender.writerows(newlist)
# csv_file.close()
newlist2 = []
with open("Python Akmalbek\semester_1\Lesson_32\date_store.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file)
    counter2 = 0
    csvlist = []
    for x in csv_reader:
        csvlist.append(x)
    for x in csvlist:
        if x[4] == "amountplayed":
            continue
        x[4] = int(x[4])
        newlist2.append(x[4])
    newlist3 = newlist2
    sortedlist = sort_function(newlist2)
    sortinglist= []
    index = []
    counter3 = 0
    print(sortedlist)
    while newlist3:
        for z in sortedlist:
            minn = newlist3[0]
            if z == minn:
                counter2 = 0
            counter2+= 1
        index.append(counter2)
        newlist3.remove(minn)
    print(index)
    for z in index:
        sortinglist.append(csvlist[z])
    print(sortinglist)
with open("Python Akmalbek\semester_1\Lesson_32\sorted_data.csv", "w", newline='') as csv_file:
    write = csv.writer(csv_file)
    write.writerows(sortinglist)
csv_file.close()
