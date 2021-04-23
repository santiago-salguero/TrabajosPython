print('Ingrese su peso en kg: ')
peso = int(input()) 

print('Ingrese su estatura en cm: ')
estatura = int(input()) 
estatura = estatura/100

def IMC(ps,est):
  imc = ps/(est**2)
  imc = round(imc, 2)
  print('Su índice de masa corporal es: ', imc) 

IMC(peso,estatura)