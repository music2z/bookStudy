"""
x = int(input())
for i in range(x):
    for j in range(x*2-1):
        if x - i <= j + 1 <= x + i:
            print('*', end='')
        else:
            print('-', end='')
    print()

a, b = map(int, input().split())
for i in range(a, b+1):
    if i % 35 == 0:
        print('FizzBuzz')
    elif i % 5 == 0:
        print('Fizz')
    elif i % 7 == 0:
        print('Buzz')
    else:
        print(i)
"""
# import turtle as t
# t.shape('turtle')
# t.color('red')
# t.begin_fill()
# n = 6
# for i in range(n):
#     t.forward(100)
#     t.right(360 / n)
# t.end_fill()

# n = 60
# t.speed('fastest')
# for i in range(n):
#     t.circle(120)
#     t.right(360 / n)

# n = 300
# t.speed('fastest')
# for i in range(n):
#     t.forward(i)
#     t.right(91)

# n, line = map(int, input().split())

# import turtle as t
#
# n, line = map(int, input().split())
# t.shape('turtle')
# t.speed('fastest')
# for i in range(n):
#     t.forward(line)
#     t.right((360 / n) * 2)
#     t.forward(line)
#     t.left(360 / n)
#
# t.mainloop()

# x = 10
# y = 20
# a = []
# for i in range(x, y+1):
#     a.append(2 ** i)
#
# del a[1]
# del a[-2]
# print(a)

x = '''
the grown-ups' response, this time, was to advise me to lay aside my drawings of boa constrictors, whether from the inside or the outside, and devote myself instead to geography, history, arithmetic, and grammar. That is why, at the, age of six, I gave up what might have been a magnificent career as a painter. I had been disheartened by the failure of my Drawing Number One and my Drawing Number Two. Grown-ups never understand anything by themselves, and it is tiresome for children to be always and forever explaining things to the.
'''

# x = input()
# ss = x.split()
# count = 0
# for s in ss:
#     s = s.strip(',.')
#     if s == 'the':
#         count += 1
#
# print(count)

# x = '51900;83000;158000;367500;250000;59200;128500;1304000'
#
# x = list(map(int, x.split(';')))
# x.sort(reverse=True)
# for i in x:
#     s = format(i, ',')
#     print(s.rjust(9))
#
# a = [1,2,3,4,5,6,7]
# for index, value in enumerate(a):
#     print(index, value)

keys = 'alpha bravo charlie delta'.split()
values = map(int, '10 20 30 40'.split())

x = dict(zip(keys, values))
x.pop('delta')
x = {k: v for k, v in x.items() if v != 30}

print(x)