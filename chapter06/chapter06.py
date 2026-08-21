# chapter 06 나의 생활 계산기 만들기 

# 카페 주문 금액
coffee_price = 4500
coffee_quantity = 3

cake_price = 6500
cake_quantity = 2

total_price = (coffee_price * coffee_quantity) + (cake_price * cake_quantity)
print("총 결제 금액:",(str(total_price) + "원"))

#학습 시간 변환
total_minutes = 385
hours = total_minutes //60
minutes = total_minutes % 60
print(hours, "시간")
print(minutes, "분")

# 직사각형 계산
'''
나는 파이썬을 공부하고 있는  초보자야
지금 파이썬을 사용해서 직사각형을  계산하려 해
width = 12
height = 8
조건은  
- 넓이를 계산해야 함
- 넓이가 100보다 큰지 비교해야 함
- width += 3  적용
- 새 넓이를 다시 계산 해야 함
코드를 짜주진 말고 초보자가 직접 실행해보면서 체득할 수 있게 약간의 힌트를 주면서 알려줘
/ELI10
'''
width = 12
height = 8

area = (width * height)
print("처음 넓이" , area )

print ( "100보다 큰가요?" , area >= 100) 

width += 3

area =  width * height
print( "새로운 넓이" , area)
