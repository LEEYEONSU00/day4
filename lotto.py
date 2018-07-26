import random

# 로또 번호는 1~46, 총 6개의 당첨 번호

today = []

# 1부터 46까지 1씩 단위로 숫자가 들어감
# 리스트에 숫자가 들어가 있어야 today[0] = random.randrange(1,46,1) 가능
# today.append(random.randrange(1,46,1))
# today.append(random.randrange(1,46,1))
# today.append(random.randrange(1,46,1))
# today.append(random.randrange(1,46,1))
# today.append(random.randrange(1,46,1))
# today.append(random.randrange(1,46,1))

#반복문으로 바꾸기
# start = 0
# while start <6:
#     today.append(random.randrange(1,46,1))
#     start = start+1

ran_num = random.randrange(1,47,1)

for i in range(1,7):
    while ran_num in today:
        ran_num = random.randrange(1,47,1)
    today.append(ran_num)

# #random.sample 예제
# today = [i for i in range(1,47)] # today = random.sample(range(1,47),6)
# ran_num = random.sample(today,6)
# print(ran_num)

print("오늘의 추천번호는 " , today[0] , today[1] , today[2] , today[3] , today[4] ,today[5] , "입니다.")
