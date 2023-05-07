purchase_dict = {
                                "Products" : ["apple", "banana", "cherry"],
                                "Prices" : [2.5, 3, 3.5]
                                }
                                product = input("Type your product: ") 
                                quantity = int(input("Type your quantity(kg): "))
                                payment = input("Type your payment(cash,visa,uzcard): ")
                                counter = 0
                                for x in purchase_dict["Products"]:
                                    price = list(purchase_dict["Prices"])
                                    if x == product:
                                        real_price = price[counter]
                                        real_price1 = real_price * quantity
                                        if payment == "uzcard":
                                            payment_function(x,quantity,tax_price_function(0.32,real_price,quantity))
                                            break
                                        elif payment == "visa":
                                            payment_function(x,quantity,tax_price_function(0.32,real_price,quantity))
                                            break
                                        elif payment == "cash":
                                            payment_function(x,quantity,real_price1)