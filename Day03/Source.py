# Day03
# Chapter 06
# 예제: 6개의 원 그리기
'''
import turtle
t = turtle.Turtle(shape="turtle")
for count in range(6):
    t.circle(100)
    t.left(360/6)
'''
# Lab 반복을 사용하여 도형 그리기
'''
import turtle
t = turtle.Turtle(shape="turtle")

for i in range(3):
    t.fd(100)
    t.left(360/3)

t.up()
t.goto(200,0)
t.down()

for i in range(4):
    t.fd(100)
    t.left(360/4)
'''
# Lab n각형 그리기
'''
import turtle
t = turtle.Turtle(shape="turtle")
n = turtle.textinput("", "몇각형을 원하시나요?")
n = int(n)

for i in range(n):
    t.fd(100)
    t.lt(360/n)
'''
# Lab 거북이를 랜덤하게 움직이기
'''
import turtle
import random
t = turtle.Turtle(shape="turtle")

for i in range(30):
    length = random.randint(1, 100)
    t.fd(length)
    angle = random.randint(-180, 180)
    t.lt(angle)
'''
# Lab 팩토리얼 계산하기
'''
n = int(input("정수를 입력하시오 : "))
fact = 1
for i in range(1, n+1):
    fact = fact * i
print(f"{n}!은 {fact}이다.")
'''
# 예제: 사각형 그리기
'''
import turtle
t = turtle.Turtle(shape="turtle")
i = 0
while i < 4:
    t.fd(100)
    t.rt(360/4)
    i = i + 1
'''
# Lab 구구단 출력
'''
i = 2
while i <= 9:
    print("%4i 단" % (i))
    for j in range(1, 10):
        print("%d * %d = %d" % (i, j, i*j))
    i = i + 1
'''
# Lab 별그리기
'''
import turtle
t = turtle.Turtle(shape="turtle")
i = 0
while i < 5:
    t.fd(200)
    t.rt(144)
    i += 1
'''
# Lab 사용자가 입력하는 숫자의 합 계산하기
'''
total = 0
answer = 'yes'
while answer == 'yes':
    num = int(input("숫자를 입력하시오 : "))
    total += num
    answer = input("계속?(yes/no): ")
print(f"합계는 {total}")
'''
# Lab 숫자 맞추기 게임
'''
import random
tries = 0
guess = 0
answer = random.randint(1, 100)
print("1부터 100 사이의 숫자를 맞추시오")
while guess != answer:
    guess = int(input("숫자를 입력하시오 : "))
    tries += 1
    if tries >= 10:
        break
    if guess < answer:
        print("낮음!")
    elif guess > answer:
        print("높음!")
if guess == answer:
    print(f"축하합니다. 시도횟수 = {tries}")
else:
    print(f"정답은 = {answer}")
'''
# Lab 산수 문제 발생기
'''
import random

while True:
    x = random.randint(1, 100)
    y = random.randint(1, 100)
    op = random.choice(['-', '+'])
    if op == '+':
        print(f"{x} + {y} = ", end="")
        answer = int(input())
        if (x+y) == answer:
            print("잘했어요!!")
        else:
            print("다음번에는 잘할 수 있죠?")
    else:
        print(f"{x} - {y} = ", end="")
        answer = int(input())
        if (x-y) == answer:
            print("잘했어요!!")
        else:
            print("다음번에는 잘할 수 있죠?")
'''
# Lab 모든 샌드위치 종류 출력하기
'''
breads = ['호밀빵', '위트', '화이트']
meats = ['미트볼', '소시지', '닭가슴살']
vegis = ['양상추', '토마토', '오이']
sauces = ['마요네즈', '허니 머스타드', '칠리']

for b in breads:
    for m in meats:
        for v in vegis:
            for s in sauces:
                print(b+"+"+m+"+"+v+"+"+s)
'''
# Lab 시계 그리기
'''
import turtle
t = turtle.Turtle(shape="turtle")
t.color('red')
t.stamp()
move = 30

for i in range(12):
    t.up()
    t.fd(50)
    t.down()
    t.fd(25)
    t.up()
    t.fd(15)
    t.stamp()
    t.home()
    t.right(move)
    move += 30
'''
# Lab 점치는 게임
'''
import sys
import random

while True:
    name = input("이름 : (종료하려면 엔터키) ")
    if name == "":
        sys.exit()
    question = input("무엇에 대하여 알고 싶은가요?")
    print(name+"님", "\"", question, "\" 에 대하여 질문 주셨군요.")
    print("운명의 주사위를 굴려볼게요...")

    answer = random.randint(1,8)

    if answer == 1:
        print("네, 확실합니다.")
    elif answer == 2:
        print("전망이 좋은 거 같은데요.")
    elif answer == 3:
        print("믿으셔도 됩니다.")
    elif answer == 4:
        print("글쎄요 아닌 거 같군요.")
    elif answer == 5:
        print("한 점의 의심도 없이 맞습니다.")
    elif answer == 6:
        print("그럼요, 명백히 올바른 선택을 했습니다.")
    elif answer == 7:
        print("제 답변은 No입니다.")
    else:
        print("나중에 다시 물어보세요.")
'''
# Chapter 06 연습문제
# Q01
'''
for i in range(2, 101):
    if i % 2 == 0:
        print(i, end=" ")
'''
# Q02
'''
year = 0
balance = 1000

while balance <= 2000:
    year += 1
    interest = balance * 0.07
    balance += interest
    print(f"{year}년 후 금액 : {balance}")
print(year, "년이 걸립니다.")
'''
# Q03
'''
n = 1234
sum = 0
while n > 0:
    digit = n % 10
    sum += digit
    n //= 10
print(sum)
'''
# Q04
'''
ans = 0
while ans != 3*9:
    ans = int(input("3*9는"))
print("맞았습니다.")
'''
# Q05
'''
sum = 0
while True:
    x = int(input("정수를 입력하시오 : "))
    if x == 0:
        break
    sum += x
print(f"합은 {sum}입니다.")
'''
# Q06
'''
import random
for i in range(3):
    d1 = random.randint(1, 6)
    d2 = random.randint(1, 6)
    print(f"첫번째 주사위 = {d1}, 두번째 주사위 = {d2}")
'''
# Q07
'''
import turtle
t = turtle.Turtle(shape="turtle")
t.color('blue')
angle = 60
for i in range(6):
    t.fd(100); t.fd(-30); t.lt(60); t.fd(30); t.fd(-30); t.rt(120); t.fd(30); t.fd(-30);
    t.home()
    t.lt(angle)
    angle += 60
'''
