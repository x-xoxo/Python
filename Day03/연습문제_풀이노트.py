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
'''
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
'''
# 3.10
'''
a, b = input("두 정수를 입력하시오 : ")
a = int(a)
b = int(b)
if a % b == 0:
    print(f"{a}는(은) {b}의 배수입니다.")
else:
    print(f"{a}는(은) {b}의 배수가 아닙니다.")
'''
# 3.11
'''
n = 0
a, b, c = input("세 복권번호를 입력하시오 : ").split()
a = int(a)
b = int(b)
c = int(c)
'''
'''
if a == 2 or a == 3 or a == 9:
    n += 1
if b == 2 or b == 3 or b == 9:
    n += 1
if c == 2 or c == 3 or c == 9:
    n += 1
'''
'''
lotto = [2, 3, 9]
if a in lotto:
    n += 1
if b in lotto:
    n += 1
if c in lotto:
    n += 1
if n == 0:
    print("다음 기회에...")
elif n == 1:
    print("상금 1만원")
elif n == 2:
    print("상금 1천만원")
else:
    print("상금 1억원")
'''
# 3.12
'''
x, y = input("점의 좌표 x, y를 입력하시오 : ").split()
x = int(x)
y = int(y)
r = (x*x + y*y)**0.5
if r <= 10:
    print("원의 내부에 있음")
else:
    print("원의 외부에 있음")
'''
# 3.13
'''
x, y = input("점의 좌표 x, y를 입력하시오 : ").split()
x = int(x)
y = int(y)
r = ((x-3)**2 + (y-4)**2)**0.5
if r <= 10:
    print("원의 내부에 있음")
else:
    print("원의 외부에 있음")
'''
# 3.14
'''
alphabet = input("알파벳을 입력하시오 : ")
vowel = ['a','e','i','o','u']
if alphabet in vowel:
    print(f"{alphabet}(은)는 모음입니다.")
else:
    print(f"{alphabet}(은)는 자음입니다.")
'''
# 3.15
'''
print("for 문 사용")
for i in range(1, 10):
    print("%d * %d = %d" % (2,i,2*i))

print("while 문 사용")
i = 1
while i < 10:
    print("%d * %d = %d" % (2,i,2*i))
    i += 1
'''
# 3.16
'''
dan = int(input("1에서 9까지의 수를 입력하세요 : "))
while True:
    if dan >=2 and dan <=9:
        break
    dan = int(input("1에서 9까지의 수를 다시 입력하세요 : "))
print("for 문 사용")
for i in range(1, 10):
    print("%d * %d = %d" % (dan,i,dan*i))
print("while 문 사용")
i = 1
while i < 10:
    print("%d * %d = %d" % (dan,i,dan*i))
    i += 1
'''
# 3.17
'''
for i in range(3):
    print('Python ')
    print('is ')
    print('FUN! ')
# 'Python \nis \nFUN! ''Python \nis \nFUN! ''Python \nis \nFUN! '

for i in range(3):
    print('Python ')
    print('is ')
print('FUN! ')
# 'Python \nis \n''Python \nis \n''Python \nis \n''FUN! \n'

for i in range(3):
    print('Python ')
print('is ')
print('FUN! ')
# 'Python \n''Python \n''Python \n''is \n''FUN! \n'
'''
# 3.18
'''
print("맛나 식당에 오신것을 환영합니다. 메뉴는 다음과 같습니다")
print("1) 햄버거")
print("2) 치킨")
print("3) 피자")
menu = ['햄버거', '치킨', '피자']
select = int(input("1에서 3까지의 메뉴를 선택하세요 : "))
while True:
    if select in [1,2,3]:
        break
    select = int(input("메뉴를 다시 입력하세요 : "))
print(f"{menu[select-1]}를 선택하였습니다.")
'''
# 3.19
'''
print("맛나 식당에 오신것을 환영합니다. 메뉴는 다음과 같습니다")
print("1) 햄버거")
print("2) 치킨")
print("3) 피자")
menu = ['햄버거', '치킨', '피자']
select = input("메뉴를 선택하세요(알파벳 b, c, p 입력) : ")
while True:
    if select in ['b','c','p']:
        break
    select = input("메뉴를 다시 입력하세요(알파벳 b, c, p 입력) : ")
if select == 'b':
    select = 0
elif select == 'c':
    select = 1
else:
    select = 2
print(f"{menu[select]}를 선택하였습니다.")
'''
# 3.20
'''
n = int(input("숫자를 입력하세요 : "))
for i in range(1, n+1):
    print('*'*i)
for i in range(1, n+1):
    print(' '*(n-i) + '*'*i)
'''
# 3.21
'''
n = int(input("숫자를 입력하세요 : "))
isPrime = True
for i in range(2, n):
    if n % i == 0:
        isPrime = False
        break
print(f"{n}은 소수{'입니다' if isPrime else '가 아닙니다'}")
'''
# 3.22
'''
for i in range(2, 13):
    isPrime = True
    for j in range(2, i):
        if i % j == 0:
            isPrime = False
            break
    print(f"{i} : {'소수' if isPrime else '합성수'}")
'''
# 3.23
'''
sum = 0
n = int(input("숫자를 입력하세요 : "))
for i in range(1, n+1):
    sum += i**2
print(f"결과는 {sum}입니다.")
'''
# 3.24
'''
day = 0
snail = 0
up = 7
down = 5
destination = 30
while True:
    day += 1
    snail += up
    print(f"day : {day} 달팽이의 위치 : {snail} 미터")
    if snail > destination:
        print("탈출 완료")
        break
    snail -= down
'''
# 3.25
'''
n = int(input("n을 입력하시오(1~9) : "))
row = 1
t = 0
for i in range(1, n*n+1):
    if row % 2 == 1:
        t = 0
        print("%3d " % i, end='')
        if i % n == 0:
            row += 1
            print()
    else:
        print("%3d " % (row*n-t), end='')
        t += 1
        if i % n == 0:
            row += 1
            print()
'''
# 3.26
'''
isReverseNum = True
text = input("정수를 입력하시오 : ")
length = len(text)
begin = 0
end = length - 1
while begin < end:
    if text[begin] != text[end]:
        isReverseNum = False
        break
    else:
        begin += 1
        end -= 1
print(f"{text+'은 거꾸로 정수입니다.' if isReverseNum else text+'은 거꾸로 정수가 아닙니다.'}")
'''
# 3.27
'''
fuel = 500
warning = fuel * 0.1
while True:
    if fuel < warning:
        print("경고: 연료가 10% 미만이니 충전하세요!")
        break
    change = int(input("충전 또는 사용한 연료를 +/- 기호와 함께 입력하시오 : "))
    fuel += change
    print(f"현재 탱크양은 {fuel} 입니다.")
'''
