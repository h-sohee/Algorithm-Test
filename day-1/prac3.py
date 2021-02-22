# 문자열 연산
a = 'Hello'
b = 'World'
print(a+b)

c = "String"
print(c * 3)

d = "ABCDEF"
print(d[2:4])


# 딕셔너리
data = dict()
data['사과'] = 'Apple'
data['바나나'] = 'Banana'
data['코코넛'] = 'Coconut'

print(data)

if '사과' in data:
    print("'사과'를 키로 가지는 데이터가 존재합니다.")

e = {
    '홍길동': 97,
    '이순신': 98
}

print(e)
print(e['이순신'])

key_list = list(e.keys())
print(key_list)




