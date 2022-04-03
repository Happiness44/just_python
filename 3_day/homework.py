# 어떤 숫자를 넘기면 제곱을 리턴하는 함수 square
def square(num):
    return num**2


print(square(4))
print(square(5.5))


# 밑변과 높이를 넣으면 삼각형의 넓이를 구해주는 함수
def area(width, height):
    return width * height / 2


print(area(3, 5))
print(area(4, 8))


# 1달러 환율이 1120원이라 가정하고 원을 넣으면 달러로 바꾼 뒤 출력해주는 함수
def won_to_dollars(won):
    return round((won / 1120), 2)


print(won_to_dollars(100))
print(won_to_dollars(1120))


# 주문 정보(음료 이름, 사이즈, 아이스 여부, 수량)를 넣으면 주문 정보를 출력해주는 함수 order(name, size, is_ice, amount)
# order은 결과 값으로 받은 정보를 그대로 리턴해야 함
def order(name, size, is_ice, amount):
    print(f"[주문정보] 음료 이름 : {name}, 사이즈 : {size}, 아이스 여부 : {is_ice}, 수량 : {amount}")
    return name, size, is_ice, amount


order("아메리카노", "tall", "아이스", 3)
print(order("딸기라떼", "small", "핫", 1))
# 리턴을 여러 개 할 경우 -> tuple 타입
print(type(order("딸기라떼", "small", "핫", 1)))


# 주문 정보(음료 이름, 사이즈, 아이스 여부, 수량)를 받아서 커피를 만드는 make_coffee(name, size, is_ice, amount)
# "주문 하신 {name} {size}사이즈 {is_ice} {amount} 잔 나왔습니다." 가 출력되도록
def make_coffee(name, size, is_ice, amount):
    print(f"주문 하신 {name} {size} 사이즈 {is_ice} {amount}잔 나왔습니다.")


make_coffee("유자차", "tall", "핫", "2")
make_coffee("바닐라 라떼", "small", "아이스", "1")
