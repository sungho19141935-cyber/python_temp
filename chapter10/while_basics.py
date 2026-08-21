'''
count =1 
while count <=3:
    print(f"현재 count:{count}")
    count+=1
print("종료")


for row in range(3):
    for column in range(4):
        print("*", end="")
    print()
'''

result = 0 
for i in [1,10]:
    result = result + i
    print(result)