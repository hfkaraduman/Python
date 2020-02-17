# coding=utf-8
#Kullanıcı tarafından girilen 3 tane sayıdan en büyüğünü bulma
print("""********************
3 Sayıdan En Büyüğünü Bulma
""")
birinci_sayi=float(raw_input("Birinci Sayıyı Giriniz:"))
ikinci_sayi=float(raw_input("İkinci Sayıyı Giriniz:"))
ucuncu_sayi=float(raw_input("Üçüncü Sayıyı Giriniz:"))

if birinci_sayi>ikinci_sayi and birinci_sayi>ucuncu_sayi:
    print("En büyük sayı :{:.0f}".format(birinci_sayi))
elif ikinci_sayi>birinci_sayi and ikinci_sayi>ucuncu_sayi:
    print ("En büyük sayı :{:.0f}".format(ikinci_sayi))
else :
    print ("En büyük sayı :{:.0f}".format(ucuncu_sayi))