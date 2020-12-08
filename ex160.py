리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']
for i in 리스트:
  a = i.split('.') #리스트안 원소 i를 '.' 기준으로 나누고 에이에 저장한다 예) ['intra', 'h']
  if (a[1] == 'h') or (a[1] == 'c'):  # a의 2번째 원소가 'h' 거나 'c'이면 i를 출력한다
    print(i)