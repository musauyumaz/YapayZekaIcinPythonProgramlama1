class Calisan:
    def __init__(self,isim,soyisim,maas):
        self.isim = isim
        self.soyisim = soyisim
        self.maas = maas
        self.email = isim+soyisim+"@asd.com"
    
    def giveNameSurname(self):
        return self.isim + " " + self.soyisim
        
isci1 = Calisan("Ali", "Veli", 100)

isci1

isci1.isim

isci1.email

isci1.giveNameSurname()