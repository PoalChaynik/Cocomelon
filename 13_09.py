import datetime as dt

class Rekins():
    def __init__(self, klients, veltijums, izmers, materials):
        self.klients = klients
        self.veltijums = veltijums
        self.izmers = izmers
        self.materials = materials
    
    def aprekins(self):
        darba_samaksa = 15
        PVN = 21
        produkta_cena = len(self.veltijums)*1.2+(self.izmers[0]/100*self.izmers[1]/100*self.izmers[2]/100)/3*self.materials
        PVN_summa = (produkta_cena+darba_samaksa)*PVN/100
        rekina_summa = (produkta_cena+darba_samaksa)+PVN_summa
        return rekina_summa

    def izdrukat(self):
        print(f'Klients: {self.klients}')
        print(f'Veltijums: {self.veltijums}')
        print(f'Izmers: {self.izmers}')
        print(f'Materials: {self.materials}')
        print(f'\n Rekina Summa: {}')

aa = Rekins('Anna','Lai izdodas!',[150,200,150],3.5)

aa.aprekins()