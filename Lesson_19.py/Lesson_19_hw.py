from Functions import*
newlist = []
newlistall = []
login = {"Login1" : 'Abdu1',
        "Login2" :  "Abdu2",
        "Login3" :  "Abdu3",
        "Login4" :  "Abdu4",
        "Login5" :  "Abdu5"
}
passw = {"Password1" : "Akmalbek1",
         "Password2" : "Akmalbek2",
         "Password3" : "Akmalbek3",
         "Password4" : "Akmalbek4",
         "Password5" : "Akmalbek5"
}
entpassw = input("Enter your password: ")
entlogin = input("Enter your login: ")
check_function(entpassw,passw.values(),entlogin,login.values(),newlist,newlistall)










