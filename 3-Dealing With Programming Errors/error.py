# %% syntax error

print(9)
# print 9

int(10.0)
# int 10.0

i = 0
while (i < 10):
    print(i)
    i = i + 1
    
# %% exceptions
a = 10
b = "2"
liste = [1,2,3]
print(sum(liste))
# print(a + b)
print(str(a) + b)
k = 10
print(k)
zero = 0
# a = k/zero # hata

if(zero == 0):
    a = 0
else:
    a = k / zero
    
try:
    a = k/zero
except ZeroDivisionError:
    a= 0