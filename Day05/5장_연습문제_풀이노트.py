# 5장 리스트 연습문제
# 5.1
'''
list_ex = [10, 20, 30, 40, 50, 60, 70]
high = 5
low = 3
list_ex[low]        -> 40
list_ex[low + 2]    -> 60
list_ex[high - low] -> 30
list_ex[low - high] -> 60
list_ex[-1]         -> 70
list_ex[-low]       -> 50
list_ex[2 * 3]      -> 70
list_ex[2] * 3      -> 90
list_ex[5 % 4]      -> 20
len(list_ex)        -> 7
'''
# 5.2
'''
spell = ['s', 'w', 'e', 'e', 't']
spell -> ['s', 'w', 'e', 'e', 't']
spell[3] = 'a'
spell -> ['s', 'w', 'e', 'a', 't']
spell[4] = 'r'
spell -> ['s', 'w', 'e', 'a', 'r']
spell * 2 -> ['s', 'w', 'e', 'a', 'r', 's', 'w', 'e', 'a', 'r']
'''

# 5.4
'''
a = [2, 3, 4, 5, 6]
rev_a = []
print("a = ", a)

for i in range(len(a)):
    rev_a.append(a.pop())
print("rev_a =", rev_a)
'''
# 5.5
'''
l1 = ['I like', 'I love']
l2 = ['fan cake.', 'kiwi juice.', 'espresso.']

for i in l1:
    for j in l2:
        print(i, j)
'''
# 5.6
'''
list1 = [2, 3, 4, 1, 32]
max(list1) -> 32

sum(list1) -> 42

list1.remove(32)

list1 -> [2, 3, 4, 1]

list1.reverse()
list1 -> [1, 4, 3, 2]

list1.sort()
list1 -> [1, 2, 3, 4]
'''
# 5.7
'''
n_list = [10, 20, 30, 50, 60]
total = 0
for i in n_list:
    total += i
print("리스트의 원소들 :", n_list)
print("리스트 원소들의 합 : %d" % total)
'''
# 5.8
'''
n_list = [10, 20, 30, 50, 60]
total = 1
for i in n_list:
    total *= i
print("리스트의 원소들 :", n_list)
print("리스트 원소들의 곱 : %d" % total)
'''
# 5.9
'''
n_list = [10, 20, 30, 50, 60]
max = n_list[0]
for i in n_list:
    if max < i:
        max = i
print("리스트의 원소들 :", n_list)
print("리스트 원소들중 최댓값 : %d" % max)
'''
# 5.10
'''
n_list = [10, 20, 30, 50, 60]
min = n_list[0]
for i in n_list:
    if min > i:
        min = i
print("리스트의 원소들 :", n_list)
print("리스트 원소들중 최솟값 : %d" % min)
'''
# 5.11
'''
s = input("5개의 수를 입력하시오 : ")
n_list = []
for i in s.split():
    n_list.append(int(i))
print("합 :", sum(n_list))
print("평균 :", sum(n_list)/len(n_list))
print("최댓값 :", max(n_list))
print("최솟값 :", min(n_list))
'''
# 5.12
'''
n = input("n을 입력하세요 : ")
s = input(n + "개의 수를 입력하세요 : ")
n_list = []
for i in s.split():
    n_list.append(int(i))
print("합 :", sum(n_list))
print("평균 :", sum(n_list)/len(n_list))
print("최댓값 :", max(n_list))
print("최솟값 :", min(n_list))
'''
# 5.13
'''
s = input("10개의 수를 입력하세요 : ")
n_list = []
for i in s.split():
    n_list.append(int(i))
avg = sum(n_list)/len(n_list)
print("합 :", sum(n_list))
print("평균 :", avg)

std = 0

for i in n_list:
    std += (i-avg) ** 2
std = (std / len(n_list)) ** 0.5
print("표준편차 : %.2f" % std)
'''
# 5.14
'''
spell = ['h', 'a', 'p', 'p', 'y', ' ', 'b', 'i', 'r', 't', 'h', 'd', 'a', 'y']

spell[1:5] -> ['a', 'p', 'p', 'y']

spell[:] -> ['h', 'a', 'p', 'p', 'y', ' ', 'b', 'i', 'r', 't', 'h', 'd', 'a', 'y']

spell[:5] -> ['h', 'a', 'p', 'p', 'y']

spell[6:] -> ['b', 'i', 'r', 't', 'h', 'd', 'a', 'y']

spell[:2] + spell[9:] -> ['h', 'a', 't', 'h', 'd', 'a', 'y']
'''
# 5.15
'''
greet = 'Have a beautiful day.'

greet[:4] -> 'Have'

greet[7:16] -> 'beautiful'

greet[17:20] -> 'day'
'''
# 5.16
'''
s = 'Birthday'
s[:5] -> Birth
s[5:] -> day
s[1:-1] -> irthda
s[::-1] -> yadhtriB
'day' in s -> True
'birth' in s -> False
'Birth' in s -> True
'Birth' not in s -> False
'''
# 5.17
# 1)
'''
animals = ['dog', 'cat', 'tiger', 'lion']
print("animals =", animals)
'''
# 2)
'''
animals = ['dog', 'cat', 'tiger', 'lion']
def shift(animals):
    temp = animals[0]
    for i in range(1, len(animals)):
        animals[i - 1] = animals[i]
    animals[len(animals) - 1] = temp
animals = ['dog', 'cat', 'tiger', 'lion']
print("이동 전 animals =", animals)
shift(animals)
print("이동 후 animals =", animals)
'''
# 3)
'''
animals = ['dog', 'cat', 'tiger', 'lion']

for i in animals:
    print(f"I love {i}.")
'''
# 5.18
# 1)
'''
s_list = ['abc', 'bcd', 'bcdefg', 'abba', 'cddc', 'opq']
min_len = len(s_list[0])
min_str = s_list[0]
for i in s_list:
    if min_len > len(i):
        min_len = len(i)
        min_str = i
print("가장 길이가 짧은 문자열 :", min_str)
'''
# 2)
'''
s_list = ['abc', 'bcd', 'bcdefg', 'abba', 'cddc', 'opq']
max_len = len(s_list[0])
max_str = s_list[0]
for i in s_list:
    if max_len < len(i):
        max_len = len(i)
        max_str = i
print("가장 길이가 긴 문자열 :", max_str)
'''
# 3)
'''
s_list = ['abc', 'bcd', 'bcdefg', 'abba', 'cddc', 'opq']
s_list.sort(key=len)
group_list = []
min_len = len(s_list[0])
for i in s_list:
    if len(i) == min_len:
        group_list.append(i)
print("가장 길이가 짧은 문자열 :", group_list)
'''
# 5.19
'''
s_list = ['abc', 'bcd', 'abc', 'abba', 'cddc', 'opq', 'opq']
new_s_list = []

for i in s_list:
    if i not in new_s_list:
        new_s_list.append(i)

print("s_list =", s_list)
print("new_s_list =", new_s_list)
'''