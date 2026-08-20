class animal:
    def make_sound(delf):
        print("making sound")
class cat(animal):
    def make_sound(self):
        print("meow meow")
class dog(animal):
    def make_sound(self):
        print("woah woah")

#cat =cat()
#cat.make_sound()
#dog = dog()
#dog.make_sound()

class ATM:
    def __init__(self):
       pass
    def widtdraw(self):
        print("widthdrawing money")
class card(ATM):
    def widtdraw(self):
        print("withdrawing money from card")
class QRscan (ATM):
    def widtdraw(self):
        print("widtdrawing money from qr code")

#card = card()
#card.widtdraw()

#qr = QRscan()
#qr.widtdraw()

class internet:
    def __init__(self, name, speed, price):
        self.name = name
        self.speed = speed
        self.price = price
    def show_name(self):
        print(f"internet's provider: {self.name}")

class smart(internet):
    def show_name(self):
        print(f"********** smart - internet's provider (ISP) **********")
        print(f"internet's provider: {self.name}")
        print(f"internet's provider: {self.speed}")
        print(f"internet's provider: {self.price}")  

class cellard(internet):
    def show_name(self):
        print(f"********** cellard - internet's provider (ISP) **********")
        print(f"internet's provider: {self.name}")
        print(f"internet's provider: {self.speed}")
        print(f"internet's provider: {self.price}")

class metfone(internet):
    def show_name(self):
        print(f"********** metfone - internet's provider (ISP) **********")
        print(f"internet's provider: {self.name}")
        print(f"internet's provider: {self.speed}")
        print(f"internet's provider: {self.price}") 

Smart = smart("smart", "2GB", "11$") 
Cellard = cellard("cellard", "3GB", "13$")
Metfone = metfone("metfone", "150MB", "1$")

ISP = [Smart, Cellard, Metfone]

for isp in ISP:
    isp.show_name()

def usage(ISP):
    ISP.show_name()
usage(Smart)
usage(Cellard)
usage(Metfone)