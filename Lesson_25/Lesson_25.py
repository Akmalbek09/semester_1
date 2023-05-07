def my_fun():
    name = "Akmalbek"
    def my_fun_inner():
        surname = "Abdurakhmonov"
        print(name, surname)
    my_fun_inner()
my_fun()


age = 14
def my_fun():
    name = "Akmalbek"
    age = "My age is 13"
    print(age, "It was out of function")
    def my_fun_inner():
        surname = "Abdurakhmonov"
        print(name, surname, age)
    my_fun_inner()
my_fun()

name = "Aki"
def my_work():
    global name
    name = "Akmalbek"
    print(name, "The meaning of kindness")

my_work()
print(name)

















