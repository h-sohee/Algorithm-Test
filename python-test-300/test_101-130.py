# 101
print(type(True), type(False))

# 102
print(3 == 5)

# 103
print(3 < 5)

# 104
x = 4
print(1 < x < 5)

# 105
print((3 == 3) and (4 != 3))

# 106
# print(3 => 4)       # SyntaxError: invalid syntax -> >=, <=, ==, !=

# 107
if 4 < 3:
    print("Hello World")

# 108
if 4 < 3:
    print("Hello World.")
else:
    print("Hi, there.")

# 109
if True:
    print("1")
    print("2")
else:
    print("3")

print("4")
print()

# 110
if True:
    if False:
        print("1")
        print("2")
    else:
        print("3")
else:
    print("4")

print("5")

111
s = input("입력하세요: ")
print(s * 2)

# 112
num = int(input("숫자를 입력하세요: "))
print(num + 10)

# 113
nums = int(input("숫자를 입력하세요: "))

if nums % 2 == 0:
    print("짝수")
else:
    print("홀수")

# 114
n = int(input("숫자를 입력하세요: "))

if n + 20 > 255:
    print(255)
else:
    print(n + 20)

# 115
n = int(input("숫자를 입력하세요: "))

if n - 20 < 0:
    print(0)
elif n - 20 > 255:
    print(255)
else:
    print(n - 20)

# 116
time = input("시간을 입력하세요(예: 09:00): ")

if time[-2:] == '00':
    print("정각입니다.")
else:
    print("정각이 아닙니다.")

# 117
fruit = ["사과", "포도", "홍시"]
f = input("좋아하는 과일은? ")

if f in fruit:
    print("정답입니다.")
else:
    print("오답입니다.")

# 118
warn_investment_list = ["Microsoft", "Google", "Naver", "Kakao", "SAMSUNG", "LG"]
w = input("종목명: ")

if w in warn_investment_list:
    print("투자 경고 종목입니다.")
else:
    print("투자 경고 종목이 아닙니다.")

# 119
fruit = {"봄": "딸기", "여름": "토마토", "가을": "사과"}
f = input("좋아하는 계절은? ")

if f in fruit:
    print("정답입니다.")
else:
    print("오답입니다.")

# 120
f = input("좋아하는 과일은? ")

if f in fruit.values():
    print("정답입니다.")
else:
    print("오답입니다.")

# 121
u = input("문자 하나를 입력하세요.")

if u.islower():
    print(u.upper())
else:
    print(u.lower())

# 122
score = int(input("score:"))

if score > 80:
    print("grade is A")
elif score > 60:
    print("grade is B")
elif score > 40:
    print("grade is C")
elif score > 20:
    print("grade is D")
else:
    print("grade is E")

# 123
money = input("입력(예:100 달러): ")

exchange = {"달러": 1167, "엔": 1.096, "유로": 1268, "위안": 171}
num, currency = money.split(" ")
print(float(num) * exchange[currency], "원")

# 124
num1 = int(input("input number1:"))
num2 = int(input("input number2:"))
num3 = int(input("input number3:"))

nums = [num1, num2, num3]
nums.sort()

print(nums[2])

# 125
phone = input("휴대전화 번호 입력: ")

num, _, _ = phone.split("-")

if num == "011":
    agency = "SKT"
elif num == "016":
    agency = "KT"
elif num == "019":
    agency = "LGU"
elif num == "010":
    agency = "알수없음"

# print("당신은", agency, "사용자 입니다")
print(f"당신은 {agency} 사용자 입니다")

# 126
address = input("우편번호:")
address = address[0:3]

if address in ["010", "011", "012"]:
    print("강북구")
elif address in ["013", "014", "015"]:
    print("도봉구")
elif address in ["016", "017", "018", "019"]:
    print("노원구")

# 127
number = input("주민등록번호: ")
number1 = number.split("-")[1]

if number1[0] == "1" or number1[0] == "3":
    print("남자")
elif number1[0] in ["2", "4"]:
    print("여자")

# 128
if "00" <= number1[1:3] <= "08":
    print("서울입니다.")
elif "09" <= number1[1:3] <= "12":
    print("부산입니다.")
else:
    print("아닙니다.")

# 129
calc1 = int(number[0]) * 2 + int(number[1]) * 3 + int(number[2]) * 4 + int(number[3]) * 5 + int(number[4]) * 6 + int(number[5]) * 7 \
        + int(number[7]) * 8 + int(number[8]) * 9 + int(number[9]) * 2 + int(number[10]) * 3 + int(number[11]) * 4 + int(number[12]) * 5
check = 11 - (calc1 % 11)

if check == int(number[-1]):
    print("유효한 주민등록번호입니다.")
else:
    print("유효하지 않은 주민등록번호입니다.")

# 130
import requests

btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']

change = int(btc["max_price"]) - int(btc["min_price"])
price = int(btc["opening_price"]) + change

if price > int(btc["max_price"]):
    print("상승장")
else:
    print("하락장")
