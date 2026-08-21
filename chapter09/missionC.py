# 간단한 로그인 판정

saved_id = "python"
saved_password = 1234
user_id = input('아이디 : ')
user_password = int(input("비밀번호 :"))

if user_id == saved_id and user_password == saved_password:
    print( "로그인 성공")
else:
    print("아이디와 비밀번호를 확인하세요")    