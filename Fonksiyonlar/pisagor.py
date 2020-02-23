print("""
********************************
Bu program 1'den 100' e kadar 
sayılardan pisagor üçgeni
oluşturanları ekrana yazdırır
********************************
""")
import math


def pisagor(i, j,k):
    if(i*i+j*j==k*k):
        print(i,j,k)


for i in range(1,100):
    for j in range(1,100):
        for k in range(1,100):
            pisagor(i,j,k)
