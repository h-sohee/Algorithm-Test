import random


# 앵겔지수 계산
def calc_engels(f, e):
    engels = (f / e) * 100

    if engels <= 25:
        return "최상위"
    elif engels <= 30:
        return "상위"
    elif engels <= 50:
        return "중위"
    elif engels <= 70:
        return "하위"
    else:
        return "극빈층"


fp = open("engels.csv", "w", encoding="utf-8")
fp.write("food,expenses,label\r\n")

cnt = {"최상위": 0, "상위": 0, "중위": 0, "하위": 0, "극빈층": 0}

for i in range(30000):
    food = random.randint(500, 800)      # 식료품비
    expenses = random.randint(1000, 3000)  # 가계 총 지출액
    label = calc_engels(food, expenses)
    cnt[label] += 1
    fp.write("{0},{1},{2}\r\n".format(food, expenses, label))

print(cnt)
fp.close()
print("ok")
