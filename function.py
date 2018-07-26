def hello(name='kim', age='10'):
    print("Hello, "  + name)
    print(age + "years old")



name = input("What is your name? ")
age = input("how old are you? ")
hello(name, age )
hello(name) # 매개변수 2번째값에 초기값 설정해주면 오류나지 않음. ex) age= 10
hello()
hello(age = '30', name = 'Jay')