import requests
btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']
시가=float(btc['opening_price']) #opening_price 발류값을 시가에 실수로 저장
최고가=float(btc['max_price'])    #max_price 발류값을 시가에 실수로 저장
변동폭=float(btc['max_price'])-float(btc['min_price'])   #max_price 발류값을 시가에 실수로 저장한거에 min_price 발류값을 시가에 실수로 저장한 값을 뺀다
if (시가+변동폭)> 최고가:  #시가+변동폭이 최고가 보다 크면 상승장 출력 아니면 하락장 출력
    print('상승장')
else:
    print('하락장')