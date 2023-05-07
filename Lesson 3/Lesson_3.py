a = 2
b = 3
c = a + b


a = a + 2 
a += 2
b *= 5
c //= 5
print(a,b,c)

Name = "Akmalbek"
Surname = "Akbarovich"
full_name = Name + " " + Surname
# print(full_name)
# \t - tab
info = "\t\tAkmalbek\'s laptop is cool. \nNext -> \ntext"
print(info)
age = 13
formatted_str = f"My name is {Name}"
print(formatted_str)
formatted_str = "My name is {1} , my surname is {0} and my age is at {2}".format(Surname, Name, age)
print(formatted_str)
formatted_str = "My name is %s , my surname is %s and my age is at %d"% (Surname, Name, age)
print(formatted_str)

print(len(formatted_str))
print(formatted_str[0], formatted_str[len(formatted_str)-1])
# # -1
# print(formatted_str[-66])
# print(formatted_str)
# print(formatted_str[4:10]) #4-9
# print(formatted_str[0:10])
# print(formatted_str[0:len(formatted_str)])
print(formatted_str[::-1])
# print(formatted_str[66:-65])
# print(formatted_str[0:20])
# print(formatted_str[:10])
# print(formatted_str[:21:2])
print(formatted_str[::3])
name = input("Введите свое имя: ")
print("Ваше имя: ",(name))
print("Reversed: ",(name[len(name)::-1]))    