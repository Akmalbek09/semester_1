# dictcars = {
#     "cars" : ["Tesla", "BYD", "BMW", "Mercedenz"]
# }
# for x in dictcars["cars"]:
#     if x == "Tesla":
#         print(x)

    

def sort_function(my_list):
    aki_list = []
    while my_list:
        min = my_list[0]
        for x in my_list:
            if x < min:
                min = x
        aki_list.append(min)
        my_list.remove(min)
    return aki_list
# def chet_function(my_list):
#     aki_list = []
#     while my_list:
#         min = my_list[0]
#         for x in my_list:
#             if x < min:
#                 min = x
#         if min % 2== 0:
#             aki_list.append(min)
#         my_list.remove(min)
#     return aki_list
my_list = [6,1,45,23,67]
print(sort_function(my_list))

# akmalbek_list = []
# for x in my_list:
#     min = my_list[0]
#     counter = 0
#     if min < x:
#         min = my_list[counter]
#         akmalbek_list.append((min))
#     counter += 1
# print(akmalbek_list)













