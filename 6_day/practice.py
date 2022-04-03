# 반복문 연습
# 주사위를 던져서 랜덤한 숫자가 출력되게 하는 함수 dice()를 만들어 봅시다.
# dice()를 두 번 실행하여 더한 값을 리턴하는 double_dice() 함수를 만들어 보고 값을 출력해 봅시다.
import random


def dice():
    return random.randrange(1, 7)


def double_dice():
    sum = 0
    for n in range(2):
        sum += dice()
    return sum


#print(double_dice())


def multiple_dice(num):
    sum = 0
    for n in range(num):
        sum += dice()
    return sum


#print(multiple_dice(10))


# double_dice()를 player1, player2 에게 각각 실행시켜서 큰 숫자가 나오는 플레이어가 이기는 게임을 만들어 봅시다.
def dice_game():
    player1 = double_dice()
    player2 = double_dice()

    if player1 > player2:
        print(f"player1 : {player1} vs player2 : {player2} | player1 win!")
        return 1
    elif player1 < player2:
        print(f"player1 : {player1} vs player2 : {player2} | player2 win!")
        return 2
    else:
        print(f"player1 : {player1} vs player2 : {player2} | draw!")
        return 0


#dice_game()


# while을 사용하여 주사위 게임을 여러 판 할 수 있게 만들어 봅시다.
# 가상의 플레이어 p1, p2가 게임을 하게 됩니다.
# exit를 입력하면 도중에 게임에서 나가도록 합시다.
# 종료 시에는 지금까지 몇판을 했는 지와 p1 승리 횟수, p2 승리 횟수, 무승부를 화면에 출력해 봅시다.
def dice_game_areum():
    round_num = 0
    p1_win = 0
    p2_win = 0
    draw = 0

    while True:
        if input("exit"):
            break
        else:
            p1 = dice()
            p2 = dice()

            round_num += 1
            if p1 > p2:
                print("p1 승리")
                p1_win += 1
            elif p1 < p2:
                print("p2 승리")
                p2_win += 1
            else:
                print("무승부")
                draw += 1

    print(f"총 횟수 : {round_num}, p1 승리 : {p1_win}, p2 승리 : {p2_win}, 무승부 : {draw}")


#dice_game_areum()


def dice_game2():
    round_num = 0
    p1_win = 0
    p2_win = 0
    draw = 0
    while True:
        round_num += 1
        result = dice_game()

        if result == 1:
            p1_win += 1
        elif result == 2:
            p2_win += 1
        elif result == 0:
            draw += 1

        command = input("종료 exit: ")
        if command == 'exit':
            break
    print(f"round : {round_num}, p1_win : {p1_win}, p2_win : {p2_win}, draw : {draw}")


dice_game2()

