# 파이썬 함수 실습

# 사칙 연산
def add(a, b):
    # 더하기
    return a + b


def subtract(a, b):
    # 뺴기
    return a - b


def multiply(a, b):
    # 곱하기
    return a * b


def divide(a, b):
    # 나누기
    return a / b


a = 3
b = 5
print("a + b = ", add(a, b))
print("a - b = ", subtract(a, b))
print("a * b = ", multiply(a, b))
print("a / b = ", divide(a, b))


# greeting
# 매개 변수로 이름을 넣으면 "안녕 {이름}?"이라고 출력하는 greeting 함수를 만들어 봅시다.
# {이름}에는 매개 변수로 넣은 문자열이 나와야 합니다.

# formatting : 문자열 안에 변수를 넣을 수 있음
def greeting(name):
    # 인사를 하는 함수
    return f"안녕? {name}"


name = "아름"
print(greeting(name))
print(greeting("다롱이"))


# 화씨 -> 섭씨, 섭씨 -> 화씨
# 화씨를 섭씨로 만드는 공식 : (? - 32) / 1.8
# 섭씨를 화씨로 만드는 공식 : (? * 1.8) + 32
def f_to_c(degree):
    # 화씨를 섭씨로
    return (degree - 32) / 1.8


print("f_to_c : ", f_to_c(32))


def c_to_f(degree):
    # 섭씨를 화씨로
    return (degree * 1.8) + 32


print("c_to_f : ", c_to_f(0))


# 3초 후에 인사를 하는 함수
# 3초라고 고정되어 있는 시간을 매개 변수로 받을 수 있도록 변경
import time


def delay_hello(text, sec):
    time.sleep(sec)
    print(text)


delay_hello("안녕하세요~ 다롱언니입니다!", 0.8)
