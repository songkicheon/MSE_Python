fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
a=input('좋아하는 과일은?')        #a에 사용자 입력 값을 저장한다
if a in fruit.values():      # fruit딕셔너리 발류 값에 a 가있으면 "정답입니다"출력 아니면 "오답입니다"출력
    print('"정답입니다"')
else:
    print('"오답입니다"')