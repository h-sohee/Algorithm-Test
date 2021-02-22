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
import time

start_time = time.time()
# 실행할 소스코드
emd_time = time.time()
print("time: ", emd_time-start_time)

