b=1
#i=1
lista =[]
numero = int(input('ingrese el numero a evaluar :'))
c = numero % 2 
if c == 0:
  lista.append(numero)
  #b=2
if b ==1:
  lista.append(numero)
  numero= numero *3 +1
  lista.append(numero)
while numero != 1: #i >0:
  numero=numero / 2
  lista.append(numero)
  #if numero == 1:
  #  i=0
  #else:
  #  i=1

#[6,3,10,5,16,8,4,2,1]




print("la lista de numero es :")
print(lista)