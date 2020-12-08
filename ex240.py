def 함수0(num) :
    return num * 2

def 함수1(num) :
    return 함수0(num + 2)

def 함수2(num) :
    num = num + 10
    return 함수1(num)

c = 함수2(2) #함수2(2)는 함수1(12)로 리턴되고 함수1(12)는 함수0(14)로 리턴되고 함수0(14)는 28로 리턴된다
print(c) #그래서 c의 값은 28이다