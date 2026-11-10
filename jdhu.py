y=0
x= 600851475143
for i in range(2,x+1):
    if x%1==0:
        z=0   
        for j in range(1,i+1):
            if i%j==0:
                z=z+1
if z==2:
    y=i
print(y)


        
     
