print("""
************************************
Bu program kullanıcının girdiği
2 basamaklı sayının okunuşunu söyler
Çıkmak için 'q' ya basınız
***************************************
""")


def okunuş_birler(birler):
    if(birler==1):
        return("bir")
    elif(birler==2):
        return("iki")
    elif(birler==3):
        return("üç")
    elif (birler == 4):
        return("dört")
    elif (birler == 5):
        return("beş")
    elif (birler == 6):
        return("altı")
    elif (birler == 7):
        return("yedi")
    elif (birler == 8):
        return("sekiz")
    else :
        return("dokuz")


def okunuş_onlar(onlar):
    if (onlar == 1):
        return "on"
    elif (onlar == 2):
        return ("yirmi")
    elif (onlar == 3):
        return("otoz")
    elif (onlar == 4):
        return("kırk")
    elif (onlar == 5):
        return("elli")
    elif (onlar == 6):
        return("altmış")
    elif (onlar == 7):
        return("yetmiş")
    elif (onlar == 8):
        return("seksen")
    else:
        return("doksan")



def okunuş(sayı):

    birler=sayı%10
    onlar=sayı//10
    print("birler:",birler)
    print("onlar",onlar)
    print("****************")
    print("{}---->{} {}".format(sayı,okunuş_onlar(onlar),okunuş_birler(birler)))
    okunuş_onlar(onlar)
    okunuş_birler(birler)



while True:
    girilen_sayı = input("Sayı:")
    if(girilen_sayı=="q"):
        break
    else:
        girilen_sayı=int(girilen_sayı)
    okunuş(girilen_sayı)