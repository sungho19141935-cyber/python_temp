'''
score = int(input("숫자 :"))
print(f"{score}점은 통과인가? : {score >= 60}")


score = 90
if score >= 60:
    print ("통과입니다")
else:
    print("탈락입니다")


temperature = int(input("온도 :"))

if temperature >= 30:
    print("더워요!")
else:
    print("시원해요")
'''
'''
score = 85

if score >= 90:
    print("A")

elif score >= 80:
    print("B")

elif score >= 70:
    print("C")

else:
    print("D")

age = 25
if age >= 20 and age < 30:
    print("20대입니다.")
'''

order_amount = int(input("주문 금액 :"))
is_member = bool(input("멤버 인가요? :"))

if order_amount >= 50000 or is_member :
    print( " 무료배송 입니다.")
else:
    print( "배송비 3000원 입니다")