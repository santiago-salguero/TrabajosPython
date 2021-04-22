
archivo = open('palabras500.csv', encoding="utf-8")
lineas = archivo.readlines()
archivo.close

#print(len(lineas))
def rima(palabras): 
  for i in (palabras):
    if ('an') in (i[-3:-1]):
      print(i)
  return
  
rima(lineas)