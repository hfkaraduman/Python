print("""
************************************************************************************************
Mükemmel Sayı Bulma
*Kendi Hariç Pozitif Bölenlerinin Toplamına Eşit Olan Sayılar Mükemmel Sayı Olarak Adlandırılırlar*
*Örneğin 6 sayısının bölenler (1,2,3) ve toplamları 6'dır"

**Bu program girilen sayının mükemmel sayı olup olmadığını söylemektedir**

**Programdan Çıkmak İçin 'q' ya Basın""
************************************************************************************************
""")

while True:
    sayi = (input("Sayı Giriniz:"))
    if(sayi=="q"):
        break
    else:
        toplam = 0

        sayi=int(sayi)
        for i in range(1,sayi):
            if(sayi%i == 0):
                toplam=toplam+i
        if(toplam == sayi):
            print("Girdiğiniz Sayı Mükemmel Sayıdır")

        else:
            print("Girilen Sayı Mükemmel Değildir")




