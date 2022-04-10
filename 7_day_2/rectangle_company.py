# 데이터와 함수가 엮이게 되면 클래스를 만들어 사용할 수 있음!
class Rectangle:

    def __init__(self, w, h):
        self.width = w
        self.height = h

    def get_area(self):
        return "사각형의 넓이", self.width * self.height

    def get_perimeter(self):
        return "사각형의 둘레", (self.width + self.height) * 2


r1 = Rectangle(10, 4)
r2 = Rectangle(3, 5)
r3 = Rectangle(5, 7)
r4 = Rectangle(23, 4)
r5 = Rectangle(6, 8)
r6 = Rectangle(9, 10)


print(r1.get_area(), r1.get_perimeter())
print(r2.get_area(), r2.get_perimeter())
print(r3.get_area(), r3.get_perimeter())
print(r4.get_area(), r4.get_perimeter())
print(r5.get_area(), r5.get_perimeter())
print(r6.get_area(), r6.get_perimeter())

