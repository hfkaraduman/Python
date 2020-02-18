print("""
**************************
ATM Makenesine Hoşgeldiniz

İşlemler;

1.Bakiye Sorgulama

2.Para Yatırma

3.Para Çekme

Programdan Çıkmak İçin 'q' ya basın
**************************
""")

bakiye=1000

while True:
    islem=input("İşlemi Seçiniz:")

    if (islem=="q"):
        print("Hoşçakalın...")
        break
    elif (islem=="1"):
        print("Bakiyeniz {} tl'dir".format(bakiye))
    elif (islem =="2"):
        miktar=int(input("Miktarı Giriniz:"))
        bakiye+=miktar
    elif (islem=="3"):
        miktar = int(input("Miktarı Giriniz:"))
        if(bakiye-miktar<0):
            print("Bakiyeniz girdiğiniz miktardan yetersiz.")
            continue
        bakiye-=miktar
