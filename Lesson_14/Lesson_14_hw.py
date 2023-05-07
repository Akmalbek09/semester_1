passw = input("Your password: ")
symbols = ["!", "@", "#", "$", "%", "&", ",", ".", "/"]
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# letters1 = str(letters)
# symbols1 = str(symbols)
# symbs = []
# for sym in symbols1:
#     sym = str(sym)
numbers = range(0,9)
numbers1 = list(numbers)
# num = []
# for nums in numbers1:
#     nums = str(nums)
counter = 0
for x in passw:
    counter += 1
    for nums in numbers1:
        nums = str(nums)
        if nums in passw:
            print("Password status: Mid")
            break
    for syms in symbols:
        syms = str(syms)
        if syms in passw:
            print("Password status: Weak")
            break
    for letts in letters:
        letts = str(letts)
        if letts in passw and syms in passw and nums in passw:
            print("Strong")
            break
    break
        # passw = input("Your password: ")
    
        