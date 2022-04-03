"""
% 사용하기
%s : 문자열
%i : 숫자
"""

# 암묵적으로 숫자는 문자로 변환 가능 But, 문자는 숫자로 변환 불가
name = "아름"
age = 29
test = "안녕 %s %s" % (name, age)
print(test)


# String 포맷
"""
타입에 관계없이 넣을 수 없나?
파이썬 3부터 가능
format() 함수를 사용하자!
사용법 : "문자열".format(*args, **kwargs)

*args
'{} {} {} {} ... {}'.format('param1', 2, 'param3', ... , paramN)
파라미터를 여러 개 넣을 수 있다는 것을 의미
중괄호 {}는 파라미터 갯수만큼 넣을 수 있으며 적어도 상관없으나 많으면 IndexError가 발생

**kwargs
'{key1} {key2} {key3}'.format(key1='a', key2='b', key3=3)
파라미터의 키와 값이 같이 있는 형태를 의미
*args와 마찬가지로 키에 있는 값이 덜 들어가는 것은 괜찮지만, 파라미터가 더 많다 거나 모르는 키가 들어가면 KeyError 발생

% 를 사용하는 방법보다는 좋아졌지만,
여전히 문자열과 파라미터의 갯수 혹은 키가 맞지 않으면 에러가 나게 될 가능성이 있고,
파라미터가 많아지면 많아질 수록 스트링과 format 함수의 값을 맞추는 것이 힘듦
"""
version = 3
function_name = "format()"
print("파이썬 {0}부터 가능 {1} 함수를 사용하자".format(version, function_name))


print("{key1} {key2} {key3}".format(key1="문자열1", key2="문자열2", key3=3))


txt1 = "울릉도"
txt2 = "동남쪽"
txt3 = "뱃길따라"
txt4 = "87k"
txt5 = "외로운"
txt6 = "섬하나"
txt7 = "새들의 고향"
print("{} {} {} {} {} {} {}".format(txt1, txt2, txt3, txt4, txt5, txt6, txt7))

# 가독성과 복잡함을 줄이기 위해 f-string 사용
