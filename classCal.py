#class의 상속

class Cal():
    def __init__(self, value):
        self.value = value # 계산기 맨 처음에 입력되어있는 값 ex) 0

    def result(self):
        print(self.value)
    
    def add(self, input_value):
        self.value += input_value
    
    def sub(self, input_value):
        self.value -= input_value

    def mul(self, input_value):
        self.value *= input_value

    def div(self, input_value):
        #self.value /= input_value # 0으로 나누면 에러남
        try:
            self.value /= int(input_value) # 오류가 일어날 가능성이 있는 구문
        except ZeroDivisionError:
            print("0으로 나눌 수 없습니다.")
        else:# ZeroDivisionError이 아닌 에러가 났을때 else로 옴
            print("알 수 없는 에러입니다.")
        
    
class SafeCal(Cal): # 부모 클래스 상속 받음
    def __init__(self, value):
        self.value = value
    def div(self, input_value): # 부모 클래스와 똑같은 이름으로 함수 정의-> 오버라이딩
        if(input_value == 0):
            self.value = 0 #나누기를 하지 않고 현재 값을 0으로 해준다.
        else:
            self.value /= input_value

cal1 = Cal(10)
cal2 = SafeCal(0)

num1 = input("숫자를 입력해 주세요: ")
# num1 = int(num1)
# # cal1.add(num1)
# cal1.result()
# cal1.sub(num1)
# cal1.result()
# cal1.mul(num1)
# cal1.result()
cal1.div(num1)
#cal1.result()