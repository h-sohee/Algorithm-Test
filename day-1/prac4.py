# 조건문
x = 15

if x >= 10:
    print("x >= 10")

if x >= 0:
    print("x >= 0")

if x >= 30:
    print("x >= 30")

# if-elif-else 예제 (학점구하기)
score = 85

if score >= 90:
    print('학점: A')
elif score >= 80:
    print('학점: B')
elif score >= 70:
    print('학점: C')
else:
    print('학점: F')

# if-pass
if score >= 80:
    pass
else:
    print("성저이 80점 미만입니다.")
print("프로그램을 종료합니다.")


x = 0
y = 1

# 비교 연산자
print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

# 논리 연산자
print(x and y)
print(x or y)
print(not x)


x = [1, 2, 3, 4, 5]
y = {1, 2, 3, 4, 5}
z = (1, 2, 3, 4, 5)

# 기타 연산자
print(6 in x)
print(6 in y)
print(6 in z)
print(6 not in x)
print(6 not in y)
print(6 not in z)
