class product:
    def __init__(self, name, price, qty):
        self.__name = name
        self.__price = price
        self.__qty = qty


    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self, value):
        self.__price = value

    @property
    def qty(self):
        return self.__qty
    @qty.setter
    def qty(self, value):
        self.qty = value

    def show_product(self):
        print(f"product name : {self.__name}")
        print(f"price : {self.__price}")
        print(f"quantity : {self.__qty}")

    def change_product(self, price):
            self.price = price

painting_color = product("watercolor", 40000, 12)
painting_color.change_product(38000)
painting_color.show_product()

       