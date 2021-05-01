A = [2,3,4,5]
B = [3,1,8,6]

n = len(A)//2

C = [((A[i+1]**2)*B[2*i])+B[n+i] for i in range(n)] 
print('La lista generada por las listas: ',A,B,'\nes:',C)