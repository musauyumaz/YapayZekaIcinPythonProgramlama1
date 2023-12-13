# %% Built int functions

str1 = "deneme"

float1 = 10.6
float(10)
round(float1)

str2 = "1005"
int(str2)

# %% user defined functions
var1 = 20
var2 = 50
output = (((var1 + var2)*50)/100.0) * var1 / var2

#fonksiyon parametresi = input
def benim_ilk_func(a, b):
    """
    bu benim ilk denemem

    parametre:
    
    return:
    """
    output = (((a + b)*50)/100.0) * a / b
    return output

benim_ilk_func(1, 2)
sonuc = benim_ilk_func(var1, var2)

def deneme1(): 
    print("bu benim ikinci denemem")

