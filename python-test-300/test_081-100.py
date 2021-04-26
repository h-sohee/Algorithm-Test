# 81
a, b, *c = (0, 1, 2, 3, 4, 5)
print(a)
print(b)
print(c)

scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
*valid_score, a_score, b_score = scores
print(valid_score)
print(a_score)
print(b_score)

# 82
a_score, b_score, *valid_score = scores
print(a_score)
print(b_score)
print(valid_score)

# 83
a_score, *valid_score, b_score = scores
print(a_score)
print(valid_score)
print(b_score)

# 84
temp = {}
print(temp, type(temp))

# 85
icecream = {"메로나": 1000, "폴라포": 1200, "빵빠레": 1800}
print(icecream)

# 86
icecream["죠스바"] = 1200
icecream["월드콘"] = 1500
print(icecream)

# 87
print("메로나 가격:", icecream["메로나"])

# 88
icecream["메로나"] = 1300
print("메로나 가격:", icecream["메로나"])

# 89
del icecream["메로나"]
print(icecream)

# 90
# print(icecream['누가바'])    # KeyError: '누가바' -> 누가바 라는 키가 딕셔너리에 없음

# 91
inventory = {"메로나": [300, 20], "비비빅": [400, 3], "죠스바": [250, 100]}
print(inventory)

# 92
print(inventory["메로나"][0], "원")

# 93
print(inventory["메로나"][1], "개")

# 94
inventory["월드콘"] = [500, 7]
print(inventory)

# 95
icecream2 = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
key_list = list(icecream2.keys())
print(key_list)

# 96
value_list = list(icecream2.values())
print(value_list)

# 97
print(sum(value_list))

# 98
new_product = {'팥빙수': 2700, '아맛나': 1000}
icecream.update(new_product)
print(icecream)

# 99
keys = ("apple", "pear", "peach")
vals = (300, 250, 400)
result = dict(zip(keys, vals))
print(result)

# 100
date = ['09/05', '09/06', '09/07', '09/08', '09/09']
close_price = [10500, 10300, 10100, 10800, 11000]
close_table = dict(zip(date, close_price))
print(close_table)



