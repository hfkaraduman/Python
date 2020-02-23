print("""
*************************************
Bu program girilen sayının 
tam bölenlerini geriye döndürmektedir

Bir sayının bölenlerinin toplamı kendine eşitse bu sayı mükemmel bir sayıdır.
Örnek olarak 6 mükemmel bir sayıdır (1 + 2 + 3 = 6).
*************************************
Çıkmak için 'q' ya basınız
""")

def tam_bolenler(sayı):
    liste = []
    for i in range(1,sayı+1):
        if(sayı%i==0):
            liste.append(i)
    for i in liste:
        print(i)
while True:
    girilen_sayı=input("Sayı giriniz:")
    if(girilen_sayı=="q"):
        break
    else:
        girilen_sayı=int(girilen_sayı)
        tam_bolenler(girilen_sayı)