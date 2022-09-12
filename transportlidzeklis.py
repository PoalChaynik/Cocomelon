class Transportlidzeklis():
    def __init__(self,modelis,krasa,motoraTilpums,atrumkarba):
        self.modelis = modelis
        self.krasa = krasa
        self.motoraTilpums = motoraTilpums
        self.atrumkarba = atrumkarba

    def dati(self):
        print(f'Modelis: {self.modelis}')
        print(f"Krasa: {self.krasa}")
        print(f'Motora tilpums: {self.motoraTilpums}')
        print(f"Atrumkarba: {self.atrumkarba}")

auto = Transportlidzeklis('X5','sarkana','3.0','Automatiska')
auto.dati()