A = [1,3,5,3]
B = [1,6,2,7]
C = [7,2,1,5]

n = len(B)

print(sum (((A[i]*B[i])+C[i]) for i in range (n))/(n**2))
