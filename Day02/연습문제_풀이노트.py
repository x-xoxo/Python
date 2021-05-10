# 3.2
'''
name = input("이름을 입력하시오 : ")
height = int(input("키를 입력하시오(단위: cm) : "))
if height < 140:
    print(name, "님은 놀이기구를 탈 수 없습니다.")
else:
    print(name, "님은 놀이기구를 탈 수 있습니다.")
'''
# 3.3
'''
age = int(input("나이를 입력하시오 : "))
height = int(input("키를 입력하시오(단위: cm) : "))

if height >= 150 and age >= 19:
    print("입장할 수 있습니다.")
else:
    print("입장할 수 없습니다.")
'''
# 3.4
'''
age = int(input("나이를 입력하시오 : "))
if age >= 20:
    print("Adult")
elif age >= 10:
    print("Youth")
else:
    print("Kid")
'''
# 3.5
'''
num1, num2 = input("두 정수를 입력하시오 : ").split()
num1 = int(num1)
num2 = int(num2)
if num1 > num2:
    print(num2, num1)
else:
    print(num1, num2)
'''
# 3.6
'''
num1, num2, num3 = input("세 정수를 입력하시오 : ").split()
num1 = int(num1)
num2 = int(num2)
num3 = int(num3)
if num1 > num2 and num1 > num3 and num2 > num3:
    print(num3, num2, num1)
elif num1 > num2 and num1 > num3 and num3 > num2:
    print(num2, num3, num1)
elif num2 > num1 and num2 > num3 and num1 > num3:
    print(num3, num1, num2)
elif num2 > num1 and num2 > num3 and num3 > num1:
    print(num1, num3, num2)
elif num3 > num1 and num3 > num2 and num1 > num2:
    print(num2, num1, num3)
elif num3 > num1 and num3 > num2 and num2 > num1:
    print(num1, num2, num3)
else:
    print(num1, num2, num3)
'''
# 3.7
'''
score = int(input("게임점수를 입력하시오 : "))
if score >= 1000:
    print("고수입니다.")
else:
    print("입문자입니다.")
'''
# 3.8
'''
x, y = input("점의 좌표 x, y를 입력하시오 : ").split()
x = int(x)
y = int(y)
if x > 0 and y > 0:
    print("1사분면에 있음")
elif x < 0 and y > 0:
    print("2사분면에 있음")
elif x < 0 and y < 0:
    print("3사분면에 있음")
elif x > 0 and y < 0:
    print("4사분면에 있음")
else:
    print("(x, y) == (0, 0)")
'''
# 3.9

num = int(input("정수를 입력하시오 : "))
if num % 2 != 0 and num % 3 != 0:
    print(f"{num}은(는) 2와 3 모두로 나누어지지 않습니다.")
elif num % 2 == 0 and num % 3 == 0:
    print(f"{num}은(는) 2와 3 모두로 나누어집니다.")
elif num % 2 == 0:
    print(f"{num}은(는) 2로 나누어집니다.")
elif num % 3 == 0:
    print(f"{num}은(는) 2로 나누어집니다.")
elif num % 2 != 0:
    print(f"{num}은(는) 2로 나누어지지 않습니다.")
elif num % 3 != 0:
    print(f"{num}은(는) 3로 나누어지지 않습니다.")
else:
    pass
