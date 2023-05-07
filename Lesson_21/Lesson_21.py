# class class1:
#     print("My first class")
# print(type(class1))
# print(class1)

# class school:
#     def __init__(self,name,surname,grade):
#         self.name = name
#         self.surname = surname
#         self.grade = grade
# obj1 = school("Akmalbek", "Khusanov", 8)
# print(f"!st clisent name is {obj1.name} \nSurname is {obj1.surname} \nGrade is {obj1.grade}")

# class school:
#     def __init__(self,name,surname,grade):
#         self.name = name
#         self.surname = surname
#         self.grade = grade
#     def __str__(self):
#         return f"{self.name} {self.surname} {self.grade}"
    
# obj1 = school("Akmalbek", "Abdurakhmonov", 8)
# print(obj1)

class ATM_akm:
    def __init__(self,name,age,card_number,money,tax_rate = 0):
        self.name = name
        self.age = age
        self.card_number = card_number
        self.money = money
        self.tax_rate = tax_rate
    def get_cash(self):
        cash = float(input("Type your cash: "))
        self.tax_rate = cash / 100 * 1.5
        self.money = self.money - self.tax_rate - cash
        return self.money
    def deposit_cash(self):
        deposit = float(input("Type your deposit: "))
        self.money = self.money + deposit
        return self.money
    def convert(self):
        USD = 13000
        self.money = self.money * USD
        USD = 11300
        while True:
            transfer_money = float(input("Type the exchanging amount(USD) : "))
            sum_money = transfer_money * USD
            convert_tax = sum_money * 0.06
            if convert_tax + sum_money < self.money:
                print("Successfully converted to USD")
                self.money = self.money - sum_money - convert_tax
                print("Your sum: ",sum_money)
                print("Tax rate 6% = ",convert_tax)
                print("Your balance: ",self.money)
                break
            else:
                print(f"You don't have enougn money\nYour balance: {self.money} + Tax 6%: ", convert_tax)

    def __str__(self):
        return f"Name : {self.name}\nAge : {self.age}\nCard_number : {self.card_number}\nBalance : {self.money}\n Tax rate 3.5%: {self.tax_rate}"
counter = 0
user_dict = {
    "User1" : "paswuser1",
    "User2" : "paswuser2",
    "User3" : "paswuser3",
    "User4" : "paswuser4"
    }
while True:
    entusername = input("Enter your username: ")
    if entusername in user_dict:
        passw = input("Enter your password: ")
        x = user_dict[entusername]
        if passw in x:
            print("Welcome ",entusername)
            in_name = input("Enter your name: ") 
            in_age = input("Type your age: ")
            in_card_number = input("Enter your card number: ") 
            in_money = float(input("Enter your balance(USD): "))
            print(f"----------Welcoome to ATM, {in_name}------------")
            user1 = ATM_akm(in_name, in_age, in_card_number, in_money)
            listnum = [1,2,3,4,5]
            while True:
                for x in listnum:
                    if x == 1:
                        print("Press 1 to see your balance")
                    if x == 2:
                        print("Press 2 to withdraw cash")
                    if x == 3:
                        print("Press 3 to deposit cash")
                    if x == 4:
                        print("Press 4 to convert to UZS")
                    if x == 5:
                        print("Press 5 to quit")
                menu = int(input("Choose action: "))
                if menu == 1:
                    print(user1)
                elif menu == 2:
                    print(f"Your balance: {user1.get_cash()}")
                elif menu == 3:
                    print(f"Your balance: {user1.deposit_cash()}")
                elif menu == 4:
                    user1.convert()
                elif menu == 5:
                    break
        else:
            print("Press 1 to restore the password")
            print("Press 2 to register")
            print("Press 3 to quit")
            m = int(input())
            if m == 1:
                change = input("Enter your new password: ")
                z = list(x)
                z.insert(0,change)
            elif m == 2:
                ch = input("Enter your new username: ")
                chp = input("Enter your new password: ")
                user_dict.update({ch:chp})                
            elif m == 3:
                break


















