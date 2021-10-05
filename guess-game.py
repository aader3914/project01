import random
x=random.randint(1,50)

print(x)

for i in range(5):
  isOk = False
  while not isOk:
    try:
      y=int(input('猜數值(1-50)?'))
      if y<=50 and y>0:
        isOk = True
      else:
        print('輸入錯誤, 請輸入1~-50的數值')
    except:
      print('輸入錯誤, 請輸入1~-50的數值')


  if x==y:
    print('猜對了')
    break

  if x>y:
    print('再高一點')
  else:
     print('再低一點')   

