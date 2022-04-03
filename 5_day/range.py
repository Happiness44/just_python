# range 연습하기
# 1부터 100까지 range와 for를 사용하여 출력하기
def range1():
    for n in range(100):
        # 0 ~ 99
        if n % 10 == 0:
            print()
        print(n + 1, end=" ")


# range1()


# range를 사용하여 구구단을 출력해주는 함수 gugudan(num)을 만들어 봅시다.
# num이 3이면 구구단 3단을 출력하면 됩니다.
def gugudan(num):
    for n in range(9):
        print(f"{num} * {n + 1} = {num * (n + 1)}")


# gugudan(5)


# for와 range를 두 번 사용해서(중첩) 구구단 1단부터 9단까지 출력하는 함수 gugudan2()를 만들어 봅시다.
def gugudan2():
    # 1~9단 모두 출력
    for n in range(9):
        # n : 0 ~ 8
        print("====================")
        # for m in range(9):
        #     print(f"{n + 1} X {m + 1} = {(n + 1) * (m + 1)}")
        # 함수 재사용으로 복잡한 것을 간단하게!
        gugudan(n + 1)


gugudan2()
