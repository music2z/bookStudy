def factorail(n):
    if n == 1:
        return 1
    return n * factorail(n-1)

print(factorail(5))

def fib(n=0):
    if n == 0 or n == 1:
        return n
    return fib(n-1) + fib(n-2)

print(fib(20))

import sys
print(sys.getrecursionlimit())

plus_tem = lambda x: x + 10
print(plus_tem(1))
print((lambda x: x + 10)(10))

print(list(map(lambda x: x+10, [1, 2, 3])))

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = list(map(lambda x: str(x) if x % 3 == 0 else x, a))
print(b)

def f(x):
    return x > 5 and x < 10

a = [8, 3, 2, 10, 15, 7, 1, 9, 0, 11]
b = list(filter(f, a))
print(b)

b= list(filter(lambda x: x>5 and x<10, a))
print(b)

from functools import reduce
a = [1, 2, 3, 4, 5]
b = reduce(lambda x, y: x+y, a)
print(b)


files = '97.xlsx 98.docx 99.docx 100.xlsx 101.docx 102.docx'.split()

b = list(map(lambda x: x.zfill(len(x) + (3 - x.find('.'))), files))
print(b)

x = 20
def foo():
    global x
    x = 10
    print(x)

foo()
print(x)

print(locals())


def A():
    x = 10
    y = 100

    def B():
        x = 20

        def C():
            nonlocal x
            nonlocal y
            x = x + 30
            y = y + 300
            print(x)
            print(y)
        C()
    B()
A()


def countdown(n):
    a = n + 1
    def minus1():
        nonlocal a
        a = a - 1
        return a
    return minus1


n = 20 #int(input())

c = countdown(n)
for i in range(n):
    print(c(), end=' ')

