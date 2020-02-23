print("""
*************************************************
Kullanıcının girdiği sayının asal olup olmadığını
söyleyen program

Çıkmak için 'q' ya basınız
**************************************************
""")

def asal_mi(sayi):
    if(sayi==1):
        print("Asal değildir")
    elif(sayi==2):
        print("Asal Sayıdır")
    else:
        for i in range(2,sayi):
            if(sayi % i ==0):
                print("Asal değildir")
                return False
        return True

while True:
    sayı=input("Sayı:")
    if(sayı=="q"):
        break
    else:
        sayı=int(sayı)
        if(asal_mi(sayı)):
            print("Asaldır")

