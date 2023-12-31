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

# %% Default and Flexible Functions

# default f : cemberin cevre uzunlugu = 2*pi*r

def cember_cevre(r, pi = 3.14):
    """
    input(parametre): r,pi
    output : cemberin cevresi
    """
    output = 2* pi *r
    return output

# flexiable
def hesapla(boy, kilo, *args):
    print(args)
    output = boy+kilo
    return output

# def hesapla(boy, kilo, yas):
#     output = (boy+kilo) * yas
#     return output


# %% Quiz

yas = 10
name = "ali"
soyisim = "veli"

def function_quiz(yas, name, *args, ayakkabiNumarasi = 35):
    print("Cocugun ismi : " , name, " yasi: ", yas, " ayak numarasi: ", ayakkabiNumarasi)
    print(type(name))
    print(float(yas))
    
    output = args[0]*yas
    return output

sonuc = function_quiz(yas, name,soyisim)

print("args[0]*yas: ", sonuc)

# %% Lambda Function
def hesapla(x):
    return x*x

sonuc = hesapla(3)

sonuc2 = lambda x: x*x
print(sonuc2(2))



