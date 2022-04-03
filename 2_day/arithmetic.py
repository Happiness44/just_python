# 산술 연산 : 숫자 계산
# 더하기
phone = 1000_000
delivery_fee = 3000
print("핸드폰 가격 : ", phone + delivery_fee)

# 뺴기
total = phone + delivery_fee
card_sale = 40000
to_pay = total - card_sale
print("지불할 돈 : ", to_pay)

# 곱하기
egg = 150
print("계란 한 판 : ", egg * 30)

# 나누기
em_cnt = 700
total_bonus = 100_000_000
print("인당 보너스 : ", total_bonus // em_cnt)

# 나머지
num = 12345677
print("나머지가 1이면 홀수 : ", num % 2)
num = 12345678
print("나머지가 0이면 짝수 : ", num % 2)

if num % 2 == 0:
    print("나머지가 0이면 짝수 : ", num % 2)
else:
    print("나머지 1이면 홀수 : ", num % 2)

# 거듭 제곱
# 2의 10승 : 1024
print("2의 10승 : ", 2**10)

# 글자의 산술 연산 : string의 산술 연산(+, * 가능)
print("철수야 " + "안녕")
print("글자의" + " " + "산술연산," + " " + "string의" + " " + "산술연산")

print("=" * 30)
print("타이틀")
print("=" * 30)
