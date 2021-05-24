# Lab 편의점 재고 관리
'''
items = {"커피음료": 7, "펜": 3, "종이컵": 2, "우유": 1, "콜라": 4, "책": 5}
while True:
    print("### 재고 현황 ###")

    for key in sorted(items.keys()):
        print(key, items[key])

    print("\n************************")
    print("0. 종료")
    print("1. 재고 추가")
    print("2. 재고 삭제")
    print("************************")
    menu = int(input())
    if menu == 1:
        prod_name = input("어떤 물풀을 추가 하시겠습니까?")
        if prod_name in items.keys():
            add_amount = int(input("몇 개 추가 하시겠습니까?"))
            items[prod_name] += add_amount
            continue
        print("물품을 찾을 수 없습니다.")
    elif menu == 2:
        prod_name = input("어떤 물풀을 삭제 하시겠습니까?")
        if prod_name in items.keys():
            sub_amount = int(input("몇 개 삭제 하시겠습니까?"))
            if items[prod_name]-sub_amount < 0:
                print("잘못된 수량입니다.")
            else:
                items[prod_name] -= sub_amount
            continue
        print("물품을 찾을 수 없습니다.")
    else:
        print("종료합니다.")
        break
'''
# Lab 이메일 보내기
'''
import smtplib
from email.mime.text import MIMEText

me = "abc@server.kr"
you = "temp@example.com"
contents = "12월 20일에 동창회가 있으니 참석해주시기 바랍니다."
msg = MIMEText(contents, _charset="euc-kr")
msg['Subject'] = "동창회 모임"
msg['From'] = me
msg['To'] = you

server = smtplib.SMTP("smtp@gmail.com", 587)
server.ehlo()
server.starttls()
server.ehlo()

server.login("아이디", "패스워드")

server.sendmail(me, you, msg.as_string())
server.quit()
'''
# 연습문제
# Q01
'''
list = []
sum = 0

for i in range(5):
    i = int(input("정수를 입력하시오 : "))
    list.append(i)

for i in list:
    sum += i

avg = sum / len(list)

print("평균 = %.2f" % avg)
'''
# Q02
'''
import random

counters = [0, 0, 0, 0, 0, 0]
for i in range(1000):
    value = random.randint(0, 5)
    counters[value] += 1

for i in range(6):
    print(f"주사위가 {i+1}인 경우는 {counters[i]}")
'''
# Q03
'''
contacts = {}

while True:
    name = input("(입력모드)이름을 입력하시오 : ")
    if not name:
        break
    tel = input("전화번호를 입력하시오 : ")
    contacts[name] = tel

while True:
    name = input("(검색모드)이름을 입력하시오 : ")
    if not name:
        break
    if name in contacts.keys():
        print(f"{name}의 전화번호는 {contacts[name]} 입니다.")
    else:
        print("이름을 찾지 못했습니다.")
'''
# Q07
'''
domains = {"kr": "대한민국", "sk": "슬로바키아", "no": "노르웨이", "us": "미국", "jp": "일본", "hu": "헝가리", "de": "독일"}

for k, v in domains.items():
    print(f"{k} : {v}")
'''
# Q08
'''
problems = {'파이썬': '최근에 가장 떠오르는 프로그래밍 언어',
            '변수': '데이터를 저장하는 메모리 공간',
            '함수': '작업을 수행하는 문장들의 집합에 이름을 붙인것',
            '리스트': '서로 관련이 없는 항목들의 모임'}

def show_words(problems):
    display_message = ""
    i = 1
    for word in problems.keys():
        display_message += '('+str(i)+')'
        display_message += word + " "
        i += 1
    print(display_message)


for value in problems.values():
    print("다음은 어떤 단어에 대한 설명일까요? ")
    print(f"\"{value}\"")
    correct = False
    while not correct:
        show_words(problems)
        guessed_word = input("")
        if problems[guessed_word] == value:
            print("정답입니다!")
            correct = True
        else:
            print("정답이 아닙니다.")
'''