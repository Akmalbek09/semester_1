# def qust_func(a,b,c):
#     countcor = 0
#     countincor = 0
#     for x in a:
#         print(c,b)
#         answer1 = int(input("Your answer: "))
#         if answer1 == 1:
#             print("Correct")
#             countcor += 1
#             break
#         else:
#             print("Incorrect answer")
#             countincor += 1
#             break
#     return countincor
# one_dict = {
#     "Question 1" : "What is your country? \n 1) Uzbekistan; \n 2) Kazakhstan; \n 3)Tajikistan; \n 4)Pakistan",
#     "Question 2" : "What is your age? \n 1) 14; \n 2) 13; \n 3) 10; \n 4)I am not born yet",
#     "Question 3" : "What is your gender? \n 1) Male; \n 2)Female",
#     "Question 4" : "Where do you live? \n 1)Sebzar; \n 2)Nowhere",
#     "Question 5" : "Where do you study? \n 1)Home; \n 2)School"
# }
# for x in one_dict:
#     firques = list(one_dict["Question 1"])
#     qust_func(firques,one_dict["Question 1"],"Queston 1: ")
#     secques = list(one_dict["Question 2"])
#     qust_func(secques,one_dict["Question 2"],"Question 2: ")
#     thirdques = list(one_dict["Question 3"])
#     qust_func(thirdques,one_dict["Question 3"],"Queston 3: ")
#     fourthques = list(one_dict["Question 4"])
#     qust_func(fourthques,one_dict["Question 4"],"Question 4: ")
#     print()
#     break

listall = [
    "Question 1: What is your country? \n 1) Uzbekistan; \n 2) Kazakhstan; \n 3)Tajikistan; \n 4)Pakistan",
    "Question 2: What is your age? \n 1) 14; \n 2) 13; \n 3) 10; \n 4)I am not born yet",
    "Question 3: What is your gender? \n 1) Male; \n 2)Female",
    "Question 4: Where do you live? \n 1)Sebzar; \n 2)Nowhere",
    "Question 5: Where do you study? \n 1)Home; \n 2)School"
]

rightans = [1,2,1,1,2]
counter = 0
for z in listall:
    print(z)
    ans = int(input("Type your answer: "))
    if ans == rightans[counter]:
        print("Correct")
    elif ans != rightans[counter]:
        print("Incorrect")
    counter += 1
            


















































