print("""
**Kullanıcının girdiği sayıları toplayan program**

*Çıkmak için 'q' ya basın*
Her bir while döngüsünde kullanıcıdan bir sayı alın ve kullanıcının girdiği sayıları "toplam" isimli bir değişkene ekleyin.
 Kullanıcı "q" tuşuna bastığı zaman döngüyü sonlandırın ve ekrana "toplam değişkenini" bastırın.

İpucu : while döngüsünü sonsuz koşulla başlatın ve kullanıcı q'ya basarsa döngüyü break ile sonlandırın.


""")
toplam=0
while True:
    sayi=(input("Sayı Giriniz:"))
    if(sayi=="q"):
        print("Sayıların Toplamları:{:.1f}".format(toplam))
        break
    else:
        sayi=float(sayi)
        toplam+=sayi
