print("""
************************************************************************************************
Armstrong Sayı Bulma

**Bu program girilen sayının armstrong sayı olup olmadığını söylemektedir**
**Örnek olarak, Bir sayı eğer 4 basamaklı ise ve oluşturan rakamlardan herbirinin 4. kuvvetinin toplamı( 3 basamaklı sayılar için 3.kuvveti )
 o sayıya eşitse bu sayıya "Armstrong" sayısı denir.**

**Örnek olarak : 1634 = 1^4 + 6^4 + 3^4 + 4^4

**Programdan Çıkmak İçin 'q' ya Basın""
************************************************************************************************
""")

while True:
    sayi = (input("Sayı Giriniz:"))
    if(sayi=="q"):
        break
    else:
        basamak = 0
        for i in sayi:
          if(i=="0" or i=="1" or i=="2" or i=="3" or i=="4" or i=="5" or i=="6" or i=="7" or i=="8" or i=="9"):
              basamak+=1
        print("Basamak Sayısı:",basamak)

        toplam=0
        for i in sayi:
            print(i)
            i=int(i)
            toplam=toplam+i**basamak
        sayi=int(sayi)
        if(sayi==toplam):
            print("Girilen Sayı Armstrong Sayıdır ")
        else:
            print("Girilen Sayı Armstrong Sayı Değildir ")

        




