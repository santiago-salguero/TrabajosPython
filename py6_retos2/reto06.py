import random
random.seed()
n = random.randint(1,121)
if n<=10:
  print('El número ', n, ' es menor de 10')
elif n<=50:
    print('El número ', n, ' esta en un intervalo de 10 a 50')
elif(n<=100):
    print('El número ', n, ' esta en un intervalo de 50 a 100')
else:
    print('El número ', n, ' es mayor a 100')