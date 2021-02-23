# 시간복잡도 -> 빅오 표현법
# O(1)        -> 상수 시간
# O(logN)     -> 로그 시간
# O(N)        -> 선형 시간
# O(NlogN)    -> 로그 선형 시간
# O(N^2)      -> 이차 시간
# O(N^3)      -> 삼차 시간
# O(2^n)      -> 지수 시간

# O(N)------------------------------------------------
array = [3, 5, 1, 2, 4]
summary = 0

for x in array:
    summary += x

print(summary)

# O(1)-------------------------------------------------
a = 5
b = 7
print(a + b)

# O(N^2) ----------------------------------------------
array = [3, 5, 1, 2, 4]     # 5개의 데이터(N = 5)

for i in array:
    for j in array:
        temp = i * j
        print(temp)

# O(N)-------------------------------------------------
temperature = input("What whether why?")
temperature = int(temperature)

if temperature > 30:
    print("very hot")
elif 16 < temperature < 30:
    print("it cool")
else:
    print("Have a nice day")

print(exit)


# 공간 복잡도 -> 빅오 표현법
# int a[1000]: 4KB
# int a[1000000]: 4MB
# int a[2000][2000]: 16MB


# 수행시간 측정
# 선택정렬-기본정렬 수행시간 비교
import time
from random import randint

# 배열에 10000개의 정수를 삽입
array = []
for _ in range(10000):
    array.append(randint(1, 100))

# 선택 정렬 프로그램 성능 측정
start_time = time.time()

# 선택 정렬 프로그램 소스코드
for i in range(len(array)):
    min_index = i           # 기징 작은 원소의 인덱스
    for j in range(i + 1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]     # 스와프

emd_time = time.time()      # 측정 종료
print("선택 정렬 성능 측정: ", emd_time-start_time)        # 수행 시간 출력


# 배열을 다시 무작위 데이터로 초기화
array = []
for _ in range(10000):
    array.append(randint(1, 100))

# 기본 정렬 프로그램 성능 측정
start_time = time.time()

# 기본 정렬 프로그램 소스코드
array.sort()

emd_time = time.time()  # 측정 종료
print("기본 정렬 성능 측정: ", emd_time - start_time)  # 수행 시간 출력




