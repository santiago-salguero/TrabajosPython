import random
random.seed()
l = random.randint(1,10) #Intervalo
a = random.randint(5,55) #Numero inicial
b = random.randint(55,90) #Numero final
total=0
for i in range(a,b,l):
  total = i+total
  print(i)
print('La sumatoria del listado es: ',total)