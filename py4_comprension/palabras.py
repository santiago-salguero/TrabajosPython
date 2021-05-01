A = ['Ceniza', 'Primaria','Ingenuo','Abrelatas','Avenida',    'Radio','Negro','Pedestal','Reventar','Asado']
n = len(A)

Pa = [(A[i]) for i in range(n) if ('a') in ((A[i])[-1])]
print('Las palabras terminadas en "a" son: ', Pa)