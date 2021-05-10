# 1장
'''
print('강동욱')
print('인천',end=' ')
print("{} and {}".format('강동욱','인천'))
print("{1} and {0} and {1}".format('강동욱','인천'))
print("{a} and {b} and {a}".format(a='강동욱',b='인천'))
print("%s이(가) 좋아하는 숫자는 %d입니다." % ('강동욱', 9))
print("Test : {0:5d}, Price : {1: 4.2f}".format(776, 6543.123))
print("Test : %5d, Price : %4.2f" % (776, 6543.123))
print("\'강동욱\'")
print("\\강동욱\\\n\n")
print("test")
print("안녕!" + str(3))
print("안녕하세요? 여러분")
print("저는 파이썬을 무척 좋아합니다.")
print("9*8은", 9*8, "입니다.")
print("안녕히계세요.")
'''
# turtle 프로그램
'''
import turtle
t = turtle.Pen()
t.shape("turtle")
'''
# 사각형
'''
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
'''
# 육각형
'''
t.forward(100)
t.right(60)
t.forward(100)
t.right(60)
t.forward(100)
t.right(60)
t.forward(100)
t.right(60)
t.forward(100)
t.right(60)
t.forward(100)
'''
'''
import turtle
colors = ["red", "purple", "blue", "green", "yellow", "orange" ]
t = turtle.Turtle()

turtle.bgcolor("black")
t.speed(0)
t.width(3)
length = 10

while length < 500:
    t.forward(length)
    t.pencolor(colors[length%6])
    t.right(89)
    length += 5
'''
'''
import turtle
t = turtle.Turtle()
t.shape("turtle")
t.fd(100)
t.lt(120)
t.fd(100)
t.lt(120)
t.fd(100)
t.lt(120)
'''
'''
import turtle
t = turtle.Turtle()
t.shape("turtle")
t.fd(100)
t.lt(60)
t.fd(100)
t.lt(60)
t.fd(100)
t.lt(60)
t.fd(100)
t.lt(60)
t.fd(100)
t.lt(60)
t.fd(100)
t.circle(100)
'''
'''
import turtle
t = turtle.Turtle()
t.shape("turtle")
t.fd(100)
t.lt(60)
t.fd(100)
t.lt(60)
t.fd(100)
t.lt(60)
t.fd(100)
t.lt(60)
t.fd(100)
t.lt(60)
t.fd(100)
t.circle(100)
t.lt(60)
t.backward(100)
'''
# 연습문제 (1장)
# 1번
'''
print("환영합니다.\n파이썬의 세계에 오신 것을 환영합니다.\n파이썬은 강력합니다.")
'''
# 2번
'''
print("반갑습니다. 파이썬!")
print(2*3/10)
print("Hello", "World", "!!!")
# -> 반갑습니다. 파이썬!
# -> 0.6
# -> Hello World !!!
'''
# 3번
'''
print("일주일은", 7*24, "시간 입니다.")
'''
# 4번
'''
import turtle
t = turtle.Turtle()
t.shape("turtle")
t.width(3)
t.fd(100)
t.lt(90)
t.fd(100)
t.rt(90)
t.fd(100)
t.rt(90)
t.fd(100)
t.lt(90)
t.fd(100)
'''
# 5번
'''
import turtle
t = turtle.Turtle()
t.shape("turtle")
t.width(10)
t.fd(100)
t.lt(90)
t.fd(100)
'''
# 6번
'''
import turtle
t = turtle.Turtle()
t.shape("turtle")
t.color("blue")
t.fd(100)
'''
# 7번
'''
import turtle
t = turtle.Turtle()
t.shape("square")
t.fd(100)
'''
# 8번
'''
import turtle
t = turtle.Turtle()
t.shape("turtle")
t.fd(100)
t.up()
t.goto(0,100)
t.down()
t.fd(100)
'''
# 9번
'''
import turtle
t = turtle.Turtle()
t.shape("turtle")
t.width(2)

# t.fillcolor("black")
# t.begin_fill()
t.circle(100)
# t.end_fill()

t.up()
t.goto(-190, 0)
t.down()
t.color("blue")
# t.fillcolor("blue")
# t.begin_fill()
t.circle(100)
# t.end_fill()

t.up()
t.goto(190, 0)
t.down()
t.color("red")
# t.fillcolor("red")
# t.begin_fill()
t.circle(100)
# t.end_fill()

t.up()
t.goto(-100, -120)
t.down()
t.color("yellow")
# t.fillcolor("yellow")
# t.begin_fill()
t.circle(100)
# t.end_fill()

t.up()
t.goto(100, -120)
t.down()
t.color("green")
# t.fillcolor("green")
# t.begin_fill()
t.circle(100)
# t.end_fill()
'''
# 2장
'''
name = input("이름을 입력하세요 : ")
print(name,"씨, 안녕하세요?")
print("파이썬에 오신 것을 환영합니다")
x = int(input("첫 번째 정수를 입력하시오: "))
y = int(input("두 번째 정수를 입력하시오: "))
sum = x+y
print(x, "과", y, "의 합은", sum, "입니다")
'''
# 집 그리기 프로그램
'''
import turtle
t = turtle.Turtle(shape='turtle')
size = int(input("집의 크기는 얼마로 할까요? "))

t.fd(size)
t.rt(90)
t.fd(size)
t.rt(90)
t.fd(size)
t.rt(90)
t.fd(size)

t.rt(90)
t.fd(size)
t.lt(120)
t.fd(size)
t.lt(120)
t.fd(size)
t.lt(120)
'''
# 로봇 기자 만들기
'''
stadium = input("경기장은 어디입니까?")
winner = input("이긴 팀은 어디입니까?")
loser = input("진 팀은 어디입니까?")
vip = input("우수선수는 누구입니까?")
score = input("스코어는 몇대몇입니까?")

print("")
print("==================================================")
print("오늘 {}에서 야구 경기가 열렸습니다.".format(stadium))
print("{}과 {}은 치열한 공방전을 펼쳤습니다.".format(winner,loser))
print("%s이 맹활약을 하였습니다." % (vip))
print("결국 %s가 %s를 %s로 이겼습니다." % (winner, loser, score))
print("==================================================")
'''
# 부동산 광고 만들기
'''
street = input("위치를 입력하시오 : ")
type = input("종류를 입력하시오 : ")
number_of_rooms = int(input("방의 개수를 입력하시오 : "))
price = input("가격을 입력하시오 : ")

print("##################")
print("#                #")
print("# 부동산 매물 광고 #")
print("#                #")
print("##################")
print("")
print("{0}에 위치한 아주 좋은 {1}가 매물로 나왔습니다. 이 {1}는 {2}개의 방을 가지고 있으며 가격은 {3}입니다.".format(street, type, number_of_rooms, price))
'''
# 연습문제 (2장)
# 1번
'''
from datetime import date
d = date.today()
year = d.year
name = input("이름을 입력하시오 : ")
age = int(input("나이를 입력하시오 : "))
year = year-age+100
print("{}씨는 {}년에 100살이시네요!".format(name, year))
'''
# 2번
'''
num1 = int(input("첫 번째 숫자를 입력하시오 : "))
num2 = int(input("두 번째 숫자를 입력하시오 : "))
num3 = int(input("세 번째 숫자를 입력하시오 : "))
avg = (num1+num2+num3)/3
print("%d, %d, %d의 평균은 %.1f입니다." % (num1, num2, num3, avg))
'''
# 3번
'''
radius = float(input("반지름을 입력하시오 : "))
area = 3.141592 * radius * radius
print("반지름이 {}인 원의 넓이 = {}".format(radius, area))
'''
# 4번
'''
import turtle
t = turtle.Turtle(shape="turtle")
radius = 50
t.up()
t.goto(0, 0)
t.down()
t.circle(radius)
t.up()
t.goto(100, 0)
t.down()
radius += 20
t.circle(radius)
t.up()
t.goto(200, 0)
t.down()
radius += 20
t.circle(radius)
'''
# 5번
'''
import turtle
t = turtle.Turtle(shape="turtle")
side = 100
t.fd(side)
t.lt(120)
t.fd(side)
t.lt(120)
t.fd(side)
t.lt(120)
'''
# 6번
'''
import turtle
t = turtle.Turtle(shape="turtle")
side = 200
t.fd(side)
t.lt(120)
t.fd(side)
t.lt(120)
t.fd(side)
t.lt(120)
'''
# 7번
'''
import turtle
t = turtle.Turtle(shape="turtle")
side = int(input("변의 길이 : "))
angle = 90
t.up()
t.goto(-side, side)
t.down()
t.fd(side*2)
t.rt(angle)
t.fd(side*2)
t.rt(angle)
t.fd(side*2)
t.rt(angle)
t.fd(side*2)
t.rt(angle)
t.up()
t.goto(-side, 0)
t.down()
t.fd(side*2)
t.up()
t.goto(0, side)
t.down()
t.rt(angle)
t.fd(side*2)
'''
# 3장
# 나머지 연산자 %
'''
p = int(input("분자를 입력하시오 : "))
q = int(input("분모를 입력하시오 : "))
print("나눗셈의 몫 = ", p // q)
print("나눗셈의 나머지 = ", p % q)
'''
# %를 이용한 홀짝 구분
'''
number = int(input("정수를 입력하시오 : "))
print(number % 2)
'''
# %를 이용한 시,분,초 계산
'''
sec = int(input("초를 입력하시오 : "))
hour = sec // 3600
sec = sec % 3600
min = sec // 60
sec = sec % 60
print("%d시간 %d분 %d초" % (hour, min, sec))
'''
# 다각형 그리기
'''
import turtle
t = turtle.Turtle(shape="turtle")
n = int(input("몇각형을 그리시겠어요?(3~8): "))
angle = 360 // n
for i in range(n):
    t.fd(100)
    t.lt(angle)
'''
# 커피 가게 매출 계산하기
'''
americano_price = 2000
cafelatte_price = 3000
capucino_price = 3500

americanos = int(input("아메리카노 판매 개수: "))
cafelattes = int(input("카페라떼 판매 개수: "))
capucinos = int(input("카푸치노 판매 개수: "))

sales = americanos*americano_price
sales = sales + cafelattes*cafelatte_price
sales = sales + capucinos*capucino_price
print("총 매출액은 %d원입니다." % (sales))
if sales < 100000:
    print(100000-sales,"원 적자입니다.")
else:
    print(sales-100000, "원 흑자입니다.")
'''
# 화씨 -> 섭씨 변환하기
'''
F = float(input("화씨온도 : "))
C = (F-32)*5/9
print("섭씨온도 : %.1f" % (C))
'''
# BMI 계산하기
'''
weight = float(input("몸무게를 kg단위로 입력하시오 : "))
height = float(input("키를 m단위로 입력하시오 : "))
bmi = weight/(height**2)
print("당신의 BMI =",bmi)
'''
# 자동 판매기 프로그램
'''
money = int(input("투입한 돈 : "))
price = int(input("물건 값 : "))
change = money-price
print("거스름돈 : {}".format(change))
coin500s = change // 500
change = change % 500
coin100s = change // 100
change = change % 100
coin50s = change // 50
change = change % 50
coin10s = change // 10
print("500원 동전의 개수 : {}".format(coin500s))
print("100원 동전의 개수 : {}".format(coin100s))
print("50원 동전의 개수 : {}".format(coin50s))
print("10원 동전의 개수 : {}".format(coin10s))
'''
# 지수 연산자 **
'''
a = 1000
r = 0.05
n = 10
print(a*(1+r)**n)
'''
# 연습문제 (3장)
# 1번
'''
x = int(input("x : "))
y = int(input("y : "))
print("두 수의 합 : {}".format(x+y))
print("두 수의 차 : {}".format(x-y))
print("두 수의 곱 : {}".format(x*y))
print("두 수의 평균 : {}".format((x+y)/2))
print("큰수 : {}".format(max(x, y)))
print("작은 수 : {}".format(min(x, y)))
'''
# 2번
'''
r = int(input("r : "))
h = int(input("h : "))
vol = 3.141592 * r ** 2 * h
print("원기둥의 부피 = {}".format(v))
'''
# 3번
'''
x = int(input("정수를 입력하시오 : "))
sum = 0
for i in range(len(str(x))):
    sum += int(strx[i])
print(f"자릿수의 합 : {sum}")
'''
# 4번
'''
x1 = int(input("x1 : "))
y1 = int(input("y1 : "))
x2 = int(input("x2 : "))
y2 = int(input("y2 : "))
diff = ((x1-x2) ** 2 + (y1-y2) ** 2) ** 0.5
print(f"두점 사이의 거리 = {diff}")
'''
# 5번
'''
import turtle
t = turtle.Turtle(shape="turtle")
t.lt(45)
t.fd(141)
t.up()
t.goto(0, 0)
t.down()
t.setheading(0)
t.fd(100)
t.lt(90)
t.fd(100)
'''
# 6번
'''
x1 = int(input("x1 : "))
y1 = int(input("y1 : "))
x2 = int(input("x2 : "))
y2 = int(input("y2 : "))
diff = ((x1-x2) ** 2 + (y1-y2) ** 2) ** 0.5
import turtle
t = turtle.Turtle(shape="turtle")
t.up()
t.goto(x1, y1)
t.down()
t.goto(x2, y2)
t.write(f"직선의 길이 = {diff}")
'''
# 7번
'''
import time
fsec = time.time()
fmin = fsec // 60
fhour = fmin // 60
hour = fhour % 24
min = fmin % 60
sec = fsec % 60
print("현재 시간(영국 그리니치 시각): %d시 %d분 %d초" % (hour, min, sec))
'''
# 8번
weight = float(input("물체의 무게를 입력하시오(Kg): "))
speed = float(input("물체의 속력을 입력하시오(m/s): "))
e = 1.0/2.0*weight*speed**2
print("물체는 %.1f (J)의 에너지를 가지고 있다." % (e))
