# 161
for i in range(0, 100):
    print(i)

# 162
for i in range(2002, 2051, 4):
    print(i)

# 163
for i in range(1, 31):
    if i % 3 == 0:
        print(i)

# 164
for i in range(100):
    print(99 - i)

# 165
for i in range(10):
    print(i / 10)

# 166
for i in range(1, 10):
    print("3 X", i, "=", 3*i)

# 167
for i in range(1, 10, 2):
    print("3 X", i, "=", 3*i)

# 168
result = 0

for i in range(1, 11):
    result += i

print(result)

# 169
result = 0

for i in range(1, 11):
    if i % 2 == 1:
        result += i

print(result)

# 170
result = 1

for i in range(1, 11):
    result *= i

print(result)

# 171
price_list = [32100, 32150, 32000, 32500]

for i in price_list:
    print(i)

# 172
for i, j in enumerate(price_list):
    print(i, j)

# 173
for i, j in enumerate(price_list):
    print((len(price_list) - 1) - i, j)

# 174
for i in range(1, 4):
    print(90 + 10 * i, price_list[i])

# 175
my_list = ["가", "나", "다", "라"]

for i in range(1, len(my_list)):
    print(my_list[i - 1], my_list[i])

# 176
my_list2 = ["가", "나", "다", "라", "마"]

for i in range(1, len(my_list2) - 1):
    print(my_list2[i - 1], my_list2[i], my_list2[i + 1])

# 177
for i in range(1, len(my_list)):
    print(my_list[len(my_list) - i], my_list[len(my_list) - i - 1])

# 178
my_list3 = [100, 200, 400, 800]

for i in range(len(my_list3) - 1):
    print(abs(my_list3[i+1] - my_list3[i]))

# 179
my_list4 = [100, 200, 400, 800, 1000, 1300]

for i in range(0, len(my_list4) - 2):
    sum = my_list4[i] + my_list4[i + 1] + my_list4[i + 2]
    print(sum / 3)

# 180
low_prices = [100, 200, 400, 800, 1000]
high_prices = [150, 300, 430, 880, 1000]

volatility = []

for i in range(len(low_prices)):
    volatility.append(high_prices[i] - low_prices[i])

print(volatility)




