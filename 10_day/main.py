# 실행 파일
# import test_module as m
# from test_module import val, add, Name
from test_module import *
# val이 덮어 씌워짐
from test_module2 import val

# print(m.val)
# print(m.add(10, 20))

# name = m.Name("아롱")
# print(name)


print(val)
print(add(10, 20))

name = Name("아롱")
print(name)

