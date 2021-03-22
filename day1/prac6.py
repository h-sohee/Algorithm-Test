# 뎃셈 함수
def add(a, b):
    return a + b


# 뺼셈 함수
def sub(a, b):
    return print('결과:', a - b)


print(add(3, 7))
sub(7, 4)


# 함수 패킹, 언패킹
def operator(a, b):
    add_var = a+b
    subtract_var = a-b
    multiply_var = a*b
    divide_var = a/b
    return add_var, subtract_var, multiply_var, divide_var      # 패킹


a, b, c, d = operator(7, 3)             # 언패킹
print(a, b, c, d)


# 람다 표현식
print((lambda x, y: x+y)(3, 7))

# 람다 표현식을 리스트에 적용
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]

result = map(lambda x, y: x+y, list1, list2)

print(list(result))




