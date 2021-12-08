"""
내장 자료형 (built-in data types)
숫자) 정수 : int, 실수 : float, 복소수 : complex(실수부 + 허수부)
문자) string
불리언) boolean

두 가지 함수
print({something}) : 화면에 출력해주는 함수
type({something}) : 자료형의 타입을 리턴해주는 함수
"""
# 정수, 소수, 복소수
print(42)
print(3.14)
print(4 + 11j + 4 - 1j)

# 2진수, 8진수, 16진수
print(0b1000)
print(0o1000)
print(0x0ff)

# 문자열(string)
print("answer")
print('문자열')
print('아들이 엄마에게 "엄마 나 100원만" 이라고 말했다.')
print('아들이 엄마에게 \'엄마 나 100원만\' 이라고 말했다.')
print("안녕하세요. \n다롱언니입니다.")
print("안녕하세요. \\역슬래시입니다.")
print("""안녕하세요! 
개행입니다.""")
print('''안녕하세요~ 
개행입니다.''')

# 불리언(True / False) => 1 or 0을 가진 자료형
# 참과 거짓만 있는 자료형
print(1 == 1)
print(1 != 2)
print(1 == 2)
# True는 숫자 1, False는 숫자 0
print(True == 1)
print(False == 0)

# 자료형은 다르지만 내부적으로 int로 다룰 수 있음
# 내부적으로 True를 1로 변환 => 자동 형변환
print(type(True))
print(int(True) == 1)