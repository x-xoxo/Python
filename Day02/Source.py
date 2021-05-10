# Python Day 02
# Chapter 4
# Lab 'Say Hello to Turtle'
'''
import turtle
t = turtle.Turtle(shape='turtle')
s = turtle.textinput("", "이름을 입력하시오: ")
t.left(90)
t.fd(100)
t.write("안녕하세요? " + s + "씨, 터틀 인사드립니다.")
t.left(90)
t.fd(100)
t.write("안녕하세요? " + s + "씨, 터틀 인사드립니다.")
t.left(90)
t.fd(100)
t.write("안녕하세요? " + s + "씨, 터틀 인사드립니다.")
t.left(90)
t.fd(100)
t.write("안녕하세요? " + s + "씨, 터틀 인사드립니다.")
'''
# Lab 'Print Out Date'
'''
year = input("오늘의 연도를 입력하시오 : ")
month = input("오늘의 월을 입력하시오 : ")
day = input("오늘의 일을 입력하시오 : ")
print(f"오늘은 {year}년 {month}월 {day}일 입니다.")
print(f"오늘은 {month}/{day}/{year} 입니다.")
'''
# Lab 'Calc Age'
'''
import time

now = time.time()
thisYear = int(1970 + now//(365*24*3600))
print(f"올해는 {thisYear}입니다.")
curAge = int(input("몇 살이신지요?"))

print("2050년에는 "+str(curAge + 2050 - thisYear)+"살 이시군요.")
'''
# Lab 'Create Friend list'
'''
friendList = []
for i in range(5):
    friend = input("친구의 이름을 입력하시오 : ")
    friendList.append(friend)
'''
# Lab 'Paint Circle using list'
'''
import turtle
t = turtle.Turtle(shape='turtle')
color_list = ["yellow", "red", "blue", "green"]
t.fillcolor(color_list[0])
t.begin_fill()
t.circle(100)
t.end_fill()

t.fd(50)
t.fillcolor(color_list[1])
t.begin_fill()
t.circle(100)
t.end_fill()

t.fd(50)
t.fillcolor(color_list[2])
t.begin_fill()
t.circle(100)
t.end_fill()

t.fd(50)
t.fillcolor(color_list[3])
t.begin_fill()
t.circle(100)
t.end_fill()
'''
# Practice Question
# Q01
'''
print('나는 ' + str(12) + '개의 사과를 먹었다.')
'''
# Q02 다음과 같은 수식의 계산 결과는 ?
'''
'apple' + 'grape'
=> applegrape
'apple' * 3
=> appleappleapple
'''
# Q03
'''
s = input("문자열을 입력하시오 : ")
print(s[0:2] + s[-2:])
'''
# Q04
'''
s = input("문자열을 입력하시오 : ")
s += '하는 중'
print(s)
'''
# Q05
'''
symbol = input("기호를 입력하시오 : ")
word = input("중간에 삽입할 문자열을 입력하시오 : ")
s = symbol[:1]+word+symbol[1:]
print(s)
'''
# Q06
'''
list = [1,2,3,4]
sum = list[0]+list[1]+list[2]+list[3]
print('리스트 =', list)
print("리스트 숫자들의 합 =", sum)
'''
# Q07
'''
import turtle
t = turtle.Turtle(shape='turtle')
color_list = []
color = input("색상 #1을 입력하시오 : ")
color_list.append(color)
color = input("색상 #2을 입력하시오 : ")
color_list.append(color)
color = input("색상 #3을 입력하시오 : ")
color_list.append(color)

t.fillcolor(color_list[0])
t.begin_fill()
t.circle(50)
t.end_fill()

t.up()
t.fd(100)
t.down()
t.fillcolor(color_list[1])
t.begin_fill()
t.circle(50)
t.end_fill()

t.up()
t.fd(100)
t.down()
t.fillcolor(color_list[2])
t.begin_fill()
t.circle(50)
t.end_fill()
'''
# Q08
'''
import turtle
t = turtle.Turtle(shape='turtle')
list = []
list.append(int(input("x1 : ")))
list.append(int(input("y1 : ")))
list.append(int(input("x2 : ")))
list.append(int(input("y2 : ")))
list.append(int(input("x3 : ")))
list.append(int(input("y3 : ")))

t.goto(list[0], list[1])
t.goto(list[2], list[3])
t.goto(list[4], list[5])
'''
# Chapter 5
# Lab '영화 나이 제한 검사'
'''
age = int(input("나이를 입력하시오 : "))
if age >= 15:
    print("이 영화를 보실 수 있습니다.")
    print("영화의 가격은 10000원입니다.")
else:
    print("이 영화를 보실 수 없습니다.")
    print("다른 영화를 보시겠습니까?")
'''
# Lab '정수의 부호에 따라 거북이를 움직이자'
'''
import turtle
t = turtle.Turtle(shape='turtle')
t.up()
t.goto(100,100)
t.write("거북이가 여기로 오면 양수입니다.")
t.goto(100,0)
t.write("거북이가 여기로 오면 0입니다.")
t.goto(100,-100)
t.write("거북이가 여기로 오면 양수입니다.")

t.goto(0,0)
t.down()
s = turtle.textinput("", "숫자를 입력하시오 : ")
n = int(s)
if(n > 0):
    t.goto(100, 100)
if(n == 0):
    t.goto(100, 100)
if(n < 0):
    t.goto(100, -100)
'''
# Lab '거북이 제어하기'
'''
import turtle
t = turtle.Turtle(shape='turtle')
t.width(3)
t.shapesize(3, 3)

while True:
    cmd = input("명령을 입력하시오 : ")
    if cmd == "q" or cmd == "quit":
        break
    elif cmd == "l":
        t.left(90)
        t.fd(100)
    elif cmd == "r":
        t.right(90)
        t.fd(100)
    else:
        continue
'''
# Lab '윤년 판단'
'''
year = int(input("연도를 입력하시오 : "))
if( (year % 4 == 0 and year % 100 != 0) or year % 400 = 0):
    print(year, "년은 윤년입니다.")
else:
    print(year, "년은 윤년이 아닙니다.")
'''
# Lab '동전 던지기 게임'
'''
import random
print("동전 던지기 게임을 시작합니다.")
coin = random.randrange(2)
if coin == 0:
    print("앞면입니다.")
else:
    print("뒷면입니다.")
print("게임이 종료되었습니다.")
'''
# Usage for random
'''
import random
x = random.random()
print(f"random.random() : 0.0 <= {x} < 1.0")
x = random.uniform(1, 5)
print(f"random.uniform(1, 5) : 1.0 <= {x} <= 5.0")
x = random.randint(1, 100)
print(f"random.randint(1, 100) : 1 <= {x} <= 100")
x = random.randrange(0, 100, 3)
print(f"random.randrange(0, 100, 3) : 0 <= {x} < 100")
li = [0, 1]
x = random.choice(li)
print(f"random.choice(li) : {x}")
'''
# Lab '동전 던지기 게임(그래픽 버전)'
'''
import turtle
import random
screen = turtle.Screen()
image1 = "C:\\Users\\ehddn\\Python\\Day02\\front.GIF"
image2 = "C:\\Users\\ehddn\\Python\\Day02\\back.GIF"
screen.addshape(image1)
screen.addshape(image2)

t = turtle.Turtle()
coin = random.randint(0, 1)
if coin == 0:
    t.shape(image1)
    t.stamp()
else:
    t.shape(image2)
    t.stamp()
'''
# Lab '종달새가 노래할까?'
'''
import random
time = random.randint(1, 24)
print("좋은 아침입니다. 지금 시각은 " + str(time) + "시 입니다.")
sunny = random.choice([True, False])
if sunny:
    print("현재 날씨가 화창합니다. ")
else:
    print("현재 날씨가 화창하지 않습니다. ")

if (time >= 6 and time < 9) or (time >= 14 and time < 16) and sunny:
    print("종달새가 노래를 한다.")
else:
    print("종달새가 노래를 하지 않는다.")
'''
# Lab '로그인 프로그램'
'''
id = "ilovepython"
s = input("아이디를 입력하시오 : ")
if s == id:
    pw = "123456"
    pwinput = input("패스워드를 입력하시오 : ")
    if pw == pwinput:
        print("환영합니다.")
    else:
        print("비밀번호가 틀렷습니다.")
else:
    print("아이디를 찾을 수 없습니다.")
'''
# Lab '축구 게임'
'''
import random
options = ["좌단", "좌상단", "중앙", "우상단", "우단"]
ai_choice = random.choice(options)
user_choice = input("어디를 수비하시겠어요?(좌단, 좌상단, 중앙, 우상단, 우단) : ")
if ai_choice == user_choice:
    print("수비에 성공하셨습니다.")
else:
    print(f"페넉티 킥이 성공하였습니다. 들어간 지점 : {ai_choice}")
'''
# Lab '도형 그리기'
'''
import turtle
t = turtle.Turtle(shape='turtle')

s = turtle.textinput("", "도형을 입력하시오 : ")
if s == "사각형":
    s = turtle.textinput("", "가로 : ")
    width = int(s)
    s = turtle.textinput("", "세로 : ")
    height = int(s)
    t.fd(width)
    t.lt(90)
    t.fd(height)
    t.lt(90)
    t.fd(width)
    t.lt(90)
    t.fd(height)
elif s == "삼각형":
    s = turtle.textinput("", "밑변 : ")
    base = int(s)
    t.fd(base)
    t.lt(120)
    t.fd(base)
    t.lt(120)
    t.fd(base)
elif s == "원":
    s = turtle.textinput("", "반지름 : ")
    radius = int(s)
    t.circle(radius*2)
else:
    pass
'''
# Practice Question
# Q01 다음 프로그램의 출력은 무엇인가?
'''
age = 20
if age < 20:
    print("20살 미만")
else:
    print("20살 이상")
=> 20살 이상
'''
# Q02
'''
if age >= 30 and age < 50:
    print("30 이상 50 미만")
'''
# Q03
'''
temp = int(input("현재 온도를 입력하시오 : "))
if temp < 25:
    print("긴 바지를 입으세요")
else:
    print("반바지를 입으세요")
'''
# Q04
'''
score = int(input("성적을 입력하시오 : "))
if score >= 90:
    print("A학점입니다.")
elif score >= 80:
    print("B학점입니다.")
elif score >= 70:
    print("C학점입니다.")
elif score >= 60:
    print("D학점입니다.")
else:
    print("F학점입니다.")
'''
# Q05
'''
import random
x = random.randint(1, 100)
y = random.randint(1, 100)
ans = int(input(f"{x} - {y} = "))
if ans == x-y:
    print("맞았습니다.")
else:
    print("틀렸습니다.")
'''
# Q06
'''
n = int(input("정수를 입력하시오 : "))
if n % 2 == 0 and n % 3 == 0:
    print(f"{n}은(는) 2와 3으로 나누어 떨어집니다.")
else:
    print(f"{n}은(는) 2와 3으로 나누어 떨어지지 않습니다.")
'''
# Q07
'''
import random
solution = random.randint(0, 99)
cnt = 0
user = int(input("복권번호를 입력하시오(0에서 99사이) : "))
sol_digit1 = solution // 10
sol_digit2 = solution % 10
user_digit1 = user // 10
user_digit2 = user % 10
print(f"당첨번호는 {solution}입니다.")
if sol_digit1 == user_digit1:
    cnt += 1
if sol_digit2 == user_digit2:
    cnt += 1
if cnt == 0:
    print("상금은 없습니다.")
elif cnt == 1:
    print("상금은 50만원 입니다.")
elif cnt == 2:
    print("상금은 100만원 입니다.")
else:
    pass
'''
# Q08
'''
import turtle
t = turtle.Turtle(shape='turtle')
x1 = int(input("큰 원의 중심좌표 x1 : "))
y1 = int(input("큰 원의 중심좌표 y1 : "))
r1 = int(input("큰 원의 반지름 : "))
x2 = int(input("작은 원의 중심좌표 x2 : "))
y2 = int(input("작은 원의 중심좌표 y2 : "))
r2 = int(input("작은 원의 반지름 : "))

t.up()
t.goto(x1, y1)
t.down()
t.circle(r1)

t.up()
t.goto(x2, y2)
t.down()
t.circle(r2)


dist = ((x1-x2) ** 2 + (y1-y2) ** 2) ** 0.5
if dist <= abs(r1-r2):
    turtle.write("두번째 원이 첫번째 원 내부에 있습니다.")
elif dist <= r1+r2:
    turtle.write("두번째 원이 첫번째과 겹칩니다.")
else:
    turtle.write("두번째 원이 첫번째 원 외부에 있습니다.")
'''
