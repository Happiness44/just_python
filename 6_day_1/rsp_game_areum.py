# 미니 프로젝트 - 아름의 풀이 버전
# 가위 바위 보 게임을 만들고, player1을 사용자가 직접 입력할 수 있게 해봅시다.
# r은 바위, s는 가위, p는 보를 의미합니다.
# 컴퓨터는 랜덤을 사용하여 r, s, p를 내게 됩니다.
# for loop를 사용해서 10판을 컴퓨터와 하고 전적(승, 무, 패)를 계산하여 넣어봅시다.
# r, s, p 대신 exit를 입력하면 도중에 게임을 포기할 수 있도록 해봅시다.
import random


def rsp_game(rsp):
    computer = random.choice(["r", "s", "p"])

    if rsp == computer:
        print(f"나는 {rsp}, 컴퓨터는 {computer}, 무승부")
        return 0
    elif rsp == "r" and computer == "s":
        print(f"나는 {rsp}, 컴퓨터는 {computer}, 나의 승리")
        return 1
    elif rsp == "s" and computer == "p":
        print(f"나는 {rsp}, 컴퓨터는 {computer}, 나의 승리")
        return 1
    elif rsp == "p" and computer == "r":
        print(f"나는 {rsp}, 컴퓨터는 {computer}, 나의 승리")
        return 1
    else:
        print(f"나는 {rsp}, 컴퓨터는 {computer}, 컴퓨터의 승리")
        return 2


def game():
    total = 0
    win = 0
    lose = 0
    draw = 0

    for n in range(10):
        command = input("종료는 exit\n")
        if command == "exit":
            break
        else:
            result = rsp_game(command)
            total += 1
            if result == 1:
                win += 1
            elif result == 2:
                lose += 1
            elif result == 0:
                draw += 1
    print(f"총 횟수 : {total}, 승리 : {win}, 패배 : {lose}, 무승부 : {draw}")


game()
