print('Ingrese el año deseado: ')
añ_us = int(input()) 

def bisiesto(año):
  c1 = año%4
  if (c1 == 0):
    c2 = año%100
    if (c2 == 0):
      c3 = año%400
    else:
      print('El año ', año,' no es bisiesto.')  
      if(c3 == 0):
        print('El año ', año,' es bisiesto.')
      else:
        print('El año ', año,' no es bisiesto.')
  else:
    print('El año ', año,' no es bisiesto.')

bisiesto(añ_us)