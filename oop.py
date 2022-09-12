#class - definē klasi

class Auto():
    def __init__(self,modelis,krasa):
        self.modelis = modelis
        self.krasa = krasa

bmw = Auto(modelis= 'X5', krasa= 'Sarkana')

print(bmw.modelis)

class Auto():
    def __init__(self,modelis,krasa):
        self.modelis = modelis
        self.krasa = krasa

    def dati(self):
        