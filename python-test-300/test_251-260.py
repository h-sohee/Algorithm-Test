# 252
class Human:
    # 254
    # def __init__(self):
    #     print("응애응애")

    # 255
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    # 257
    def who(self):
        print("이름: {} 나이: {} 성별: {}".format(self.name, self.age, self.sex))

    # 258
    def setInfo(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    # 259
    def __del__(self):
        print("나의 죽음을 알리지마라")


# 253-254
# areum = Human()

# 255
areum = Human("아름", 25, "여자")

# 256
print(areum.name, areum.age, areum.sex)

# 257
areum.who()

# 258
serom = Human("모름", 0, "모름")
serom.setInfo("새롬", 29, "여자")
serom.who()

# 259
del serom



