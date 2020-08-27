class Felide:
    type = "Mammal"

    def get_type(self):
        print(self.type)

class Tiger(Felide):
    def bark(self):
        self.bark = print("으르렁")

class Cat(Tiger):
    def bark(self):
        self.bark = print("야오옹")

class Lion(Felide):
    def bark(self):
        self.bark = print("어흥")

print("="*50)
print("호돌이는 호랑이")
호돌이 = Tiger()
호돌이.get_type()
호돌이.bark()

print("="*50)
print("사돌이는 사자")
사돌이 = Lion()
사돌이.get_type()
사돌이.bark()

print("="*50)
print("애옹이는 고양이")
애옹이 = Cat()
애옹이.get_type()
애옹이.bark()
