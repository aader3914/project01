import random
x=random.randint(1,50)

print(x)

for i in range(5):
  y=int(input('猜數值(1-59)?'))

  if x==y:
    print('猜對了')
    break

  if x>y:
    print('再高一點')
  else:
     print('再低一點')   

