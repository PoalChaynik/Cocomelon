#-- 1 UZDEVUMS --#

class Ballite():
    def __init__(self,dekoracijas, ciemini, ediens, vel_davanas):
        self.dekoracijas = dekoracijas
        self.ciemini = ciemini
        self.ediens = ediens
        self.velDavanas = vel_davanas

    def pirkumi(self):
        print('\nNepieciešams nopirkt sekojošās dekorācijas:')
        for i in self.dekoracijas:
            print(i)
        print('\nNepieciešams nopirkt sekojošos ēdienus:')
        for i in self.ediens:
            print(i)

    def Davanas(self):
        print('\nVēlamais dāvanu saraksts:')
        for i in self.velDavanas:
            print(i)

dzD = Ballite(["Baloni","Virtene","Salvetes"],["Anna","Pēteris","Zeltīte","Valters"],["Kartupeļi","Gurķi","Burkāni","Kūka","Sula"],["Grāmata","Krājkase","Termokrūze"])
print(dzD.ediens)
dzD.pirkumi()
dzD.Davanas()

#-- 2 UZDEVUMS --#
