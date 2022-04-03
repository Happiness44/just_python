# 그 외의 연산자

# 비트 연산
print(bin(42))
print(bin(10))

"""
101010
001010
|(파이프), &(앤드), ^(캐럿), ~(틸드)

101010 | 001010 = 101010
101010 | 001011 = 101011

101010 & 001010 = 001010

^ : 1와 0이 다른 경우에만 1
101010 ^ 001011 = 100001

~42 : -42 - 1
~~42 : -(-43) - 1 = 42 
"""
print(42 | 10)
print(42 | 11)

print(42 & 10)

print(42 ^ 11)

print(~42)
print(~~42)

# 항등 연산
# id 함수 : 값의 메모리 주소
txt = "python"
txt = "python"
print(id(txt))

print(id(1))
print(id("1"))
print(1 == "1")

# 멤버 연산
# in, not in
fruits = ["사과", "바나나", "오렌지"]
print("사과가 있나요? ", "사과" in fruits)
print("딸기가 있나요? ", "딸기" in fruits)
print("키위는 없나요? ", "키위" not in fruits)
