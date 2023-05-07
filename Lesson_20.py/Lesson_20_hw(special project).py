from list_functions import*
class korzinkauser:
    def __init__(self,user):
        self.user = user
    def regsignus(self):
            while True
a = input("Who are you(user/admin/superadmin): ")
if a == "user":
    user = {
        "User1" : "paswuser1",
        "User2" : "paswuser2",
        "User3" : "paswuser3",
        "User4" : "paswuser4"
    
    
    
    
    
     }
    entuser = input("Enter your username: ")
    entpasw = input("Enter your password: ")
    if entuser in user.keys():
        if entpasw in user.values():
            user = korzinkauser(user)
        else:
            print("No such passwor")
    else:
        print("No such user found")




        #     
        #     else:
        #         print("Wrong user")
        # elif a == "admin":
        #     if b in admin.values() and c in admin.values():
        #         print("Welcome, admin!")
        #         purchase_dict = {
        #         "Products" : ["apple", "banana", "cherry"],
        #         "Prices" : [2.5, 3, 3.5]
        #         }
        #         print(purchase_dict)
        #         while True:
        #             print("\tPress 1 to make a change")
        #             print("\tPress 2 to quit")
        #             change = int(input())
        #             if change == 1:
        #                 print("\tPress 1 to add a product")
        #                 print("\tPress 2 to remove a product")
        #                 menu = int(input())
        #                 if menu == 1:
        #                     pr = input("Type your new product: ")
        #                     pri = int(input("Type the new price: "))
        #                     purchase_dict["Prices"].append(pri)
        #                     purchase_dict["Products"].append(pr)
        #                     print(purchase_dict)
        #                 if menu == 2:
        #                     rem = input("Type your removing product: ")
        #                     if rem in purchase_dict["Products"]:
        #                         counter = 0
        #                         counter2 = 0
        #                         products = list(purchase_dict["Products"])
        #                         for x in products:
        #                             price = list(purchase_dict["Prices"])
        #                             if x == rem:
        #                                 real_price = price[counter]
        #                                 price.remove(real_price)
        #                                 products.remove(x)
        #                                 purchase_dict["Prices"] = price
        #                                 purchase_dict['Products'] = products
        #                                 print(purchase_dict)
        #                             counter += 1
        #                             counter2 += 1
        #                     else:
        #                         print("We don't have this, Perhaps you might add it?")
                    
        #             elif change == 2:
        #                 break
        #     else:
        #         print("Wrong admin, Perhaps user?")
        # elif a == "superadmin":
        #     if b in superadmin.values() and c in superadmin.values():
        #         while True:
        #             print("Press 1 to make a change in the system")
        #             print("Press 2 to quit")
        #             menu = int(input())
        #             if menu == 1:
        #                 ch = input("Whom do you want to change(user/admin): ")
        #                 change = input("Choose the action(remove/add): ")
        #                 if change == "remove" and ch == "user":
        #                     print(user)
        #                     lp = input("What do you want to do")
        #             elif menu == 2:
        #                 break


        

















