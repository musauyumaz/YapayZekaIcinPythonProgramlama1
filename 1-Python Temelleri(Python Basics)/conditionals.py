# %% if else statement
1 == 1
1 == 2
1 != 1
True == True
True == False
1 > 5
5 > 5
1 > 0 and 4 < 5
1 > 0 or 4 < 3

var1 = 10
var2 = 20

if(var1 > var2):
    print("var1 büyüktür var2")
elif(var1 == var2):
    print("var1 var2'ye eşittir")
else:
    print("var1 küçüktür var2")

liste = [1,2,3,4,5]

if 6 in liste :
    print("evet 6 değeri listenin içinde")
else:
    print("hayır")
    
# %% 

def centuryToYear(year):
    yuzyil = (year//100) + 1 if year % 100 != 0 else year // 100
    return yuzyil

print(centuryToYear(200))