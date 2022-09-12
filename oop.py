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
        print(f'Modelis ir {self.modelis}, krasa - {self.krasa}')
    
    def krasas_maina(self, jaunaKrasa):
        print(f'\nIepriekseja auto krasa - {self.krasa}')
        print(f'Jauna auto krasa - {jaunaKrasa}')

audi = Auto(modelis='Q6',krasa='Sudraba')

audi.dati()
audi.krasas_maina('Balta')