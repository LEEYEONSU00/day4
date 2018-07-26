'''
name = input("What is your Name? ")
print("Hello, "+name)



num1 = input("First Number : ")
num2 = input("Second Number : ")
num1 = int(num1)
num2 = int(num2)
print("더하기 >")
print(num1+num2)
print("빼기 >")
print(num1-num2)
print("곱하기 >")
print(num1*num2)
print("나누기 >")
print(num1/num2)
print("나머지 >")
print(num1%num2)

if(num1%2 == 0):
    print("even")
else:
    print("odd")


#167p 연습문제

rentcar = input("어떤 종류의 렌터카를 원하시나요?")
print(rentcar + "스바루를 찾아보겠습니다.")


resevation_num = input("저녁 식사에 몇명이 오시나요?")
resevation_num = int(resevation_num)

if resevation_num >= 9 :
    print("9명 이상이면 자리가 날 때까지 기다려야 합니다.")
else:
    print("테이블이 준비되어 있습니다.")
'''

num = input("숫자를 입력하세요. ")
num = int(num)

if num&10 == 0:
    print("10의 배수입니다.")
else:
    print("10의 배수가 아닙니다.")