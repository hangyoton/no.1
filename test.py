
  #練習問題7.1         #分散、標準偏差もやってみました。
import random  

a=[]
n=5
for i in range(n):
    a.append(random.randint(1,100))
print(a)    
#この続きを書いてください。
s=0;t=0
for i in range(len(a)):
  s=s+a[i]
  t=t+a[i]**2
m=s/n
bunsan=t/n-m**2
hyouzyunn=bunsan**(1/2)
print("合計は",s,"平均は",m,"です""分散は",bunsan,"です""標準偏差は",hyouzyunn,"です")