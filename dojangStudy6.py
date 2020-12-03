import math
import collections


class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y


Point2D = collections.namedtuple('Point2D', ['x', 'y'])    # namedtuple로 점 표현

p1 = Point2D(x=30, y=20)  # 점1
p2 = Point2D(x=60, y=50)  # 점2

print('p1: {} {}'.format(p1.x, p1.y))  # 30 20
print('p2: {} {}'.format(p2.x, p2.y))  # 60 50


a = p2.x - p1.x  # 선 a의 길이
b = p2.y - p1.y  # 선 b의 길이

c = math.sqrt((a * a) + (b * b))  # (a * a) + (b * b)의 제곱근을 구함
print(c)  # 42.42640687119285


class Point2D:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


length = 0.0
p = [Point2D(), Point2D(), Point2D(), Point2D()]
# p[0].x, p[0].y, p[1].x, p[1].y, p[2].x, p[2].y, p[3].x, p[3].y = map(int, input().split())
p[0].x, p[0].y, p[1].x, p[1].y, p[2].x, p[2].y, p[3].x, p[3].y = map(int, '100 100 200 200 300 300 400 400'.split())

for i in range(3):
    a = p[i+1].x - p[i].x  # 선 a의 길이
    b = p[i+1].y - p[i].y  # 선 b의 길이
    length += math.sqrt((a * a) + (b * b))  # (a * a) + (b * b)의 제곱근을 구함

print(length)

try:
    x = 0 #int(input('나눌 숫자를 입력하세요: '))
    y = 10 / x
except ZeroDivisionError:    # 숫자를 0으로 나눠서 에러가 발생했을 때 실행됨
    print('숫자를 0으로 나눌 수 없습니다.')
else:                        # try의 코드에서 예외가 발생하지 않았을 때 실행됨
    print(y)
finally:
    print('실행끝')

try:
    x = 4
    if x % 3 != 0:
        raise Exception('3의 배수가 아닙니다.')
    print(x)
except Exception as e:
    print('예외!', e)


class NotPalindromeError(Exception):
    pass


def palindrome(word):
    if is_palindrome(word):
        print(word)
    else:
        raise NotPalindromeError('회문이 아닙니다.')


def is_palindrome(word):
    if len(word) < 2:
        return True
    if word[0] != word[-1]:
        return False
    return is_palindrome(word[1:-1])


try:
    word = 'levele' #input()
    palindrome(word)
except NotPalindromeError as e:
    print(e)

