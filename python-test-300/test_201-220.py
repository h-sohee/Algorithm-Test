# 201
def print_coin():
    pass


# 202
print_coin()

# 203
for i in range(100):
    print_coin()


# 204
def print_coins():
    for j in range(100):
        print("비트코인")


# 205 -> NameError: name 'hello' is not defined
# hello() -> 함수 정의 전 호출
# def hello():
#     print("Hi")

# 206
def message():
    print("A")
    print("B")


message()
print("C")
message()
print()

# 207
print("A")


def message():
    print("B")


print("C")
message()
print()

# 208
print("A")


def message1():
    print("B")


print("C")


def message2():
    print("D")


message1()
print("E")
message2()
print()


# 209
def message1():
    print("A")


def message2():
    print("B")
    message1()


message2()
print()


# 210
def message10():
    print("A")


def message20():
    print("B")


def message30():
    for j in range(3):
        message20()
        print("C")
    message10()


message30()
print()


# 211
def function(s):
    print(s)


function("안녕")
function("Hi")
print()


# 212
def function2(a, b):
    print(a + b)


function2(3, 4)
function2(7, 8)
print()


# 213 -> 함수를 호출할 때 파라미터를 입력하지 않음
# def 함수(문자열):
#     print(문자열)
#
#
# 함수()  # TypeError: 함수() missing 1 required positional argument: '문자열'

# 214 -> 파라미터로 다른 타입을 입력해서 더할 수 없음
# def function3(a, b):
#     print(a + b)
#
#
# function3("안녕", 3)  # TypeError: can only concatenate str (not "int") to str

# 215
def print_with_smile(s):
    print(s + ":D")


# 216
print_with_smile("안녕하세요")
print()


# 217
def print_upper_price(price):
    print(price * 1.3)


print_upper_price(50000)
print()


# 218
def print_sum(a, b):
    print(a + b)


print_sum(10, 20)
print()


# 219
def print_arithmetic_operation(a, b):
    print(a, "+", b, "=", a + b)
    print(a, "-", b, "=", a - b)
    print(a, "*", b, "=", a * b)
    print(a, "/", b, "=", a / b)


print_arithmetic_operation(3, 4)
print()


# 220
def print_max(a, b, c):
    max_v = 0

    if a > max_v:
        max_v = a
    if b > max_v:
        max_v = b
    if c > max_v:
        max_v = c

    print("max:", max_v)

    # if a > b and a > c:
    #     print("max:", a)
    # elif b > a and b > c:
    #     print("max:", b)
    # else:
    #     print("max:", c)


print_max(3, 1, 2)
