
# 과제 — 상품 정보를 변수와 데이터형으로 표현하기

product_name = "파이썬 기초"
price = 28000
discount_rate = 0.15
is_on_sale = True
stock = 12

print(type(product_name))
print(type(price))
print(type(discount_rate))
print(type(is_on_sale))
print(type(stock))

price_text =str(price)
print(type(price_text))

product_name = int("파이썬")
print (type(product_name))
#ValueError: invalid literal for int() with base 10: '파이썬'