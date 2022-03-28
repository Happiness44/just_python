# 조건문 연습하기 6
# 1. 1에서 13 사이의 랜덤한 수를 리턴해주는 random_num() 함수를 만듭니다.
# 2. random_num()을 사용해서 p1, p2에 각각 랜덤한 수를 할당합니다.
# 3. 두 수를 비교해서 큰 수가 나온 플레이어가 이기는 게임을 만들어 봅시다.
# 4. 무승부인 경우 재시합을 하게 됩니다. 재시합에도 무승부인 경우에만 무승부로 표시를 해줍니다.
import random


def random_num():
    return random.randrange(1, 14)


player1 = random_num()
player2 = random_num()


def random_battle(p1, p2):
    sequence = 0

    if p1 > p2:
        print(f"p1 :{p1}, p2 :{p2} -> p1 승리")
    elif p1 < p2:
        print(f"p1 :{p1}, p2 :{p2} -> p2 승리")
    else:
        if sequence == 0:
            print(f"p1 :{p1}, p2 :{p2} -> 재시합")
            random_battle(random_num(), random_num())
            sequence += 1
        else:
            print(f"p1 :{p1}, p2 :{p2} -> 무승부")


random_battle(player1, player2)
