class Calisan:
    
    zamOrani = 1.8
    counter = 0
    def __init__(self,isim,soyisim,maas):
        self.isim = isim
        self.soyisim = soyisim
        self.maas = maas
        self.email = isim+soyisim+"@asd.com"
        
        Calisan.counter = Calisan.counter + 1
    
    def giveNameSurname(self):
        return self.isim + " " + self.soyisim
    
    def zamYap(self):
        self.maas = self.maas + self.maas * self.zamOrani
        
# isci1 = Calisan("Ali", "Veli", 100)
# isci1
# isci1.isim
# isci1.email
# isci1.giveNameSurname()

# %% class variables

calisan1 = Calisan("Ali", "Veli", 100)
print("ilk maas: ", calisan1.maas)
calisan1.zamYap()
print("yeni maas: ", calisan1.maas)

calisan2 = Calisan("Ayse", "Tınmaz", 200)

calisan2.counter