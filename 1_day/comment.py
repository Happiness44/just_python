def say_hello():
    # 안녕하세요!를 출력합니다.
    print("[함수] 안녕하세요!")


class Greeter:
    """
    인사에 관련된 처리를 하는 클래스
    say_안녕
    say_hello
    함수를 가지고 있다.
    """

    def __init__(self):
        print("[클래스] 안녕하세요~")


say_hello()
Greeter()
