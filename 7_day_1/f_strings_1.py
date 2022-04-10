txt1 = "울릉도"
txt2 = "동남쪽"
txt3 = "뱃길따라"
txt4 = "87k"
txt5 = "외로운"
txt6 = "섬하나"
txt7 = "새들의 고향"
print(f"{txt1} {txt2} {txt3} {txt4} {txt5} {txt6} {txt7}")

# expression : 표현식, syntax(statement) : 구문
# 표현식 : 값으로 표현될 수 있는 것, 변수의 값으로 할당할 수 있는 것
# 구문 : 값에 할당할 수 없는 것
answer = 40 + 2


def add(a, b):
    """
    더하기를 하는 함수
    :param1 a:
    :param1 b:
    :return:
    """
    return a + b


# 함수를 실행한 결과가 answer2에 대입되므로 표현식
answer2 = add(41, 1)


# 함수 할당
fn = add


print(f"{42 + 1}")
print(f"{answer}")
print(f"{add(10, 10)}")
print(f"{answer2}")
print(f"{add}")
print(f"{fn}")
print(f"{add.__doc__}")

# 구문 : if, for, while문, 할당 불가
# an = for x in range(10): pass -> 할당 불가

