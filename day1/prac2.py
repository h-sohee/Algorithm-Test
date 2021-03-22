# 리스트, 튜플
a = [7, 1, 5, 3, 2, 6, 7, 5]       # 리스트
b = (7, 1, 5, 3, 2, 6, 7, 5)       # 튜플 -> 값을 변경 할 수 없음

a[6] = 7
print(a)

# b[3] = 2 -> TypeError: 'tuple' object does not support item assignment

n = 10
z = [0] * n                        # 리스트에 같은 값 넣기
print(z)

print(a[6])                        # 리스트 특정 원소
print(a[3:6])                      # 리스트 특정 범위 -> 리스트[시작:끝+1]

# 리스트 컴프리헨션
x = [i for i in range(10)]
print(x)

y = [i for i in range(20) if i % 2 == 0]
print(y)

# 리스트 메서드
print()

x.append(10)                       # 원소 추가
print(x)

y.insert(1, 1)                     # 득정 위치에 원소 추가
print(y)

print(x.count(0))                  # 특정 원소 개수

x.remove(3)                        # 원소 제거
print(x)

a.reverse()                        # 리스트 원소 순서 뒤집기
print(a)

a.sort()                           # 오름차순 정렬
print(a)

a.sort(reverse=True)               # 내림차순 정렬
print(a)



