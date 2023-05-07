new_money = 0
def uzcard(price,product, am):           
    price1 = price * am
    money = float(input(f"Enter your money({price1}som): "))
    if money == price1:
        taxrate = (price1 * 0.5) / 100
        cheque = price1 + taxrate
        return f"Cheque:\nProduct: {product}\nPrice: {price}som\nAmount: {am}\nTax rate: {taxrate}\n\tCheque: {cheque}som"
def cash(price, product, am):
    global new_money
    price1 = float(price * am)
    while True:
        print("Available cash:\n1000.0som\n5000.0som\n10000.0som")
        print("Balance: ", new_money,"som")
        money = int(input(f"Enter your cash({price1}som): "))
        if money == 1000 or money == 5000 or money == 10000 or money == 20000:
            if new_money == price1:
                return f"Cheque:\nProduct: {product}\nAmount: {am}\nPrice: {price}som\n\tCheque: {new_money}som"
            if money == price1 and new_money == 0:
                return f"Cheque:\nProduct: {product}\nAmount: {am}\nPrice: {price}som\n\tCheque: {money}som"
            elif new_money > price1:
                to_show = new_money
                new_money = new_money - price1
                return f"Cheque:\nProduct: {product}\nAmount: {am}\nPrice: {price}som\nChange: {new_money}\n\tCheque: {to_show}som"
            elif money > price1 and new_money == 0:
                new_money = money - price1
                return f"Cheque:\nProduct: {product}\nAmount: {am}\nPrice: {price}som\nChange: {new_money}\n\tCheque: {money}som"
            elif money >= price1 and new_money > 0:
                new_money = new_money + money
                new_money = new_money - price1
                return f"Cheque:\nProduct: {product}\nAmount: {am}\nPrice: {price}som\nChange: {new_money}\n\tCheque: {money}som"
            if money < price1 or new_money < price1:
                if money == 1000:
                    new_money = new_money + 1000
                elif money == 5000:
                    new_money = new_money + 5000
                elif money == 10000:
                    new_money = new_money + 10000
        else:
            print("Wrong cash")
def addproduct(products, quantities, price, number):
    prad = input("Enter new product: ")
    amm = int(input("Enter amount of product: "))
    price1 = float(input("Enter new price for the new product: "))
    if prad not in products:
        products.append(prad)
        quantities.append(amm)
        price.append(price1)
        newnum = len(number) + 1
        number.append(newnum)
    else:
        print("This product already exists")
def addamount(quantities, nums):
    prod = int(input("Enter the number of product: "))
    for x in nums:
        if x == prod:
            newamm = int(input("Enter new amount of product: "))
            quantities[x-1] = newamm
def remprod(price,quant,prod,num):
    rempr = int(input("Enter your the number of removing product: "))
    nums = num
    for x in num:
        if x == rempr:
            prod.remove(prod[x-1])
            price.remove(price[x-1])
            quant.remove(quant[x-1])
            nums.remove(num[x-1])

my_dict = {
    "Products" : ["coca-cola", "snickers", "bounty", "water"],
    "Numbers" : [1, 2, 3, 4,],
    "Prices" : [6000.0, 7000.0, 10000.0, 2000.0],
    "Quantities" : [3, 1, 5, 10]
}
while True:
    ident = input("Enter your identity(user/admin): ")
    if ident == "user":
        print("Welcome, user!")
        for x, y in my_dict.items():
            print(x+":", y)
        number = int(input("Type your number: "))
        for x in my_dict["Numbers"]:
            if x == number:
                price1 = float(my_dict["Prices"][x-1])
                print(price1)
                name1 = my_dict["Products"][x-1]
                quantity1 = int(my_dict["Quantities"][x-1])
                am = int(input("Type your amount: "))
                if am <= quantity1:
                    quantity1 = quantity1 - am
                    my_dict["Quantities"][x-1] = quantity1
                    pay = input("Enter your payment(cash,uzcard): ")
                    if pay == "uzcard":
                        print(uzcard(price1, name1, am))
                    elif pay == "cash":
                        print(cash(price1, name1, am))
                else:
                    print("There is no more left")
    elif ident == "admin":
        check = {
            "Login" : "adminlog",
            "Password" : "adminpassw"
        }
        entlog = input("Enter your login: ")
        entpassw = input("Enter your password: ")
        if entlog == check["Login"] and entpassw == check["Password"]:
            print("Welcome, admin!")
            while True:
                print("\tPress 1 to show the products")
                print("\tPress 2 to make a changes")
                print("\tPress 3 to quit")
                menu = int(input())
                if menu == 1:
                    for x, y in my_dict.items():
                        print(x+":", y)
                elif menu == 2:
                    pr = list(my_dict["Products"])
                    num = list(my_dict["Numbers"])
                    prices = list(my_dict["Prices"])
                    quant = list(my_dict["Quantities"])
                    print("\tPress 1 to add product")
                    print("\tPress 2 to remove a product")
                    print("\tPress 3 to change amount of product")
                    ch = int(input())
                    for x, y in my_dict.items():
                            print(x+":", y)
                    if ch == 1:
                        addproduct(pr, quant, prices, num) 
                    elif ch == 2:
                        remprod(prices,quant,pr,num)
                    elif ch == 3:
                        addamount(quant,num)
                    my_dict["Products"] = pr
                    my_dict["Numbers"] = num
                    my_dict["Prices"] = prices
                    my_dict["Quantities"] = quant
                elif menu == 3:
                    break                            



