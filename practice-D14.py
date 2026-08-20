class product:
    name = "torriden"
    country = "korean"
    type = "serum"
    skin = False

    def show_info(self):
        print(f"product name : {self.name}")
        print(f"from country : {self.country}")
        print(f"type : {self.type}")

skincare = product()
skincare.show_info()

print("**************************************")

class skincare:
    def __init__(self, name, country, type, price):
        self.name = name
        self.country = country
        self.type = type
        self.price = price
    def show_info(self):
        print(f"skincare name: {self.name}")
        print(f"skincare from: {self.country}")
        print(f"skincare type: {self.type}")
        print(f"skincare price: {self.price}")

torriden = skincare("Torriden" , "korean" , "toner" , 44000)      
bioderma = skincare("Bioder", "french", "sunscreen", 80000)


torriden.show_info()
bioderma.show_info()
