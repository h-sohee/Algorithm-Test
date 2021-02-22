# while (1~9 정수의 합)
i = 1
result1 = 0

while i <= 9:
    result1 += i
    i += 1

print(result1)

# while (1~9 정수 중 홍수의 합)
i = 1
result2 = 0

while i <= 9:
    if i % 2 == 1:
        result2 += i
    i += 1

print(result2)

# for (리스트 값 출력)
array = [9, 8, 7, 6, 5]

for x in array:
    print(x)

# for-range (1~9 정수의 합)
result3 = 0
for i in range(1, 10):
    result3 += i

print(result3)

# for-continue (1~9 정수 중 홍수의 합)
result4 = 0

for i in range(1, 10):
    if i % 2 == 0:
        continue
    result4 += i

print(result4)

# while-break (1~5 정수 출력)
i = 1

while True:     # 무한반복
    print("현재 i의 값:", i)
    if i == 5:
        break
    i += 1

# 반복문 예제 (구구단)
for i in range(2,10):
    for j in range(1, 10):
        print(i, "X", j, "=", i*j)
    print()

