def tax_price_function(tax,real_price,quantity):
    real_price1 = real_price
    real_price1 = real_price1 * quantity
    tax = (real_price * tax)
    all = '%.2f'%(real_price1 + tax)
    return all

def payment_function(x,quantity,func):
    print(f"--------Cheque--------\nProduct: {x}\nQuantity: {quantity}kg\nTotal: ${func}")

def menu():
    print("Press 1 to sign in")
    print("Press 2 to register")

            
