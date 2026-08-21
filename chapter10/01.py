'''
word ="안녕하세요 저는 파이썬을 공부하고 있어요"
number = 1
for char in word:
    print(f"{number}번째 문자:{char}")
    number+=1

    for number in range(1, 6):
    total = 0
    total += number
    print(total)
'''

for number in range(1, 100):
    if number % 2 == 0:
        print(f"{number}는 짝수입니다.")

count = 1
while count <= 10:
    print(count)
    count += 1
