# %% dictionary

dictionary = {"ali":32, "veli" : 45, "ayse" : 13}

dictionary["ali"]
type(dictionary["ali"])

# ali veli ayse : keys
# 32,45,13 = values

dictionary.keys()
dictionary.values()

def deneme():
    dictionary = {"ali":32, "veli" : 45, "ayse" : 13}
    return dictionary

dict = deneme()

dict["veli"]