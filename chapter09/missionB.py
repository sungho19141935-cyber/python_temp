# 쇼핑 할인 프로그램

order_amount = int(input("주문금액 : "))

if order_amount >= 1000000:
    print(" 10% 할인 안내")
elif order_amount >= 50000:
    print(" 5% 할인 안내")
else:
    print ("할인 없음")