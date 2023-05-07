b = int(input())
c = int(input())
count1 = 0
count2 = 0
sum1 = 0
sum2 = 0
for x in range(b, c):
    if x % 2:
        print(x, "odd")
        count1 = count1 + 1
        sum1 += x
    else:
        print(x, "even")
        count2 += 1
        sum2 += x
print(count1)
print(count2)
print(sum1)
print(sum2)
