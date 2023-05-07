class Centralcard:
    def __init__(self,centralcard,history):
        self.centralcard = centralcard
        self.history = history
class userdad(Centralcard):
    def __init__(self,centralcard,history):
        Centralcard.__init__(self, centralcard, history)
    def deposit(self):
        deposit = float(input("Enter depositing money: "))
        self.centralcard = self.centralcard + deposit
        self.history.append("Adajon: +$"+str(deposit))
        return self.centralcard
    def withdraw(self):
        spend = float(input("Enter money for withdrawal: "))
        centralcarddad = self.centralcard / 100 * 50
        taxrate = (spend * 0.6) / 100
        if spend + taxrate < centralcarddad:
            self.centralcard = self.centralcard - spend - taxrate
            self.history.append("Adajon: -$"+str(spend+taxrate))
            return f"Money for withdrawal: ${spend}\nAvailable money(50%off): ${centralcarddad}\nTax rate: ${taxrate}\nMain card: ${self.centralcard}"
        else:
            print("Spendings exceed the limit of savings")
    def __str__(self):
        return f"Main card: ${self.centralcard}"
class usermom(userdad):
    def __init__(self, centralcard, history):
        userdad.__init__(self,centralcard, history)
    def spend(self):
        spend = float(input("Enter money for withdrawal: "))
        taxrate = (spend * 0.6) / 100
        if spend + taxrate < self.centralcard:
            self.centralcard = self.centralcard - spend - taxrate
            self.history.append("Oyijon: -$"+str(spend+taxrate))
            return f"Money for withdrawal: ${spend}\nTax rate : ${taxrate}\nMain card: ${self.centralcard}"
        else:
            print("Spendings exceed the limit of savings")
    def __str__(self):
        return userdad.__str__(self)
class userson(userdad):
    def __init__(self, centralcard, history,sonhistory):
        userdad.__init__(self,centralcard, history)
        self.sonhistory = sonhistory
    def spend(self):
        spend = float(input("Enter money for withdrawal: "))
        taxrate = (spend * 0.6) / 100
        if spend + taxrate < 50:
            self.centralcard = self.centralcard - spend - taxrate
            self.sonhistory.append("-$"+str(spend+taxrate))
            self.history.append("Akmalbek: -$"+str(spend+taxrate))
            return f"Money for withdrawal: {spend}\nTax rate: {taxrate}"
        else:
            print("Spendings exceed the limit of savings ")
class usersister(userdad):
    def __init__(self, centralcard, history,sisterhistory):
        userdad.__init__(self,centralcard, history)
        self.sisterhistory = sisterhistory
    def spend(self):
        spend = float(input("Enter money for withdrawal: "))
        taxrate = (spend * 0.6) / 100
        if spend + taxrate < 25:
            self.centralcard = self.centralcard - spend - taxrate
            self.history.append("Fotima: -$"+str(spend + taxrate))
            self.sisterhistory.append("-$"+str(spend+taxrate))
            return f"Money for withdrawal: {spend}\nTax rate: {taxrate}"
class usersister2(usersister):
    def __init__(self, centralcard, history, sister2history):
        usersister.__init__(self,centralcard, history)
        self.sister2history = sister2history
    def spend(self):
        spend = float(input("Enter money for withdrawal: "))
        taxrate = (spend * 0.6) / 100
        if spend + taxrate < 25:
            self.centralcard = self.centralcard - spend - taxrate
            self.history.append("Zukhra: -$"+str(spend + taxrate))
            self.sister2history.append("-$"+str(spend+taxrate))
            return f"Money for withdrawal: {spend}\nTax rate: {taxrate}"