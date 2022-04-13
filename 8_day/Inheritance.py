# 상속에 대해서 배워보자.
# 상속을 통해 클래스를 단순화 시키면서 확장 가능하게 만듦
class Vehicle:
    name = "탈것"
    power = "없음"

    def drive(self):
        print(f"[동력원 : {self.power}] {self.name} 운전하기")


v = Vehicle()
v.drive()


class Bicycle(Vehicle):
    name = "자전거"
    power = "다리"


b = Bicycle()
b.drive()


class Engine:
    power = "엔진"


class MotorCycle(Engine, Vehicle):
    name = "오토바이"


m = MotorCycle()
m.drive()


class Car(Engine, Vehicle):
    name = "자동차"


c = Car()
c.drive()


class Flyable:
    def flying(self):
        print("비행하기")


class Airplane(Flyable, Engine, Vehicle):
    name = "비행기"


a = Airplane()
a.drive()
a.flying()


# 던더메서드
# __init__, __str__
