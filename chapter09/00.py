'''
score = int(input("점수 : "))

if (score >= 65):
    print("통과입니다.")
else:
    print("탈락입니다")
'''

# 주문 금액 5만원 이상 혹은 회원 일 경우 무료 배송

customer = input("고객 이름 : ")
amount = int(input("주문 금액 : ")) 
is_member = input("회원 여부 : ")

if amount >= 50000 or is_member:
    print (" 무료 배송 입니다. ")
else:
    print("배송비 3처넌 할인")
