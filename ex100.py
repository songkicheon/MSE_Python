date=['09/05','09/06','09/07','09/08','09/09']
close_price=[10500,10300,10100,10800,11000]
close_table=dict(zip(date, close_price)) #zip은 각원소들이 순서에 맞게 쌍을이루게 하는 함수다
print(close_table)