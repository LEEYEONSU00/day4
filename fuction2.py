# def sum(num1, num2):
#     print("입력받은 숫자 2개", num1, num2)
#     return num1+num2


# num1 = 10
# num2 = 20

# result = sum(1,2) + sum(num1, num2) #함수의 합도 가능
# print(result)

def cart(fruits):
    print("장바구니 안에 다음과 같은 과일이 있습니다.")
    for fruit in fruits:
            print(fruit)

fruits = [ 'apple', 'kiwi', 'grape', 'peach']
cart(fruits)