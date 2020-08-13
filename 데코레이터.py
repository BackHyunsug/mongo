
#데코레이터 
def mydecorator(callfunc): 
    def func(a, b):
        print("------ 중간에서 함수 가로채기 ----------------")
        callfunc(a,b)          
        print("---------------------------------------------")
    return func # return  구문에서 내부함수를 반드시 반환하자 

@mydecorator 
def myfunc(a,b):
    print(a,b)
    

myfunc(4,5)

import datetime

def work():
    print("현재시간 ",  datetime.datetime.now())
    for i in range(1, 1000000):
        pass 
    print("종료시간 ",  datetime.datetime.now())

def work2():
    print("현재시간 ",  datetime.datetime.now())
    for i in range(1, 3000000):
        pass 
    print("종료시간 ",  datetime.datetime.now())

work()
work2()

#데코레이터로 사용되는 함수는 매개변수가 함수이어야 한다 
def now_time(callfunc):
    #함수안에 내부 함수를 만든다. 그리고 반드시 내부함수를 반환해야 한다 
    def inner_func():
        print("현재시간 ",  datetime.datetime.now())
        callfunc() #  매개변수로 받아온 함수를 호출한다 
        print("종료시간 ",  datetime.datetime.now())

    return inner_func #now_time 이 내부함수를 외부로 반환한다 

@now_time
def work3():
    for i in range(1, 6000000):
        pass
    print(i)

work3()










