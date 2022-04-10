"""
포맷 스트링 스펙 format()
[[fill]align][sign][#][0][minimumwidth][,][.precision][type]
콜론(:)뒤에 와야 함

fill : 아무런 문자나 가능
align : <(왼쪽), ^(가운데), >(오른쪽), 정렬
sign : +, -
minimumwidth: 양수
# : 타입이 실수인데 정수인 경우 소수점을 생각하지 않음
0 : 남는 것은 0으로 채우고 오른쪽 정렬(즉, 0> 와 동일)
, : 3자리 마다 콤마 표시
precision " .2는 소수점 2자리까지 표시
type : b(2진수), c(아스키 부호의 번호), d(10진수), e(지수 표기법), E,
       f(소수점), F, g(소수점도 지수표기법으로), G, n(숫자), o(8진수), s(string), x(16진수), X, %(백분율)
"""


def fstring1():
    for x in range(10):
        n = x + 1
        print(f"{n:02} ** {n:02} = {n ** n:$>13%}")


fstring1()


# c : 아스키 부호의 번호, 캐릭터
print(f"{65:c}, {82:c}, {64:c}")


# d : 10진수
print(f"{70:d}")


# s : 문자
print(f"{'string':s}")


class Person:
    # 클래스 초기화 함수, 초기화를 위해 사용
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 사용자가 보는 설명
    def __str__(self):
        return f"이름은 {self.name}이고, 나이는 {self.age}입니다."

    # 개발자가 보는 설명
    def __repr__(self):
        return f"name : {self.name} | age {self.age}"


# 인스턴스 생성을 통해 메모리에 올라감
my = Person("아름", 29)
print(f"{my}")
print(f"{my!r}")


# 멀티 라인
title = "파이썬 그냥 재미로"
use_time = 30
intro_just_python = f"""{title} 강의에서는
파이썬의 기초를 탄탄하게 다져줍니다.
하루에 {use_time:!>3}분만 투자하시면
어느새 나도 파이썬 개발자!"""


print(intro_just_python)


def deco_str(val):
    return f"""{'=' * 30}
{val}
{'=' * 30}
"""


print(deco_str(intro_just_python))


# f-strings를 만드는 방식은 함수를 재활용(format)하는 방식!
# 변수와 변수가 아닌 곳을 분리한 후 format 함수를 사용, +를 통해 합침
# => format spec도 사용 가능
a = "a"
b = "b"
c = 10


print(f"{a} {b} {c}")
# 실행 방법
print("{}".format(a) + " " + "{}".format(b) + " " + "{}".format(c))