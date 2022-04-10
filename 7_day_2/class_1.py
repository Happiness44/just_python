"""
사각형 컴퍼니는 다양한 사각형의 넓이를 구해주는 회사입니다.
클라이언트에게 사각형의 넓이를 구해달라는 요청이 왔습니다.
클라이언트에게 방문해보니 가로, 세로가 각각 10, 4라고 사각형 측량사에게 연락이 왔습니다.
우리에겐 '넓이 = 가로 X 세로'라는 공식이 있으니 그 공식으로 넓이를 구해주면 될 것 같아요!
"""


def get_area(width, height):
    return width * height


w = 10
h = 4

print("넓이 : ", get_area(w, h))


"""
사업이 잘돼서 갑자기 5군데의 클라이언트에게서 연락이 왔어요!
이제 5개의 사각형을 추가로 관리해야 합니다.
사각형 5개에 대한 데이터가 더 필요하겠군요!
데이터는 각각 (3,5), (5,7), (23,4), (6,8), (9,10) 이었다고 합니다.
추가로 5개의 데이터를 넣어 봅시다.
기존 데이터는 당연히 그래도 있어야 합니다.
"""
w1 = 10
h1 = 4

w2 = 3
h2 = 5

w3 = 5
h3 = 7

w4 = 23
h4 = 4

w5 = 6
h5 = 8

w6 = 9
h6 = 10

# wn, hn ... 계속 늘어나는... 문제, 둘레까지 구해달라고 하면... 문제 => 반복되는 작업이 계속됨!
# 데이터, 함수와 관련이 깊고 그것을 묶을 수 없을 까? -> 클래스 등장!
print(f"사각형의 넓이 : {get_area(w1, h1)}")
print(f"사각형의 넓이 : {get_area(w2, h2)}")
print(f"사각형의 넓이 : {get_area(w3, h3)}")
print(f"사각형의 넓이 : {get_area(w4, h4)}")
print(f"사각형의 넓이 : {get_area(w5, h5)}")
print(f"사각형의 넓이 : {get_area(w6, h6)}")

