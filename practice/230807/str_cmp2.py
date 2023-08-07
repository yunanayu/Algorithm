def itoa(a):
    s = ''
    while a > 0:
        # a % 10
        s += chr(ord('0') + a % 10) # 1의 자리 숫자의  ASCII 값
        a //= 10
    return s[::-1]

def atoi(str_value):
    value = 0
    for i in range(len(str_value)):
        c = ord(str_value[i]) - 0x30
        value = value * 10 + c
    return value





a = 123
print(itoa(a))

def itoa_1(int_value):
    return chr(int_value + 48)
t = itoa_1(256)
print(t, type(t))


def itoa_1(int_value):
    one = int_value % 10
    temp = int_value //10
    return chr(one + ord('0'))

def itoa(int_value):
    temp = int_value
    s = ''
    while temp > 0:
        one = temp % 10
        s = chr(one + ord('0')) + s
        temp = temp // 10
#-------------------------------------------------

t = itoa(2567)
print(t)=
