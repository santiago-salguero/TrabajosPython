def llenarLi(a,b):
  n = len(a)//2
  li3=[]
  for i in range(n):
    c_a = (a[i+1])**2
    m_ab = c_a*(b[2*i])
    sum_bi = m_ab+(b[n+i])
    li3.append(sum_bi)
  return li3

li1 = [2,5,4,6]
li2 = [3,8,9,2]

print('Para llenar la lista "li3" usaremos: ')
print(li1,li2)
print('Tiene como resultado: ',llenarLi(li1,li2))

##Prueba de escritorio
print('Prueba de escritorio: ',[((5**2)*3)+(9),(((4**2)*9)+(2))])

