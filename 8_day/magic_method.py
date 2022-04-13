# 던더 메서드를 사용한 클래스 상속
class Phone:
    gen = 1

    def __init__(self, name, maker):
        self.name = name
        self.maker = maker

    def __str__(self):
        return f"세대 : {self.gen}, 기종 : {self.name}, 메이커 : {self.maker}"

    def call(self, number):
        print(f"전화걸기 {number}")

    def send_message(self, number, msg):
        print(f"{number}로 [{msg}] 문자를 보냅니다.")


my_phone = Phone("택택이", "모로롤라")
print(my_phone)
my_phone.call(112)
my_phone.send_message(7979, "안녕 다롱아")
print("-" * 50)


class FeaturePhone(Phone):
    gen = 2

    def play_game(self):
        print("게임시작")

    def calendar(self):
        print("캘린더를 시작합니다.")

    def mobile_web(self):
        print("모바일 웹을 실행합니다.")


# Phone의 __init__를 사용
my_featurephone = FeaturePhone("초코", "엘엘지")
# Phone의 __str__ 출력됨
print(my_featurephone)
my_featurephone.call(114)
my_featurephone.send_message(7979, "다롱아 언니 폰 바꿨어!")
my_featurephone.play_game()
my_featurephone.calendar()
my_featurephone.mobile_web()
print("-" * 50)


class SmartPhone(FeaturePhone):
    gen = 3
    apps = ["브라우저", "캘린더", "지도", "앱스토어", "연락처"]

    # 오버 라이딩 : 상위 클래스의 메서드를 덮어쓰는 것
    def play_game(self):
        print("앱스토어에서 게임을 설치해주세요.")

    def calendar(self):
        print("캘린더 앱을 실행합니다.")

    def mobile_web(self):
        print("브라우저를 실행합니다.")

    def install_app(self, app_name):
        if app_name not in self.apps:
            print(f"{app_name}을 설치합니다.")
            self.apps.append(app_name)
        else:
            print(f"{app_name}앱이 이미 설치되어 있습니다.")

    def uninstall_app(self, app_name):
        print(f"{app_name}을 삭제합니다.")
        self.apps.remove(app_name)

    def show_apps(self):
        print("*" * 30)
        for app in self.apps:
            print(app)
        print("*" * 30)

    def __str__(self):
        return super().__str__() + f"\n설치된 앱들 {self.apps}"


my_smartphone = SmartPhone("아이뻐", "사과시럽")
print(my_smartphone)
# my_smartphone.play_game()
# my_smartphone.install_app("메신저")
# my_smartphone.show_apps()
# my_smartphone.install_app("메신저")
# my_smartphone.show_apps()
# my_smartphone.uninstall_app("메신저")
# my_smartphone.show_apps()
# my_smartphone.uninstall_app("브라우저")
# my_smartphone.show_apps()
