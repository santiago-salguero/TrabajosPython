def sumatoria_li(a,b,c):
  n = len(a)
  suma = 0
  for i in range(n):
    mult = a[i]*b[i]
    res = mult + c[i]
    suma = suma+res
  suma = suma+(n**2)
  return suma

l1 = [1,3,4]
l2 = [7,4,2]
l3 = [2,3,5]

print('La sumatoria realizada con las listas: ')
print(l1,l2,l3, '/n')
print('Tiene como resultado: ',sumatoria_li(l1,l2,l3))

##Prueba de escritorio
print('Pruba de escritorio: ',(((1*7)+2)+((3*4)+3)+((4*2)+5))+3**2)