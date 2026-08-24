# set을 쓰지말고 list 기능만 써서 unique_tags를 구현하시오

# 의사코드 작성해줘
'''
AI 프롬프트 
tags = ["Python", "AI", "Python", "Data", "AI"]
tags 안에 중복 된 값이 있잖아 내가 unique_tags를 출력을 했을 때 중복된 값이 나오지 않도록 출력을 해야 해 
코드는 내가 직접 짤거야 약간의 힌트만 부탁할게
'''

tags = ["Python", "AI", "Python", "Data", "AI"]

unique_tags =[]
for tag in tags:
    if tag not in unique_tags:
        unique_tags.append(tag)
print(unique_tags)