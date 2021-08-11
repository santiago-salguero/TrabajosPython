import matplotlib.pyplot as plt
a = int(input())
li = []
while a!=1:
  b = a%2
  if b==0:
    a = a/2
  else:
    a = (a*3)+1
  li.append(a)
print(li)
plt.plot(li)
plt.show()