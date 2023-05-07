result = []
x = 0
for a in range(1,4):
    x = x + 1
    print("User №: ", x)
    for trise in range(0,100):
        a = input("Enter your name: ").upper()
        if a.isdigit():
            print("Name must not contain any digit")
        elif not a.isdigit():
            result.append(a)
            break
    for tries2 in range(0,100):
        b = input("Enter your lastname: ").upper()
        if b.isdigit():
            print("Last name must not contain any digit")
        elif not b.isdigit():
            result.append(b)
            break
    if str("VA") in str(b):
       result.append("You are a female")
    elif str("OV") in str(b) or str("EV") in str(b):
        result.append("You are a male")
    for tries3 in range(0,100):
        c = input("Enter your e-mail: ").lower()
        if "@" not in c or "." not in c:
            print("Wrong e-mail, Try again!")
        elif "@" in c and "." in c:
            result.append(c)
            break
        
    for tries4 in range(0,100):
        d = input("Enter your age: ")
        if not d.isdigit():
            print("Age must not conatin letters")
        elif d.isdigit():
            result.append(d)
            break
        
    print("New user?")
    e = input().lower()
    if e == "no":
        break
    elif e == "yes":
        continue
if x == 1:
    print(result[0:5])
elif x == 2:
    print(result[0:5])
    print(result[5:10])
elif x == 3:
    print(result[0:5])
    print(result[5:10])
    print(result[10:15])

    
        



