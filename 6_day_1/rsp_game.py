# 미니 프로젝트 - 강의 버전
# 가위 바위 보 게임을 만들고, player1을 사용자가 직접 입력할 수 있게 해봅시다.
# r은 바위, s는 가위, p는 보를 의미합니다.
# 컴퓨터는 랜덤을 사용하여 r, s, p를 내게 됩니다.
# for loop를 사용해서 10판을 컴퓨터와 하고 전적(승, 무, 패)를 계산하여 넣어봅시다.
# r, s, p 대신 exit를 입력하면 도중에 게임을 포기할 수 있도록 해봅시다.
import random


def rsp(p1, p2):
    if p1 == p2:
        print(f"p1 : {p1} vs p2 : {p2} draw")
        return 0
    elif (
        (p1 == "r" and p2 == "s")
        or (p1 == "s" and p2 == "p")
        or (p1 == "p" and p2 == "r")
    ):
        # p1 승리
        print(f"p1 : {p1} vs p2 : {p2} p1 win")
        return 1
    else:
        # p2 승리
        print(f"p1 : {p1} vs p2 : {p2} p2 win")
        return 2


def rsp_game():
    rsp_list = ["r", "s", "p"]
    win = 0
    lose = 0
    draw = 0

    for x in range(10):
        user = input("[바위] r, [가위] s, [보] p, [종료] exit : ")
        if user == "exit":
            break

        computer = random.choice(rsp_list)
        if user not in rsp_list:
            lose += 1
            continue
        result = rsp(user, computer)
        if result == 1:
            win += 1
        elif result == 2:
            lose += 1
        elif result == 0:
            draw += 1

    print(f"win : {win}, lose : {lose}, draw : {draw}")


rsp_game()
