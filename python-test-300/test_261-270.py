# 261
class Stock:
    # 262
    # def __init__(self, name, code, per, pbr, dividend):
    #     self.name = name
    #     self.code = code

    # 266
    def __init__(self, name, code, per, pbr, dividend):
        self.name = name
        self.code = code
        self.per = float(per)
        self.pbr = float(pbr)
        self.dividend = float(dividend)

    # 263
    def set_name(self, name):
        self.name = name

    # 264
    def set_code(self, code):
        self.code = code

    # 265
    def get_name(self):
        return self.name

    def get_code(self):
        return self.code

    # 268
    def set_per(self, per):
        self.per = per

    def set_pbr(self, pbr):
        self.pbr = pbr

    def set_dividend(self, dividend):
        self.dividend = dividend

    def get_per(self):
        return self.per

    def get_pbr(self):
        return self.pbr

    def get_dividend(self):
        return self.dividend


# 262
# samsung = Stock("삼성전자", "005930")
# print(samsung.name, samsung.code)

# 263
a = Stock(None, None)
a.set_name("삼성전자")
print(a.name)

# 264
a.set_code("005930")
print(a.code)

# 265
samsung = Stock("삼성전자", "005930")
print(samsung.get_name(), samsung.get_code())

# 267
samsung = Stock("삼성전자", "005930", 15.79, 1.33, 2.83)
print(samsung.name, samsung.code, samsung.per, samsung.pbr, samsung.dividend)

# 269
samsung.set_per(12.75)
print(samsung.name, samsung.code, samsung.per, samsung.pbr, samsung.dividend)

# 270
list = []

samsung = Stock("삼성전자", "005930", 15.79, 1.33, 2.83)
hyundai = Stock("현대차", "005380", 8.70, 0.35, 4.27)
lg = Stock("엘지전자", "066570", 317.34, 0.69, 1.37)

# list = [samsung, hyundai, lg]
list.append(samsung)
list.append(hyundai)
list.append(lg)

for i in list:
    print(i.code, i.per)






