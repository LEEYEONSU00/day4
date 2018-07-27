# 파일 읽기

# with는 파일 여는 시간을 확보하기 위함
with open('MYPAGE') as file:
    content1 = file.read() #인코딩 문제로 파일은 한글 말고 영어로

with open('MYPAGE') as file:
    content2 = file.readlines() #여러줄일때 리스트 형태로 저장됨

print(content1)
print(content2)

num = 1
for line in content2:
    print(str(num) + " : " + line)
    num = num+1