# integer = 10
# string = "messi" "barcelona football team"
# %% 
integer1 = 33
string1 = "messi"

# %% classes

employee1Name = "messi"
employee1Age = 33
employee1Address = "asdasdad"

class Employee(object):
    # attribute = age, address, name
    # behaviour = pass
    pass


employee1 = Employee()
# %% attribute

class Footballer:
    
    football_club = "barcelona"
    age = 30
    
f1 = Footballer()

a = "dene"
print(a)
print(f1)
print(f1.age)
print(f1.football_club)

f1.football_club = "real madrid"
print(f1.football_club)

# %% methods
class Square(object):
    
    edge = 5 # meter
    area = 0
    
    def area1(self):
        self.area = self.edge * self.edge
        print("Area: ",self.area)
    
    
s1 = Square()
print(s1)
print(s1.edge)
print(s1.area1())

s1.edge
s1.area

s1.edge = 7
s1.area1()

# %% methods vs functions
class Emp(object):
    age = 25
    salary = 1000
    
    def ageSalaryRatio(self):
        a = self.age / self.salary
        print("method:", a)
        
    

def ageSalaryRatio(age, salary):
    a = age / salary  
    print("function: ",a)

e1 = Emp()
e1.ageSalaryRatio()

ageSalaryRatio(30, 3000)


a = 2 + 4
a

pi = 3.14
r = 5
area = pi * r ** 2


def findArea(pi, r):
    area = pi * r ** 2
    print(area)
    return area

result1 = findArea(pi, r)

result2 = findArea(pi, 10)

print(result1 + result2)

# %% initializer or constructor

class Animal(object):

    def __init__(self, name, age):
        self.name = name
        self.age  = age
        pass
    
    def getAge(self):
        return self.age
    
    def getName(self):
        return self.name

a1 = Animal("dog", 2)
a1_age = a1.getAge()
print("animal age: ",a1_age)

a2 = Animal("cat", 4)
a3 = Animal("Bird", 6)

a1.getName()
a2.getName()
a3.getName()

# %% calculator project

class Calc(object):
    "calculator"
    def __init__(self, a, b):
        "initialize values"
        self.value1 = a
        self.value2 = b
        
    def add(self):
        "addtion a+b result -> return result"
        return self.value1 + self.value2
    
    def multiply(self):
        """
        multipcliton a*b = result -> return result
        """
        return self.value1 * self.value2
    
    def division(self):
        return self.value1 / self.value2
    
v1 = 5
v2 = 3
c1 = Calc(v1, v2)
add_result = c1.add()
multiply_result = c1.multiply()  

print(f"Add: {add_result}, Multiply: {multiply_result}")  
    
print("Chooose add(1), multiply(2) div(3)")
selection = input("select 1 or 2 or 3: ")
firstValue = input("first value: ")
secondValue = input("second value: ")
c2 = Calc(int(firstValue), int(secondValue))

print(f"Add: {c2.add()}, Multiply: {c2.multiply()}, division: {c2.division()}")  


