x=[]
y=0
num=[x]
c=0
b=0
x=int(input("Cuantos integrantes son en tu grupo?:"))
for i in range(x):
    n=float(input("Cual es su promedio?: "))
    num.append(n)
    c=n+c
    b+=1
    if n>=70:
        y+=1
print(f"Esta cantidad pasó: {y}")
b=c/b
print(f"Este es el promedio: {b}")



