x = 10
y = 20

def calc(x, y):
    return x + y, x - y, x * y, x / y

a, s, m, d = calc(x, y)
print('덧셈: {0}, 뺄셈: {1}, 곱셈: {2}, 나눗셈: {3}'.format(a, s, m, d))


def print_numbers(a, b, c):
    print(a)
    print(b)
    print(c)

x = [10, 20, 30]
print_numbers(*x) # unpacking

def print_numbers(*args):
    for arg in args:
        print(arg)

print_numbers(10)
print_numbers(10, 20, 30, 40)
print_numbers(*[1, 2, 3, 4, 5])

def test(a, *args):
    print(a)
    print(args)

test('a', 1, 2, 3, 4, 5)


def personal_info(name, age, address):
    print('이름: ', name)
    print('나이: ', age)
    print('주소: ', address)

x = {'name': '홍길동', 'age': 30, 'address': '서울시 용산구 이촌동'}
personal_info(**x)

def keyword_args(**kwargs):
    for kw, arg in kwargs.items():
        print(kw, ': ', arg, sep='')

y = {'name': '홍길동', 'age': 30, 'address': '서울시 용산구 이촌동'}
keyword_args(**y)

def custom_print(*args, **kwargs):
    print(*args, **kwargs)

custom_print(1, 2, 3, sep=':', end='')


korean, english, mathematics, science = map(int, input().split())

def get_min_max_score(*args):
    return min(args), max(args)

def get_average(**kwargs):
    return sum(kwargs.values()) / len(kwargs)

min_score, max_score = get_min_max_score(korean, english, mathematics, science)
average_score = get_average(korean=korean, english=english,
                            mathematics=mathematics, science=science)
print('낮은 점수: {0:.2f}, 높은 점수: {1:.2f}, 평균 점수: {2:.2f}'
      .format(min_score, max_score, average_score))

min_score, max_score = get_min_max_score(english, science)
average_score = get_average(english=english, science=science)
print('낮은 점수: {0:.2f}, 높은 점수: {1:.2f}, 평균 점수: {2:.2f}'
      .format(min_score, max_score, average_score))