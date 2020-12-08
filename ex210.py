def message1(): #message1()를 A를 출력하는 함수로 입력한다
    print("A")

def message2():  #message2()를 B를 출력하는 함수로 입력한다
    print("B")

def message3():        #message3()을 
    for i in range (3) : #3번 반복한다
        message2()       # B를 출력한다
        print("C")       # C를 출력한다
    message1()           # A를 출력한다

message3()             #(B를 출력하고 C를 출력하는것)을 3번 반복하고 A를 출력한다
#B
#C
#B
#C
#B
#C
#A