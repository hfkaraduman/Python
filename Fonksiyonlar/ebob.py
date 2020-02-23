print("""
*************************************
Bu program kullanıcının girdiği
2 tane tamsayının 
ebobunu geriye döndürür
Çıkmak için 'q' ya basınız
**************************************
""")


def tam_bolenler(sayı):
    liste = []
    for i in range(1, sayı + 1):
        if (sayı % i == 0):
            liste.append(i)

    return liste

def ebob(sayı1,sayı2):
    liste1=tam_bolenler(sayı1)
    liste2=tam_bolenler(sayı2)
    #print(liste1[0:len(liste1)])
    #print(liste2[0:len(liste2)])
    #print(len(liste1))
    #print(len(liste2))
    ortakliste=[]
    for i in range(len(liste1)):
        for j in range(len(liste2)):
            if(liste1[i]==liste2[j]):
                ortakliste.append(liste1[i])
    #print(ortakliste)
    print("EBOB ({},{}) :".format(sayı1,sayı2),ortakliste[-1])

while True:
    birinci_sayı=(input("Birinci Sayı:"))
    ikinci_sayı=(input("İkinci Sayı:"))
    if(birinci_sayı=="q" or ikinci_sayı=="q"):
        break
    else:
        birinci_sayı=int(birinci_sayı)
        ikinci_sayı=int(ikinci_sayı)
        ebob(birinci_sayı,ikinci_sayı)