print("""
*************************************
Bu program kullanıcının girdiği
2 tane tamsayının 
ekokunu geriye döndürür
Çıkmak için 'q' ya basınız
**************************************
""")

def ekok(sayı1,sayı2):
    sayı1=int(sayı1)
    sayı2=int(sayı2)
    tambölen_sayı1=[]
    tambölen_sayı2=[]
    ekok=[]
    for i in range(1,sayı2+1):
        tambölen_sayı1.append(sayı1*i)
    for i in range(1,sayı1+1):
        tambölen_sayı2.append(sayı2*i)
    #print(tambölen_sayı1)
    #print("*************")
    #print(tambölen_sayı2)
    #print("**************")
    for i in range(len(tambölen_sayı1)):
        for j in range(len(tambölen_sayı2)):
            if(tambölen_sayı1[i]==tambölen_sayı2[j]):
                ekok.append(tambölen_sayı1[i])
    #print(ekok)
    if(ekok!=[]):
        print("EKOK({},{}:)".format(sayı1,sayı2),ekok[0])
    else:
        print(print("EKOK({},{}:)".format(sayı1,sayı2),sayı1*sayı2))



while True:
    birinci_sayı=(input("Birinci Sayı:"))
    ikinci_sayı=(input("İkinci Sayı:"))
    if(birinci_sayı=="q" or ikinci_sayı=="q"):
        break
    else:
        ekok(birinci_sayı,ikinci_sayı)
