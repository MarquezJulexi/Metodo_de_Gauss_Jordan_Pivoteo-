import numpy as np

def gssjrdn(a,b):
    a = np.array(a, float)##te crea un array de tipo numpy con datos float
    b = np.array(b, float) ##te crea un array de tipo numpy con datos float
    n = len (b) #len retorna el numero de elementos del array

    #LOOP
    for k in range(n):
        #Pivote parcial 0,0 1
        if np.fabs (a[k,k]) < 1.0e-12:
            for i in range (k+1,n):
                if np.fabs(a[i,j]) > np.fabs(a[k,k]):
                    for j in range (k,n):
                        a[k,j], a[i,j],a[k,j]
                        b[k], b[i]=b[i], b[k]
                        break
        #División Pivote
        pivot =a[k,k]
        for j in range (k,n):
            a[k,j] /= pivot
            b[k] /= pivot
        #Eliminación
        for i in range(n):
            if i == k or a [i,k] ==  0: continue
            factor = a[i,k]
            for j in range (k,n):
                a[i,j] -= factor * a[k,j]
                b[i] -=factor * b[k]
    return b,a
"""
    aqui --> a=[[1,2,-1],[5,2,2],[-3,5,-1]]
        b=[2,0,1]
        X,A = gssjrdn(a,b)
        print("La solución es:")
        print(X)
        print("La tranformada [a]:")
        print(A)
"""    




            