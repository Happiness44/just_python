# 가장 간단한 클래스
class MyClass:
    pass


# print(MyClass())


class Hello:
    """
    헬로우 클래스
    """
    default_text = "안녕하세요!"

    def __init__(self, name):
        self.name = name

    def hello(self):
        print(self.name, self.default_text)


# 클래스 오브젝트
# print(Hello.default_text)
# print(Hello.__doc__)
# TypeError: hello() missing 1 required positional argument: 'self'
# print(Hello.hello())

# 클래스가 효과가 있으려면 실행을 해줘야 함 => 인스턴스를 생성해줘야 함!
# print(Hello)
# __init__(초기화 함수)이 실행됨
# Hello를 가지고 만든 오브젝트가 인스턴스!
# print(Hello("아름"))


h1 = Hello("다롱")
h2 = Hello("재롱")
h3 = Hello("모찌")


print(h1)
print(h2)
print(h3)

