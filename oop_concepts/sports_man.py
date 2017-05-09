class SportsMan(object):
    pay_raise_index = 1.5

    def __init__(self,  fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary

    def fullname(self):
        return self.fname + ' ' + self.lname

    def pay_raise(self):
        self.salary *= self.pay_raise_index
        return self.salary

    