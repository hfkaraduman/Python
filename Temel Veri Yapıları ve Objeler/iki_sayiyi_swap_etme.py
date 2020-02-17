# coding=utf-8
birinci_sayi=float(raw_input("1.Sayiyi giriniz:"))
ikinci_sayi=float(raw_input("2.Sayıyı giriniz:"))

print("1.Sayının degeri={}\n2.Sayının degeri={}\n".format(birinci_sayi,ikinci_sayi))
print("Sayılar swap edildikten sonraki degerleri;")
birinci_sayi,ikinci_sayi=ikinci_sayi,birinci_sayi
print("1.Sayının degeri={}\n2.Sayının degeri={}\n".format(birinci_sayi,ikinci_sayi))