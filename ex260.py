class OMG : 
    def print() :#괄호안에 self 가 들어가야 한다
        print("Oh my god")
myStock = OMG()
myStock.print() #print()는 인자가 없는데 myStock.print()를 실행하면 파이썬에서는 OMG.print(mystock)라고 
#인지하기 때문에 에러가 발생한다 그러므로 위에 print()를 print(self)로 바꿔야한다.