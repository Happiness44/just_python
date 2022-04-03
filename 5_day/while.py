# while문 연습 1
def loop1():
    # 무한 반복
    while True:
        print("안녕하세요?!")


# loop1()


# while문 연습 2
# 0부터 9까지 출력하기
def loop2():
    x = 0
    while x < 10:
        print(f"x : {x}")
        x += 1


# loop2()


# while문 연습 3
# if문을 함께 사용하여 사용자의 입력을 받아서 종료시켜봅시다.
# 사용자의 입력은 input() 함수를 사용하면 됩니다.
# exit를 입력받으면 종료되고 아닌 경우는 "안녕? 반가워~"를 출력해봅시다.
def loop3():
    while True:
        command = input("[exit] 종료 : ")
        print("안녕? 반가워~!")
        if command == "exit":
            break


loop3()
