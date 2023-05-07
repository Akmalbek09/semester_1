my_list = [45,34,41,75,16]
chet_list = []
ne_chet_list = []
for x in my_list:
    a = x / 2
    result = str(a)
    if len(result) == 3:
        ne_chet_list.append(result)
    else:
        chet_list.append(result)
print(ne_chet_list)
print(chet_list)


