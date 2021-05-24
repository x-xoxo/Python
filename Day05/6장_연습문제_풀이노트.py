# 6장 딕셔너리, 튜플, 집합 연습문제
# 6.1
'''
(1) : 5000
(2) : {'김밥': 6000, '어묵': 3000, '떡볶이': 2000}
(3) : [6000, 3000, 2000]
(4) : ['김밥', '어묵', '떡볶이']
(5) : print("이 식당의 메뉴 개수는 %d개 입니다." % len(price))
'''
# 6.2
'''
(1) : price['순대'] = 4500
(2) : {'김밥': 6000, '어묵': 3000, '떡볶이': 2000, '순대': 4500}
(3) : print("순대의 가격은 %d원 입니다." % price['순대'])
(4) : print("이 식당의 메뉴 개수는 %d개 입니다." % len(price))
'''
# 6.3
# menu = {'Americano': 3000, 'Ice Americano': 3500, 'Cappuccino': 4000, 'Caffe Latte': 4500, 'Espresso': 3600}
# 1)
'''
for key, value in menu.items():
    print(f"{key}\t\t\t가격 : {value}원")
'''
# 2
'''
for key, value in menu.items():
    print(f"{key}\t\t\t가격 : {value}원")
select = input("위의 메뉴 중 하나를 선택하세요 : ")
if select in menu.keys():
    print(f"{select}는 {menu[select]}원 입니다. 결제를 부탁합니다.")
else:
    print(f"미안합니다. {select}는 메뉴에 없습니다.")
'''
# 6.4
'''
t = (10, 20, 30, 40)

t.append(50) -> 메소드 없음
t.remove(50) -> 메소드 없음
t[0] = 0 -> 대입 연산자 사용불가
'''
# 6.5
'''
t = (10, 20, 30, 40, 50, 60)
# t[0] => 10
# t[0:2] => 10, 20
# t[1:] => 20, 30, 40, 50, 60
# t[:3] => 10, 20, 30
# t[1::2] => 20, 40, 60
# t[::-1] => 60, 50, 40, 30, 20, 10
'''
# 6.6
'''
t1 = 'a', 'b', 'c'
t2 = ('a', 'b', 'c')
t3 = ('d', 'e')
# print(t1 == t2) => True

# print(t2 + t3) => ('a', 'b', 'c', 'd', 'e')

my_list = []
for e1 in t1:
    for e2 in t3:
        my_list.append(e1+e2)
# print(my_list) => ['ad', 'ae', 'bd', 'be', 'cd', 'ce']
'''
# 6.7
'''
sales = (100, 121, 120, 130, 140, 120, 122, 123, 190, 125)
day = 0
for i in range(len(sales)-1):
    if sales[i] > sales[i+1]:
        day += 1
print(f"일일 매출 기록 : {sales}")
print(f"지난 {len(sales)}일 동안 전일대비 매출이 감소한 날은 {day}일입니다.")
'''
# 6.8
'''
tup = (1, 2, 5, 4, 3, 2, 9, 1, 4, 7, 8, 9, 9)
dup = set()
for item in tup:
    if tup.count(item) > 1:
        dup.add(item)
print(f"주어진 튜플은: {tup}")
print(f"중복 원소는 {dup}")
'''
# 6.9
'''
tup = (1, 2, 5, 4, 3, 2, 1, 4, 7, 8, 9, 9, 3, 7, 3)
print(f"주어진 튜플: {tup}")
tup = tuple(set(tup))
print(f"중복 제거 튜플: {tup}")
'''
# 6.10
'''
tup = (1, 2, 5, 4, 3, 2, 1, 4, 7, 8, 9, 9, 3, 7, 3)
print(f"주어진 튜플은 {tup}")
tmp = sorted(list(tup))
max_count = 1
count = 1
cur_value = max_value = tmp[0]
for i in range(1, len(tmp)):
    if tmp[i] == cur_value:
        count += 1
        if count >= max_count:
            max_count = count
            max_value = cur_value
    else:
        cur_value = tmp[i]
        count = 1
print(f"가장 많이 나타나는 원소는 {max_value}")
'''
# 6.11
'''
li = [(), (1,), [], 'abc', (), (), (1,), ('a',), ('a', 'b'), ((),), '']
tmp = []
print(f"주어진 리스트는 {li}")
for i in li:
    if len(i) != 0:
        tmp.append(i)
print(f"빈 원소를 제거한 결과 : {tmp}")
'''
# 6.12
'''
li = [5, 6, 3, 9, 2, 12, 3, 8, 7]
print(f"주어진 리스트는 {li}")
for i in range(0, len(li)-1):
    if li[i] > li[i+1]:
        li[i], li[i+1] = li[i+1], li[i]
print(f"가장 큰 수를 마지막으로 옮긴 결과 : {li}")
'''
# 6.13
'''
li = [5, 6, 3, 9, 2, 12, 3, 8, 7]
print("강동욱")
print(f"정렬전 리스트 : {li}")
for i in range(0, len(li)-1):
    for j in range(0, len(li)-1-i):
        if li[j] > li[j+1]:
            li[j], li[j+1] = li[j+1], li[j]
print(f"정렬된 리스트 : {li}")
'''
# 6.14
'''
li = [5, 6, 3, 9, 2, 12, 3, 8, 7]
print("강동욱")
print(f"정렬전 리스트 : {li}")
for i in range(0, len(li)-1):  # 회전 수 또는 단계
    sw = True
    for j in range(0, len(li)-1-i):
        if li[j] > li[j+1]:
            li[j], li[j+1] = li[j+1], li[j]
            sw = False
    if sw:
        break
    print(f"{i+1}단계 : {li[:-(i+1)]}, {li[-(i+1):]}")
print(f"정렬된 리스트 : {li}")
'''
# 6.15
'''
print("강동욱")
tup = (4, 5, 2, 3, 8, 1, 9, 0)
for i in range(len(tup)):
    print(tup[:len(tup)-i])
'''
# 6.16
'''
print("강동욱")
student_tuple = (('191101', '홍길동', '010-123-45xx'),
                 ('191102', '임꺽정', '010-223-45xx'),
                 ('191103', '장길산', '010-323-45xx'))
student_dict = dict((num, name) for num, name, tel in student_tuple)
print("학생 정보 :", student_dict)
do = True
while do:
    id = input("학번을 입력하세요 : ")
    if id in student_dict.keys():
        print(f"{id}번 학생은 {student_dict[id]}입니다.")
    elif int(id) < 0:
        print("프로그램을 종료합니다.")
        do = False
    else:
        print("해당 학번의 학생이 없습니다.")
'''
# 6.17
'''
>>> s1 = set('abcd')
>>> s1
(1) {'a', 'b', 'c', 'd'}
>>> s2 = set('defg')
>>> s2
(2) {'g', 'f', 'd', 'e'}
>>> s1 == s2
(3) False
>>> s1 + s2
(4) TypeError
>>> s1 & s2
(5) {'d'}
'''
# 6.18
'''
>>> s1 = {0, 1, 2, 3, 4, 5}
>>> s2 = {3, 4, 5, 6, 7}
>>> s1 & s2
(1) {3, 4, 5}
>>> s1 | s2
(2) {0, 1, 2, 3, 4, 5, 6, 7}
>>> s2 - s1
(3) {6, 7}
>>> s1 - s2
(4) {0, 1, 2}
>>> s1 ^ s2
(5) {0, 1, 2, 6, 7}
>>> 2 in s1
(6) True
'''
# 6.19
'''
def is_palindrome(string):
    string = string.upper().replace(" ", "")
    return string == string[::-1]


string = "palindrome"
print(f"{string}은 회문입니다.") if is_palindrome(string) else print(f"{string}은 회문이 아닙니다.")
'''
# 6.20
# 1)
'''
scores = (('박동규', 88, 95, 90), ('강영민', 85, 90, 95), ('박동민', 70, 90, 80), ('홍승주', 90, 90, 95))

name, kor, math, science = zip(*scores)
print("학생들의 수학 성적의 평균은 : %.2f" % (sum(math)/len(math)))
'''
# 2)
'''
scores = (('박동규', 88, 95, 90), ('강영민', 85, 90, 95), ('박동민', 70, 90, 80), ('홍승주', 90, 90, 95))

name, kor, math, science = zip(*scores)
print("학생들의 수학과 과학 성적의 평균은 : %.2f" % ((sum(math)+sum(science))/(len(math)+len(science))))
'''
# 3)
'''
scores = (('박동규', 88, 95, 90), ('강영민', 85, 90, 95), ('박동민', 70, 90, 80), ('홍승주', 90, 90, 95))
student_dic = {}
for value in scores:
    avg = (value[1]+value[2]+value[3]) / 3
    student_dic[value[0]] = avg
print("이름       평균성적")
print("#################")
for k in student_dic.keys():
    print("%s   %9.2f" % (k, student_dic[k]))
'''
# 6.21



# 6.22