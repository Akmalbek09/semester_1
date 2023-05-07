
# Не изменяемые 
    # int  
    # float 
    # str 
    # bool 
    # tuple 
    # frozenset 
    # bin 
    # complex 
#  
# Изменяемые 
    # list 
    # dict 
    # set 
#  
# Итерируемые - iterable - те переменые, которые хранят одно или более значений    
    # str 
    # list 
    # tuple 
#  
    # set 
    # frozenset 
    # dict 
#  
#  
# Дополнения к переменным: 
    # Decimal 
    # Fraction 

from traceback import print_list


# Методы это такая функция которая принадлежит переменной/обьекту

# Logical operators: ==, !=, <, >, =>, <= 

s = "Behruz"
# random = " 2 , 4 , 5 , 6 , 7" Текст
#порядок   0  1  2  3  4  5 
# numbers = [2, 4, 5, 6, 7, 8]
# print(numbers)
# print(numbers[3])
# print(numbers[0])


# y = 10 
# x = 20
# if x > y:
#     print("Testing work process x < y") #True

# if x < y:
#     print("Testing work process x > y") #False

# if x < y:
#     print("Testing work process x > y") #False
# else:
#     print("x < y")


# x = 10
# y = 10

# if x > y:
#     print("Testing work process")
# elif x < y:
#     rint("x < y")
# else:
#     print("x == y")

passwords = ['Akmalbek', 'Akmalbek1','Akmalbek2' ]
logins = ['Abdurakh', 'Abdurakh1', 'Abdurakh2']
skills = ["IT web-programmer", "IT designer", "IT web-defender"]
login = input("Type yor login here:")
password = input("Type your password here: ")
skill = input("Type your occupation here:")
if password in passwords:
    if login in logins:
        if skill in skills:
            print("We've received your info")
        print("Your login has been succeed!")
    else:print("Please try your login again")
    print("Your password has been succeed!")
else:
    print("Please try your password again")
formatted_1 = f"""
Guest's login: {login}
Guest's password: {password}
Guest's occupation: {skill}
"""
print(formatted_1)












