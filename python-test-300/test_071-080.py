# 71
my_variable = ()
print(my_variable, type(my_variable))

# 72
movie_rank = ('닥터 스트레인지', '스플릿', '럭키')
print(movie_rank)

# 73
a = (1)
print(a, type(a))        # 정수로 저장됨
b = (1,)
print(b, type(b))        # 튜플로 저장됨

# 74
t = (1, 2, 3)
# t[0] = 'a'    # TypeError: 'tuple' object does not support item assignment -> 튜플값은 변경할 수 없음

# 75
t = 1, 2, 3, 4
print(type(t))

# 76
t = ('a', 'b', 'c')
t = ('A', 'b', 'c')
print(t)

# 77
interest = ('삼성전자', 'LG전자', 'SK Hynix')
interest = list(interest)
print(interest)

# 78
interest = tuple(interest)
print(interest)

# 79
temp = ('apple', 'banana', 'cake')
a, b, c = temp      # unpacking
print(a, b, c)

temps = a, b, c     # packing
print(temps)

# 80
num = tuple(range(2, 100, 2))
print(num)


