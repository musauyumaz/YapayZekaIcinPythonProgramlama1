class BankAccount(object):
    def __init__(self, name, money, address):
        self.name = name
        self.__money = money
        self.address = address
    # get and set
    def getMoney(self):
        return self.__money
    def setMoney(self, amount):
        self.__money = amount
        
    def __increase(self):
        self.__money = self.__money + 500
        
p1 = BankAccount("Messi", 1000, "Barcelona")
p2 = BankAccount("Neymar", 2000, "Paris")

p1.name
#p1.money 

#p2.money = p2.money + p1.money
#p1.money = 0

#p1.money
#p2.money

print("get method:", p1.getMoney())
p1.setMoney(5000)
print("after set method:", p1.getMoney())

# p1.__increase()
# print("after raise:", p1.getMoney())