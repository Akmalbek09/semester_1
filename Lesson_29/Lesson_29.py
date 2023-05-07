# def sett(input):
list1 = []
for x in range(0,51):
    x = str(x)
    list1.append(x)
sett = set((list1))
newlist = []
counter = 0
for z in sett:
    z = int(z)
    if counter == 20:
        print(newlist)
        score = 0
        for x in newlist:
            print(type(x))
            num = int(input("Number: "))
            if x == num:
                score = score +1
                break
            if x < num:
                score1 = int(num - x)
                score2 = '%.2f' % (score1/10)
                score = score + score2
            if x > num:
                score1 = int(x - num)
                score2 ='%.2f' % (score1/10)
                score = score + score2
            continue
        print(score)
        if score < 10:
            print("lost")
        else:
            money = 100
            for a in range(10,21):
                if score == a:
                    print(f"You win {money}")
                    break
                else:
                    money = money *2
    counter = counter + 1
    newlist.append(z)