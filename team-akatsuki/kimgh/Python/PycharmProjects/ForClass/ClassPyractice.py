#모든 것은 다 객체다.

a = 'test'
print('type(a) = ', type(a))
print('type(10) = ', type(10))
print('type(True) = ', type(True), '\n\n')
print('='*50)
#매개변수에 self만 있는 생성자를 기본 생성자라고 한다.

class MyClass:
    def __init__(self):
        pass
print('MyClass() =', MyClass(), '\n\n')
print('='*50)


#캡슐화 -> 데이터와 알고리즘을 하나로 묶어 공용 인터페이스만 제공하고, 세부 사항을 감추는 것
#클래스가 있고 그 속성들이 있는데, private한 상태로 지정해 놓는 것,
# __age __name -> 클래스 내부에서만 사용
#임의로 호출할 수 없고, 제한하여 부름. 내장 함수들은 캡슐화된 결과물

#캡슐화한 클래스의 예, get - 함수를 이용해야만 도출 가능


class People1:
    def __init__(self, age=0, name=None):
        self.__age = age
        self.__name = name

    def getAge(self):
        return self.__age

    def getName(self):
        return self.__name

    def setAge(self, age):
        self.__age = age

    def setName(self, name):
        self.__name = name

print("p1 = People1(20,\"Kim\")")
p1 = People1(20,"Kim")
print('p1.getAge() =', p1.getAge())
print('p1.getName() =', p1.getName())
print('='*50)
#상속: 부모 클래스의 메소드를 그대로 이어 받아 사용하려면 자신의 메소드 이름 앞부분에 super().을 붙이고
#매개 변수에서는 self를 빼고 사용해야 함. super()를 사용하는 경우는 부모 클래스와 다른 생성자를 만들 때,
#부모 클래스와 같은 생성자를 만들 때는 필요가 없다.



class People2:
    def __init__(self, age = 0, name = None):
        self.__age = age
        self.__name = name

    def introMe(self):
        print("Name: ", self.__name, "age: ", str(self.__age))

class Teacher(People2):
    def __init__(self, age = 0, name = None, school = None):
        # People2.__init__(self, age, name)
        super().__init__(age, name)
        self.__school = school

    def showSchool(self):
        print("My school: ", self.__school)

#호출되는 모습

print("\np2 = People2(29, \'Lee\')")
print("p2 = People2()")
p2 = People2()
print("p2.introMe()")
p2.introMe()

print("\nt1 = Teacher(48, \'Kim\', \'HighSchool\')\n")
print("t1.introMe()")
t1 = Teacher(48, "Kim", "HighSchool")
t1.introMe()
print("\nt1.showSchool()")
t1.showSchool()

print('='*50)
#인스턴스를 속성으로 사용하기, 큰 클래스의 일부분을 잘라내 별도의 클래스로 사용하는 것

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_read = 0

    def get_car_name(self):
        long_name = str(self.year) + "" + self.make + "" + self.model
        return long_name.title()

class ElectroCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

class Battery:
    def __init__(self, battery_size = 70):
        self.battery_size = battery_size

    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "kWh battery")


print('='*50)

# 다형성(Polymorphism) 동적 방식

class Korean:
    def greeting(self):
        print("안녕하세요")

class American:
    def greeting(self):
        print("Hello")

def sayhello(people):
    people.greeting()

print("Kim = Korean()")
print("James = American()")
Kim = Korean()
James = American()
print("\nsayhello(Kim)")
sayhello(Kim)
print("\nsayhello(James)")
sayhello(James)

print('='*50)


# 클래스를 정의할 때 class ClassName:과 class ClassName(): 의 차이는 없다.
# 특수 메소드
# __new__() 메소드는 객체가 생성될 때 자동으로 호출됨. __init__()는 그 다음
# __str__() 메소드는 객체의 클래스 이름과 객체의 메모리 주소로 구성된 객체에 대한 설명을
# 문자열로 반환한다.

class Me():
    pass
me = Me()
print('print(me)')
print(me)

print('='*50)

# 무슨 예제인지 모르겠다

class People3:
    def __init__(self, age = 0, name = None):
        self.__age = age
        self.__name = name

    def __str__(self):
        return "info -- name : " + self.__name + " // age : " + str(self.__age)
    
print("p3 = People3(29,\"Lee\")")
p3 = People3(29,"Lee")
print(p3)