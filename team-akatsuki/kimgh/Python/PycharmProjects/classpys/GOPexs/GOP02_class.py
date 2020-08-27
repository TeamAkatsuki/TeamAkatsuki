print("=" * 20, "House", "=" * 20)

class House:
    def __init__(self, year, acreages, address, price):
        self.year = year
        self.acreages = acreages
        self.address = address
        self.price = price

    def change_price(self, rate):
        self.price = self.price * rate

    def show_info(self):
        print("""***This house is built in {},
                 acreages : {}
                 address: {}
                 price: {}""".format(self.year, self.acreages, self.address, self.price))

if __name__ == '__main__':
    house_A = House(1999, 100, "Seoul", 1500000000)
    house_A.show_info()
    house_A.change_price(70/100)
    house_A.show_info()
