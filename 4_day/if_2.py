# 가위 바위 보 랜덤하게 출력하기
import random

rsp = random.choice(["가위", "바위", "보"])
print(rsp)


# 조건문 연습하기 5
# 랜덤하게 "가위", "바위", "보"를 리턴해주는 get_rsp() 라는 함수를 만들자.
# get_rsp()를 두 번 호출하여 player1, player2라는 변수에 각각 담자.
# result_rsp(player1, player2) 라는 함수를 만들고, 가위, 바위, 보 대결의 결과를 출력해주자
# 가위는 보에게 이기고, 바위는 가위에게 이기고, 보는 바위에게 이긴다.
# 같은 결과가 나오면 무승부를 출력하자.
def get_rsp():
    return random.choice(["가위", "바위", "보"])


player1 = get_rsp()
player2 = get_rsp()


def result_rsp(p1, p2):
    if p1 == p2:
        print("무승부")
    elif (p1 == "가위" and p2 == "보") or \
         (p1 == "바위" and p2 == "가위") or \
         (p1 == "보" and p2 == "바위"):
        print("player1 승리")
    else:
        print("player2 승리")


print(f"player1 : {player1}, player2 : {player2}")
result_rsp(player1, player2)

