# 랜덤한 숫자 출력하기
# 1000에서 20000 사이의 숫자 랜덤하게 출력하기
import random


num = random.randrange(1000, 20001)
print(num)


# 조건문 연습하기 2
# age 변수를 주고 19세 미만이면 "19세 미만은 시청하실 수 없습니다."를 출력해보자
age = random.randrange(1, 100)

print(age)
if age < 19:
    print("19세 미만은 시청하실 수 없습니다.")


# 조건문 연습하기 3
# 시험에서 95점 이상이면 A+, 90점 이상은 A, 85점 이상은 B+ ...
# 시험 점수를 넣으면 성적이 나오도록 코드를 작성해보자
score = random.randrange(55, 101)

if score >= 95:
    print(score, "A+")
elif score >= 90:
    print(score, "A")
elif score >= 85:
    print(score, "B+")
elif score >= 80:
    print(score, "B")
elif score >= 75:
    print(score, "C+")
elif score >= 70:
    print(score, "C")
elif score >= 65:
    print(score, "D+")
elif score >= 60:
    print(score, "D")
else:
    print(score, "F")


# 조건문 연습하기 4
# salary 변수가 있다.(단위는 만원, salary = 1200 : 1200 만원)
# salary : ~ 1200의 경우, 세금으로 6%를 뗀다.
# salary : 1201 ~ 4600의 경우, 세금으로 15%를 뗀다.
# salary : 4601 ~ 8800의 경우, 세금으로 24%를 뗀다.
# salary : 8801 ~ 15000의 경우, 세금으로 35%를 뗀다.
# salary : 15001 ~ 의 경우, 세금으로 40%를 뗀다.
# 실수령액을 구해보자.

# 1200 1210 1220 ...
salary = random.randrange(1200, 20001, 10)

tax = 0
if salary <= 1200:
    tax = salary * 0.06
elif 1200 < salary <= 4600:
    tax = salary * 0.15
elif 4600 < salary <= 8800:
    tax = salary * 0.24
elif 8800 < salary <= 15000:
    tax = salary * 0.35
else:
    tax = salary * 0.4

print(f"salary : {salary} | tax : {tax}")

real_salary = salary - tax
print(f"salary : {salary} | tax : {tax} | real_salary : {real_salary}")
