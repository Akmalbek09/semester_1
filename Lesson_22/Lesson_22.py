# class animals:
#     def __init__(self,name,first_name):
#         self.name = name
#         self.first_name = first_name
#     def show(self):
#         print(self.name)
#         print(self.first_name)
# obj1 = animals("Wolfie","Barisov")
# obj1.show()
# class domestic_animals(animals):
#     def __init__(self, name, first_name,year):
#         animals.__init__(self,name, first_name)
#         self.year = year
#     def show(self):
#         print(self.name)
#         print(self.first_name)
#         print(self.year)
# dom1 = domestic_animals("Dog", "Mahachkov", 2009)
# dom1.show()

class Parents:
    def __init__(self,store,login,password,time):
        self.store = store
        self.login = login
        self.password = password
        self.time = time
    def watch(self):
        if self.login in self.store and self.password in self.store:
            if self.time <12:
                print("You have access to 100 channels")
            else:
                print("You are blocked, it is sleeping time")
class Akmalbek(Parents):
    def __init__(self, store, login, password, time):
        Parents.__init__(login, password)
        self.store = store
        self.time = time
        if self.login in store and self.password in store:
            if self.time < 8:
                print("You have access to 20 channels")
            else:
                print("You are blocked, it is sleeping time")
class Sister(Parents):
    def __init__(self, store, login, password, time):
        Parents.__init__(login, password)
        self.store = store
        self.time = time
        if self.login in store and self.password in store:
            if self.time < 8:
                print("You have access to 20 channels")
            else:
                print("You are blocked, it is sleeping time")
par = Parents()

            



























