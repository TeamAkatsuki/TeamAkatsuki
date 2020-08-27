class Animal:
    def __init__(self):
        self.type = "동물"

    def get_type(self):
        print(self.type)
        return self.type


class Tiger(Animal):
    def __init__(self, name="뽀삐"):
        self.name = name
    def bark(self):
        print("으르렁")


class Lion(Animal):
    def bark(self):
        print("어흥")


class Cat(Tiger):
    def bark(self):
        print("야옹")

class Zoo:
    def __init__(self):
        self.tiger1 = Tiger("대한")
        self.tiger2 = Tiger()
        self.lion1 = Lion()
        self.cat1 = Cat()

class ZooManager(Animal):
    def bark(self):
        print("예?!!")

    def call_tiger(self):
        my_zoo.tiger1.bark()

my_zoo = Zoo()
me = ZooManager()
me.call_tiger()