print(dir([1, 2, 3].__iter__()))
print([1, 2, 3].__iter__())

it = [1, 2, 3].__iter__()
print(it.__next__())
print(it.__next__())
print(it.__next__())


class Counter:
    def __init__(self, stop):
        self.current = 0
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.stop:
            r = self.current
            self.current += 1
            return r
        else:
            raise StopIteration


for i in Counter(3):
    print(i, end=' ')

print('*'*30)
print('*'*30)

class Counter:
    def __init__(self, stop):
        self.stop = stop

    def __getitem__(self, index):
        if index < self.stop:
            return index
        else:

            raise IndexError


print(Counter(3)[0], Counter(3)[1], Counter(3)[2])

for i in Counter(3):
    print(i, end=' ')

print('*'*30)


def number_generator(stop):
    n = 0  # 숫자는 0부터 시작
    while n < stop:  # 현재 숫자가 반복을 끝낼 숫자보다 작을 때 반복
        yield n  # 현재 숫자를 바깥으로 전달
        n += 1  # 현재 숫자를 증가시킴


for i in number_generator(3):
    print(i)


def upper_generator(x):
    for i in x:
        yield i.upper()  # 함수의 반환값을 바깥으로 전달


fruits = ['apple', 'pear', 'grape', 'pineapple', 'orange']
for i in upper_generator(fruits):
    print(i)


def trace(func):  # 호출할 함수를 매개변수로 받음
    def wrapper():
        print(func.__name__, '함수 시작')  # __name__으로 함수 이름 출력
        func()  # 매개변수로 받은 함수를 호출
        print(func.__name__, '함수 끝')

    return wrapper  # wrapper 함수 반환


@trace  # @데코레이터
def hello():
    print('hello')


@trace  # @데코레이터
def world():
    print('world')


hello()  # 함수를 그대로 호출
world()  # 함수를 그대로 호출


def trace(func):  # 호출할 함수를 매개변수로 받음
    def wrapper(a, b):  # 호출할 함수 add(a, b)의 매개변수와 똑같이 지정
        r = func(a, b)  # func에 매개변수 a, b를 넣어서 호출하고 반환값을 변수에 저장
        print('{0}(a={1}, b={2}) -> {3}'.format(func.__name__, a, b, r))  # 매개변수와 반환값 출력
        return r  # func의 반환값을 반환

    return wrapper  # wrapper 함수 반환


@trace  # @데코레이터
def add(a, b):  # 매개변수는 두 개
    return a + b  # 매개변수 두 개를 더해서 반환


print(add(10, 20))


def trace(func):  # 호출할 함수를 매개변수로 받음
    def wrapper(*args, **kwargs):  # 가변 인수 함수로 만듦
        r = func(*args, **kwargs)  # func에 args, kwargs를 언패킹하여 넣어줌
        print('{0}(args={1}, kwargs={2}) -> {3}'.format(func.__name__, args, kwargs, r))
        # 매개변수와 반환값 출력
        return r  # func의 반환값을 반환

    return wrapper  # wrapper 함수 반환


@trace  # @데코레이터
def get_max(*args):  # 위치 인수를 사용하는 가변 인수 함수
    return max(args)


@trace  # @데코레이터
def get_min(**kwargs):  # 키워드 인수를 사용하는 가변 인수 함수
    return min(kwargs.values())


print(get_max(10, 20))
print(get_min(x=10, y=20, z=30))

import functools


def is_multiple(x):
    def real_decorator(func):
        @functools.wraps(func)  # @functools.wraps에 func를 넣은 뒤 wrapper 함수 위에 지정
        def wrapper(a, b):
            r = func(a, b)
            if r % x == 0:
                print('{0}의 반환값은 {1}의 배수입니다.'.format(func.__name__, x))
            else:
                print('{0}의 반환값은 {1}의 배수가 아닙니다.'.format(func.__name__, x))
            return r

        return wrapper

    return real_decorator


@is_multiple(3)
@is_multiple(7)
def add(a, b):
    return a + b


add(10, 20)

import math
r = float(input())
print(math.pi * r ** 2)