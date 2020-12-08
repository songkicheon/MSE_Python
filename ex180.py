low_prices  = [100, 200, 400, 800, 1000]
high_prices = [150, 300, 430, 880, 1000]
a=[]
b=range(0,5)
for i in b: #b가 0~4숫자를 가졌으므로 i에 0~4를넣고 high_prices[i]- low_prices[i]의 값을 a에 추가한다
    a.append(high_prices[i] - low_prices[i])
print(a)