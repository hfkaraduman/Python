# coding=utf-8
print("""""***************************
HESAP MAKİNESİ

1.İŞLEM ->TOPLAMA

2.İŞLEM ->ÇIKARMA

3.İŞLEM ->ÇARPMA

4.İŞLEM ->BÖLME

    ********************************"""
)
birinci_sayi=float(input("Birinci Sayıyı Giriniz:"))

ikinci_sayi=float(input("İkinci Sayıyı Giriniz"))

islem=input("İşleminizi Seçiniz:-->")


if islem == 1:
    print("{} + {} = {}".format(birinci_sayi,ikinci_sayi,birinci_sayi+ikinci_sayi))

elif islem==2:
    print("{} - {} = {}".format(birinci_sayi, ikinci_sayi, birinci_sayi - ikinci_sayi))

elif islem==3:
    print("{} * {} = {}".format(birinci_sayi, ikinci_sayi, birinci_sayi * ikinci_sayi))

elif islem==4:
    print("{} / {} = {}".format(birinci_sayi, ikinci_sayi, birinci_sayi / ikinci_sayi))

else :
    print("İşlem Seçimi Tanımlanmadı..!")