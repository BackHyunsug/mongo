#fstring.py

name = "홍길동"
age = 23
phone = "010-2222-2222"

s = "이름 : %s 나이 : %d 전화번호 : %s" %(name, age, phone)
print(s)

s1 = "이름 : {} 나이 : {} 전화번호 : {}".format(name, age, phone)
print(s1)

#파이썬 3.6부터 추가됨
s2 = f"이름:{name} 나이:{age}  전화번호:{phone}"
print(s2)


