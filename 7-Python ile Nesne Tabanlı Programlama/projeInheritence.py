class Website:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def loginInfo(self):
        print(self.name + " " + self.surname)


class Website1(Website):

    def __init__(self, name, surname, ids):
        Website.__init__(self, name, surname)
        self.ids = ids

    def login(self):
        print(self.name + " " + self.surname + " " + self.ids)


class Website2(Website):

    def __init__(self, name, surname, email):
        Website.__init__(self, name, surname)
        self.email = email

    def login(self):
        print(self.name + " " + self.surname + " " + self.email)


p1 = Website("name", "surname")
p1.loginInfo()

p2 = Website1("name", "surname", "123")
p2.login()
p2.loginInfo()
p2.name
p2.surname

p3 = Website2("name", "surname", "email@")
p3.login()
