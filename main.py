from funciones import gssjrdn

print("Ingrese los valores de la primera ecuación")
a1=float(input("Ingrese el valor para x_1:\n"))
a2=float(input("Ingrese el valor para x_2:\n"))
a3=float(input("Ingrese el valor para x_3:\n"))
d1=float(input("Ingrese el valor para c:\n"))

print("Ingrese los valores de la segunda ecuación")
b1=float(input("Ingrese el valor para x_1:\n"))
b2=float(input("Ingrese el valor para x_2:\n"))
b3=float(input("Ingrese el valor para x_3:\n"))
d2=float(input("Ingrese el valor para c:\n"))

print("Ingrese los valores de la tercera ecuación")
c1=float(input("Ingrese el valor para x_1:\n"))
c2=float(input("Ingrese el valor para x_2:\n"))
c3=float(input("Ingrese el valor para x_3:\n"))
d3=float(input("Ingrese el valor para c:\n"))



a=[[a1,a2,a3],[b1,b2,b3],[c1,c2,c3]]
b=[d1,d2,d3]


print("| ",a1,"x1 ",a2,"x2 ",a3,"x3 =",d1,"|")
print("| ",b1,"x1 ",b2,"x2 ",b3,"x3 =",d2,"|")
print("| ",c1,"x1 ",c2,"x2 ",c3,"x3 =",d3,"|" )

X,A = gssjrdn(a,b)
print("La solución es:")
print("x1=",X[0])
print("x2=",X[1])
print("x3=",X[2])
print("La tranformada [a]:")
print("| ",A[0][0]," ",A[0][1]," ",A[0][2],"|")
print("| ",A[1][0]," ",A[1][1]," ",A[1][2],"|")
print("| ",A[2][0]," ",A[2][1]," ",A[2][2],"|" )

"""
    aqui --> a=[[1,2,-1],[5,2,2],[-3,5,-1]]
        b=[2,0,1]
        X,A = gssjrdn(a,b)
        print("La solución es:")
        print(X)
        print("La tranformada [a]:")
        print(A)
"""    
