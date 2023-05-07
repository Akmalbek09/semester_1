# # 1
# # из заданного текста посчитать сколько слов там есть 

# # text.txt

# # 2
# # задана переменная  
# # u01,Tom,19,student,Tashkent 
# # вытащите каждое значение как новую переменную 
# # ID 
# # Name 
# # AGE
# # Occupation
# # City

# # 3
# # создайте функцию которая конвертирует цифры на слова (УЗБ) 20 - yigirma, 18 - on  sakkiz 

# 4
# user = [1,2,3,4,5,6,7,8,9]
# name = ["Jimena","Duran","Angel","Williams",
#        "Jovan" ,"Compton","Kamren","Valenzuela","Denzel"]



# создайте словарь, 
# где ключ - USER и values все элементы листа user, 
# создайте 
# второй ключ NAME и values все элементы листа name

# ПРИ СОХРАНЕНИИ ДАННЫХ В СЛОВАРЬ ВСЕ ПЕРЕМЕШАТЬ в оббеих ключах


#1
list123 = []
counter = 0
text = "Serquyosh,hur olkam,elga baxt,najot,Sen ozing dostlarga yoldosh,mehribonmehribon!Yashnagay to abad ilmu fan,ijod,Shuhrating porlasin toki bor jahon! "
for x in text:
    if x == "," or x == " " or x == "!":
        counter += 1
print(counter)
#2
count = 0
count2 = 0
id = []
txt = "u01,Tom,19,student,Tashkent"
for x in txt:
    if x == ",":
        for z in txt[count:]:
            if z == ",":
                m = txt[count:count2]
                id.append(m)
            count2 += 1
        min = txt[0:count]
        id.append(min)
    count += 1
print(id)
#3
listnum = []
names2 = ["bir", "ikki", "uch", "tor", "besh", "olti", "yetti", "sakiz", "toqiz"]
listbig = []
listfull = [10,20,30,40,50,60,70,80,90]
names = ["on", "yigirma", "ottiz", "qiriq", "ellik", "oltmish", "yetmish", "sakson", "toqson"]
def forr(list1,num, list2, counter):
    for x in list1:
        if num == x:
            print(list2[counter-1])
        counter += 1
def nums():
    counter = 0
    counter2 = 1
    counter3 = -1
    counter4 = -1
    for x in range(0,10):
        listnum.append(x)
    for z in range(11, 100):
        listbig.append(z)
    num = int(input("Num: "))
    if num in listnum:
        forr(listnum, num, names2, counter)
    elif num in listfull:
        forr(listfull, num, names, counter2)
    elif num in listbig:
        num = str(num)
        for z in listnum:
            if int(num[1]) == z:
                fnum = names2[counter3]
            counter3 += 1
        for g in listnum:
            if int(num[0]) == g:
                snum = names[counter4]
            counter4 += 1
        print(snum+" "+fnum)
nums()
# 4
user = [1,2,3,4,5,6,7,8,9]
name = ["Jimena","Duran","Angel","Williams",
       "Jovan" ,"Compton","Kamren","Valenzuela","Denzel"]
count = 0
mydict = {

}
mydict["user"] = user
mydict["name"] = name
print(mydict)
mydict["name"] = set((name))
print(mydict)
#5
# list used with multiple items and changeable
# Tuple a collection with multiple items which is ordered and unchangeable
# #Dictionary is used to store data and is a collection of changeable non-duplicate items
# Set is used to store multiple items and is unchangeable, but capable of removing and adding items and non-duplicate

















