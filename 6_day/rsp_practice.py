# 한번 해보기
# 가위바위보 게임을 만들고, player1을 사용자가 직접 입력할 수 있게 해봅시다.
# r은 바위, s는 가위, p는 보를 의미한다고 합시다.
# 컴퓨터는 랜덤을 사용하여 r, s, p를 내게 됩니다.
# 처음 게임을 시작할 때 몇 판을 할 지 입력을 받도록 합시다.

# while 또는 for loop를 사용해서 컴퓨터와 대결을 하고 전적(승, 무, 패)를 계산하여 넣어봅시다.
# r, s, p 대신 exit를 입력하면 도중에 게임을 포기할 수 있도록 해봅시다.
# 힌트 : 문자열을 숫자로 바꾸기 위해서는 int(문자열)을 사용하면 됩니다.
import random


def rsp(player1, player2):
    if player1 == player2:
        print(f"player1 : {player1}, player2 : {player2} => draw!")
        return 0
    elif (
            (player1 == 'r' and player2 == 's') or
            (player1 == 's' and player2 == 'p') or
            (player1 == 'p' and player2 == 'r')
    ):
        # player1 승리!
        print(f"player1 : {player1}, player2 : {player2} => player1 win!")
        return 1
    else:
        # player2 승리!
        print(f"player1 : {player1}, player2 : {player2} => player2 win!")
        return 2


def rsp_game():
    rsp_list = ['r', 's', 'p']
    win = 0
    lose = 0
    draw = 0

    game_num = input("게임 횟수는? ")

    for n in range(int(game_num)):
        user = input("[바위] : r, [가위] : s, [보] : p, [종료] : exit => 나의 선택은? ")
        if user == 'exit':
            break
        if user not in rsp_list:
            lose += 1
            continue
        computer = random.choice(rsp_list)
        result = rsp(user, computer)
        if result == 0:
            draw += 1
        elif result == 1:
            win += 1
        elif result == 2:
            lose += 1
    print(f"승 : {win}, 패 : {lose}, 무 : {draw}")


rsp_game()

