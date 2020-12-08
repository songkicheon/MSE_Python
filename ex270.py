class Stock:                        #268번 참고
    def __init__(self, name, code, per, pbr, dividend):
        self.name = name
        self.code = code
        self.per = per
        self.pbr = pbr
        self.dividend = dividend

    def set_name(self, name):
        self.name = name

    def set_code(self, code):
        self.code = code

    def get_name(self):
        return self.name

    def get_code(self):
        return self.code

    def set_per(self, per):
        self.per = per

    def set_pbr(self, pbr):
        self.pbr = pbr

    def set_dividend(self, dividend):
        self.dividend = dividend         #268번 참고

종목=[]	#종목이란 빈 리스트를 만듬
삼성 = Stock("삼성전자", "005930", 15.79, 1.33, 2.83) #Stock 클레스의 객체를 만듬
현대차 = Stock("현대차", "005380", 8.70, 0.35, 4.27)
LG전자 = Stock("LG전자", "066570", 317.34, 0.69, 1.37)
종목.append(삼성)	  #삼성이라는 변수가 가리키는 그 객체를 넣어준다
종목.append(현대차)
종목.append(LG전자)

for i in 종목: #i가 종목이라는 리스트안에 각각의 객체가 됨 예)i=삼성
	print(i.code,i.per)  #종목코드는 i.code로 접근 per은 i.per로 접근 (Stock클래스의 객체를 배정해서)
