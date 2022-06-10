import numpy as np      ##Importante 

arreglo = np.array([1, 2, 3, 4])
print(arreglo)

#Ver dimensiones arreglo
print(arreglo.ndim)

#Cantidad elementos 
print(len(arreglo))


c = [i for i in range(0,20)]
arreglo2 = np.array(c)

for x in range(len(c)):
    print(c[x])

