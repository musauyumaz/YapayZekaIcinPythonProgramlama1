# %% loops
# for loop

for each in range(1,11):
    print(each)
    
for each in "ankara istanbul":
    print(each)
    
for each in "ankara istanbul".split():
    print(each)
    
liste = [ 1,4,5,6,8,3,3,4,67]
sum(liste)

count = 0
for each in liste:
    count = count + each
    
print(count)
    

# while loop
i = 0
while i < 4:
    print(i)
    i = i + 1
    
sinir = len(liste)
each = 0
count = 0
while (each < sinir):
    count = count + liste[each]
    each = each + 1