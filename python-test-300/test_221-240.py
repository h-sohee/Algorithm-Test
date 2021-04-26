# 221
def print_reverse(s):
    print(s[::-1])


print_reverse("python")
print()


# 222
def print_score(score):
    print(sum(score) / len(score))


print_score([1, 2, 3, 4, 5, 6])
print()


# 223
def print_even(nums):
    for i in nums:
        if i % 2 == 0:
            print(i)


print_even([1, 3, 2, 10, 12, 11, 15])
print()


# 224
def print_keys(dic):
    for keys in dic.keys():
        print(keys)


print_keys({"이름": "김말똥", "나이": 30, "성별": 0})
print()

# 225
my_dict = {"10/26": [100, 130, 100, 100], "10/27": [10, 12, 10, 11]}


def print_value_by_key(dic, day):
    print(dic[day])


print_value_by_key(my_dict, "10/26")
print()


# 226
def print_5xn(s):
    num = int(len(s) / 5)
    for i in range(num + 1):
        print(s[i * 5: i * 5 + 5])


print_5xn("아이엠어보이유알어걸")
print()


# 227
def print_mxn(s, num):
    num = int(len(s) / num)
    for i in range(num + 1):
        print(s[i * num: i * num + num])


print_mxn("아이엠어보이유알어걸", 3)
print()


# 228
def calc_monthly_salary(sal):
    print(int(sal / 12))


calc_monthly_salary(12000000)
print()


# 229
def my_print(a, b):
    print("왼쪽:", a)
    print("오른쪽:", b)


my_print(a=100, b=200)
print()


# 230
def my_print(a, b):
    print("왼쪽:", a)
    print("오른쪽:", b)


my_print(b=100, a=200)
print()


# 231
def n_plus_1(n):
    result = n + 1


n_plus_1(3)
# print(result)   # NameError: name 'result' is not defined


# 232
def make_url(url):
    print("www." + url + ".com")
    return "www." + url + ".com"


make_url("naver")
print()


# 233
def make_list(string):
    s = []
    for i in string:
        s.append(i)

    print(s)
    return s


make_list("abcd")
print()


# 234

# 235

# 236

# 237

# 238

# 239

# 240
