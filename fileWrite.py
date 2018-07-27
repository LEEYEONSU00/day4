#파일에 쓰기

# 'w'로 쓰면 기존에 있던 내용이 사라짐
# 'a'로 쓰면 기존의 내용에 추가됨 list에서 append와 유사한 기능
with open('MYPAGE', 'a') as file:
    file.write('\nHappy Day')
    file.write('\toh my dog')


