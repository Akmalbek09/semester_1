import csv
def read(a):
    with open(a,"r") as csv_file:
        r = csv.reader(csv_file)
        return r
def login_reg(login):
    var = 0
