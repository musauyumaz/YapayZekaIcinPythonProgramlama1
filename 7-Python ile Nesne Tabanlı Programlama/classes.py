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
