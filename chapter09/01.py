'''
score = int(input("숫자 : "))

print(f"{score}는 60보다 크거나 같은가 : {score >= 60}")



number = int(input("숫자를 입력 하세요 : "))
if number >= 0:
    print (" 양수입니다 ")

else:
    print (" 음수입니다 ")


score = int(input("성적 :"))
if score >= 90:
    print ("A")
elif score >= 80:
    print ("B")
elif score >= 70:
    print(" C ")
elif score >= 60:
    print("D")
else:
    print ("F")
    '''

age = int(input("나이를 입력하세요 :"))
has_money = int(input("가지고 있는 돈 :"))

if age <=7:
    print ("무료 입장")
elif age <=12 and has_money >=5000:
    print ("입장 가능 합니다 입장료: 5000원")
elif age<= 18 and has_money >= 8000:
    print("입장 가능 합니다 입장료: 8000원")
elif age >=19 and has_money >= 12000:
    print("입장 가능 합니다 입장료: 12000원")
else:
    print ("입장이 불가 합니다")
  