print(isinstance(1, int))


class Person:
    __slots__ = ['hello', 'age', 'name', '__wallet']
    def __init__(self):
        self.hello = '안녕하세요.'
        self.__wallet = 10000

    def greeting(self):
        self.__greeting()

    def __greeting(self):
        print(self.hello)

    def pay(self, amount):
        self.__wallet -= amount


james = Person()
james.greeting()  # 안녕하세요.

james.name = 'maria'
james.pay(3000)


class Annie:
    """애니 클래스 이다."""

    count = 0

    def __init__(self, health, mana, ability_power):
        self.health = health
        self.mana = mana
        self.ability_power = ability_power
        Annie.count += 1

    def tibbers(self):
        """티버 스킬 피해량"""
        damage = self.ability_power * 0.65 + 400
        print('티버: 피해량 ' + str(damage))
        return self.ability_power * 0.65 + 400

    @staticmethod
    def myname():
        print('내 이름은 애니')

    @classmethod
    def print_count(cls):
        print('{0}명 생성되었습니다.'.format(cls.count))

# health, mana, ability_power = map(float, input().split())

# x = Annie(health=health, mana=mana, ability_power=ability_power)
# x.tibbers()

print(Annie.__dict__)
print(Annie.__doc__)
print(Annie.tibbers.__doc__)
Annie.myname()
Annie.print_count()


class Time:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    @staticmethod
    def is_time_valid(time_string):
        s = list(map(int, time_string.split(':')))
        return s[0] <= 24 and s[1] <= 59 and s[2] <=60

    @classmethod
    def from_string(cls, time_string):
        s = time_string.split(':')
        return cls(*s)

time_string = '12:62:43' #input()

if Time.is_time_valid(time_string):
    t = Time.from_string(time_string)
    print(t.hour, t.minute, t.second)
else:
    print('잘못된 시간 형식입니다.')


class Person:
    def __init__(self):
        print('Person')
        self.hello = '안녕'
    def greeting(self):
        print('안녕')

class Student(Person):
    def __init__(self):
        print('Student')
        super().__init__()
        super(Student, self).__init__()
        self.school = '도장'
    def greeting(self):
        super(Student, self).greeting()
        print('한번더 안녕')

print(issubclass(Student, Person))

james = Student()
print(james.school)
print(james.hello)
james.greeting()


class A:
    def greeting(self):
        print('안녕하세요. A입니다.')


class B(A):
    def greeting(self):
        print('안녕하세요. B입니다.')


class C(A):
    def greeting(self):
        print('안녕하세요. C입니다.')


class D(B, C):
    pass


x = D()
x.greeting()  # 안녕하세요. B입니다.
print(D.mro())


from abc import *

class StudentBase(metaclass=ABCMeta):
    @abstractmethod
    def study(self):
        pass

    @abstractmethod
    def go_to_school(self):
        pass

class Student(StudentBase):
    def study(self):
        print('공부하기')
    def go_to_school(self):
        print('학교가기')

james = Student()
james.study()
james.go_to_school()


class Animal:
    def eat(self):
        print('먹다')


class Wing:
    def flap(self):
        print('파닥거리다')


class Bird(Animal, Wing):
    def fly(self):
        print('날다')


b = Bird()
b.eat()
b.flap()
b.fly()
print(issubclass(Bird, Animal))
print(issubclass(Bird, Wing))