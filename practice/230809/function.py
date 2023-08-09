def func3():
    n = 3
    print(3)
    return
def func2():
    n = 2   #함수 안 지역변수들이 함수 상태를 유지시켜 줌
    func3()
    print(2)
    return

def func1():
    n = 1
    func2()
    print(1)
    return

n = 0
func1()