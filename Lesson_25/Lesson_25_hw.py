new_money = 0
def cash(price1,bbook,author,price):
    global new_money
    while True:
        print("Available cash:\n1000.0som\n5000.0som\n10000.0som")
        print("Balance: ", new_money,"som")
        money = int(input(f"Enter cash({price1}): "))
        if money == 1000 or money == 5000 or money == 10000 or money == 20000 or money == 50000 or money == 100000:
            if money < price1 or new_money < price1:
                if money == 1000:
                    new_money = new_money + 1000
                elif money == 5000:
                    new_money = new_money + 5000
                elif money == 10000:
                    new_money = new_money + 10000
                elif money == 20000:
                    new_money = new_money + 20000
                elif money == 50000:
                    new_money = new_money + 50000
                elif money == 100000:
                    new_money = new_money + 100000
            if new_money >= price1:
                if new_money == price1:
                    tosh = new_money
                    new_money = new_money - price1
                    return f"Cheque:\n\tBook: {bbook}\n\tAuthor: {author}\n\tPrice: {price}som\nCheque: {tosh}som"
                elif new_money > price1:
                    to_show = new_money
                    new_money = new_money - price1
                    return f"Cheque:\n\tBook: {bbook}\n\tAuthor: {author}\n\tPrice: {price}som\n\tChange: {new_money}\nCheque: {to_show}som"
            elif (money >= price1 and new_money == 0) or (money >= price1 and new_money > 0):
                if money > price1 and new_money == 0:
                    new_money = money - price1
                    return f"Cheque:\n\tBook: {bbook}\n\tAuthor: {author}\n\tPrice: {price}som\n\tChange: {new_money}\nCheque: {money}som"
                elif money == price1 and new_money == 0:
                    return f"Cheque:\nBook: {bbook}\nAuthor: {author}\n\tPrice: {price}som\nCheque: {money}som"
                elif money >= price1 and new_money > 0:
                    new_money = new_money + money
                    new_money = new_money - price1
                    return f"Cheque:\n\tBook: {bbook}\n\tAuthor: {author}\n\tPrice: {price}som\n\tChange: {new_money}\nCheque: {money}som"
        else:
            print("Wrong cash")
def uzcard(price,bbook,author):
    date = int(input("Type your deadline(1 - 10 days): "))
    newd = (date * 100) / 10
    newprice = (price * newd) / 100 
    while True:
        money = float(input(f"Enter your money(${newprice}): "))
        if money == newprice:
            return f"Cheque:\tBook: {bbook}\n\tAuthor: {author}\n\tPrice: ${price}\nCheque: ${newprice}"
def printbook(book_dict):
    for x,y in book_dict:
            print(x+":",y)
def buy(book, booksname, newbook,bookprice, bookauth):
    amount = int(input("Enter the amount: "))
    counter3 = 0
    if book in booksname:
        for x in booksname:
            if x == book:
                price = bookprice[counter3]
                auth = bookauth[counter3]
                price1 = price * amount
                pay = input("Enter the paying mehtod(cash/uzcard): ")
                if pay == "cash":
                    print(cash(price1, book,auth,price))
                elif pay == "uzcard":
                    print(uzcard(price1, book, auth))
                newbook.append(book)
            counter3 += 1
def submit(backbook, booksname, booksprice, booksauth, newbook): 
    counter = 0
    if backbook in newbook:
        for x in booksname:
            if x == backbook:
                price = booksprice[counter]
                newauthor = booksauth[counter]
                date = int(input("Type your read-book-deadline(1 - 10 days): "))
                newd = (date * 100) / 10
                price1 = (price * newd) / 100
                payment = input("Enter the payment(cash/uzcard): ")
                if payment == "cash":
                    print(cash(price1,backbook,newauthor, price))
                elif payment == "uzcard":
                    print(uzcard(price1,backbook,newauthor))
                newbook.remove(backbook)
            counter += 1 
book_dict = {
    "Name" : ["Atomic habits", "Mindset", "Rich dad and Poor dad", "Good to Great", "Cashflow Quadrant"],
    "Author" : ["James Clear", "Carol S. Dweck", "Robert T. Kiyosaki", "Jim Collins", "Robert T. Kiyosaki"],
    "Price" : [60000.0, 50000.0, 55000.0, 57000.0, 52000.0]
}
newbook = []
ident = input("Enter your identity(user/admin): ")
if ident == "user":
    user_dict = {
        "User1" : "1111",
        "User2" : "2222",
        "User3" : "3333",
        "User4" : "4444"
    }
    username = input("Enter your username: ")
    for x in user_dict.keys():
        if x == username: 
            pasw = input("Enter your password: ")
            if pasw == user_dict[x]:
                print("Welcome", x)
                while True:
                    print("\tPress 1 to buy a book")
                    print("\tPress 2 to borrow a book")
                    print("\tPress 3 to submit a book")
                    print("\tPress 4 to review an author")
                    print("\tPress 5 to review a book")
                    print("\tPress 6 to quit")
                    m = int(input())
                    if m == 1:
                        printbook(book_dict.items())
                        book = input("Enter the book: ")
                        buy(book,book_dict["Name"],newbook,book_dict["Price"], book_dict["Author"])
                    elif m == 2:
                        printbook(book_dict.items())
                        rentbk = input("Enter the book: ")
                        for x in book_dict["Name"]:
                            if x == rentbk:
                                newbook.append(x)
                    elif m == 3:
                        print("Your book-storage:",newbook)
                        backbook = input("Enter the submitting book: ")
                        quest = input(f"Did you like the book {backbook}?: ")
                        if quest == "yes":
                            quest2 = input("Do you want to buy it?: ")
                            if quest2 == "yes":
                                buy(backbook, book_dict["Name"],newbook,book_dict["Price"], book_dict["Author"])
                            elif quest2 == "no":
                                submit(backbook, book_dict["Name"], book_dict["Price"], book_dict["Author"], newbook)
                    elif m == 4:
                        author = input("Type the author: ")
                        ath = []
                        counter = 0
                        if author in book_dict["Author"]:
                            for x in book_dict["Author"]:
                                if x == author:
                                    x = book_dict["Name"][counter]
                                    ath.append(x)
                                counter += 1
                            print(f"Author: {author}\nBook: {ath}")
                    elif m == 5:
                        count = 0
                        printbook(book_dict.items())
                        bk = input("Enter the book to review: ")
                        if bk in book_dict["Name"]:
                            for x in book_dict["Name"]:
                                if x == bk:
                                    author = book_dict["Author"][count]
                                    price = book_dict["Price"][count]
                                    newprice = (10 * price) / 100
                                    print(f"Review:\tAuthor: {author}\n\tBook: {x}\n\tPrice(per day): ${newprice}")
                                    qus = input(f"Are you interested in reading this book {bk}?: ")
                                    if qus == "yes":
                                        q = input("Do you want to buy or borrow the book?: ")
                                        if q == "buy":
                                            buy(bk, book_dict["Name"],newbook,book_dict["Price"], book_dict["Author"])
                                        elif q == "borrow":
                                            printbook(book_dict.items())
                                            newbook.append(bk)
                                    else:
                                        pass
                                count += 1

        
                        
                                




















































