# 21
letters = 'python'
print(letters[0], letters[2])

# 22
license_plate = "24가 2210"
print(license_plate[4:])

# 23
string = "홀짝홀짝홀짝"
print(string[0::2])

# 24
string = "PYTHON"
print(string[::-1])

# 25
phone_number = "010-1111-2222"
print(phone_number.replace("-", " "))

# 26
print(phone_number.replace("-", ""))

# 27
url = "http://sharebook.kr"
print(url.split(".")[1])

# 28
lang = 'python'
# lang[0] = 'p' -> TypeError: 'str' object does not support item assignment
print(lang)

# 29
string = 'abcdfe2a354a32a'
string = string.replace('a', 'A')
print(string)

# 30
string = 'abcd'
string.replace('b', 'B')
print(string)

# 31
a = '3'
b = '4'
print(int(a) + int(b))

# 32
print("Hi" * 3)

# 33
print("-"*80)

# 34
t1 = 'python'
t2 = 'java'
print((t1 + " " + t2 + " ") * 4)

# 35
name1 = "김민수"
age1 = 10
name2 = "이철희"
age2 = 13
print("이름: %s, 나이: %d" % (name1, age1))
print("이름: %s, 나이: %d" % (name2, age2))

# 36
print("이름: {} 나이: {}".format(name1, age1))
print("이름: {} 나이: {}".format(name2, age2))

# 37
print(f"이름: {name1} 나이: {age1}")
print(f"이름: {name2} 나이: {age2}")

# 38
samsung = "5,969,782,550"
samsung = samsung.replace(",", "")
samsung_int = int(samsung)
print(samsung_int, type(samsung_int))

# 39
quarter = "2020/02(E) (IFRS연결)"
print(quarter[0:7])

# 40
data = "   삼성전자    "
data = data.strip()
print(data)

# 41
ticker = "btc_krw"
ticker = ticker.upper()
print(ticker)

# 42
ticker = "BTC_KRW"
ticker = ticker.lower()
print(ticker)

# 43
s = 'hello'
s = s.capitalize()
print(s)

# 44
file_name = "보고서.xlsx"
print(file_name.endswith("xlsx"))

# 45
print(file_name.endswith(("xlsx", "xls")))

# 46
file_name = "2020_보고서.xlsx"
print(file_name.startswith("2020"))

# 47
a = "hello world"
print(a.split(" "))

# 48
ticker = "btc_krw"
print(ticker.split("_"))

# 49
date = "2020-05-01"
print(date.split("-"))

# 50
data = "039490     "
data = date.rstrip()
print(data)








