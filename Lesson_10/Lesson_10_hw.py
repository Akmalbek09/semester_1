listnum = [1,2,3,4,5]
s = int(input("Type your salary($): "))
print("Menu")
for num in listnum:
    print("Press", num)
for loop in range(1,5):
    a = int(input())
    if a == 1:
        y = s * 12
        print("Annual salary: ", y,"$")
    elif a == 2:
        if s > 300:
            t = s * 12 / 100
            print("Tax bill: ", t, "$")
        elif s < 300:
            t = s * 10 / 100 
            print("Tax bill: ", t, "$")
    elif a == 3:
        h = int(input("Type your daily working-hours: "))
        m = h * 26
        if m > 234:
            bonus = m * 2
            print("We are giving you a bonus of ",bonus," for extra working-hours")
        elif m < 234:
            f = m / 2
            print("We fine you ",f,"$"," for missing working-hours")
    elif a == 4:
        z = int(input("Type your working-months per year: "))
        month = s * z
        print("Your salary($): ",month,"$ in ",z, " months" )
    elif a == 5:
        print(s * 11000,"sum")
    end = input("Are you done?: ")
    if end == "yes":
        break
    elif end == "no":
        print(num)
        continue


