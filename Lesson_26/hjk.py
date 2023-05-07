signname = "user1/aki/15"

count = 0
count4 = 0

for a in signname:
    if "user1" == a:
        for z in a:
            if z == "/":
                name = a[count+1:len(a)]
                break
            count += 1
        for g in name:
            if g == "/":
                print(f"username: user1\npassword: 0000\nname: {name[0:count4]}\nage: {name[count4+1:len(name)]}")
                break
            count4 += 1