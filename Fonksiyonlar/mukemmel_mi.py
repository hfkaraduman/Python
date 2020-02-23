print("""
********************************
Bu program 1'den 1000'e kadar sayılardan
mükemmel olanları geriye döndürür
**********************************
""")

def tam_bolenler(sayı):
    liste = []
    for i in range(1,sayı):
        if(sayı%i==0):
            liste.append(i)
#    print(liste)
    toplam=0
    for i in liste:
        toplam+=i
    if(sayı==toplam):
        print(sayı)
""""for i in liste:
      print(i)"""



def mükemmel_mi():
    for i in range(1,1000):
        tam_bolenler(i)

mükemmel_mi()



