# 주석 단축키는 드래그 + ctrl + 슬래시(/)
# fruits = ['apple', 'banana', 'kiwi', 'watermelon']

# # for fruit in fruits:
# #     print(fruit + "가 있습니다.")

# index = 0
# while index < 4: # index <=3도 같은 결과
#     print(fruits[index] + "를 꺼냈습니다.")
#     index = index + 1

# count = len(fruits)
# print("과일의 갯수는:" , count)

# message = ''

# while message !='quit':
#     message = input("\ntyping you message: ")
#     print(">" + message)

# print("\n메시지가 더이상 없습니다.")

# message = ' '
# active = True

# while active:
#     if message == 'quit':
#         active = False # break 해도 빠져나감
#     else:
#         message = input("\ntyping you message: ")
#         print(">" + message)

# print("\n메시지가 더이상 없습니다.")

# num = 0
# while num < 10 :
#     num = num + 1
#     if(num%2==0):
#         continue # while 반복문에서 continu를 만나면 뒤에 있는거 실행 안함
#     print(num)

# 175p 연습문제

# add = ' '

# while add != 'quit':
#     add = input("어떤 피자 토핑을 추가하시겠어요?")
#     if add !='quit':
#             print(add, "을 추가하겠습니다.")
#     else:
#         break

# print("피자를 만들겠습니다.")

active = True


while active:
    ticket = input("몇 살 이신가요? ")
    ticket = int(ticket)
    if ticket < 3:
        print("영화 입장권은 무료입니다.")
    elif ticket <= 12:
        print("영화 입장권은 10달러입니다.")
    elif ticket <= 65:
        print("영화 입장권은 15달러입니다.")
    else:
        active = False

sandwich_orders = ['a', 'b','c', 'd', 'e']
finished_sandwiches = []
