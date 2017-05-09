class SportsMan(object):
    """This is the parent class, from which other classes inherit """
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


class Player(SportsMan):
    """This is a child class which inherits from SportsMan"""
    pass