import random
import time

class Kumanda():


    def __init__(self,tv_durum="Kapalı",tv_ses=0,kanal_listesi=["Trt"],kanal="Trt"):
        self.tv_durum=tv_durum
        self.tv_ses=tv_ses
        self.kanal_listesi=kanal_listesi
        self.kanal=kanal
    def tv_aç(self):
        if(self.tv_durum=="Açık"):
            print("Televizyon Zaten Açık")
        else:
            print("Televizyon Açılıyor")
            self.tv_durum="Açık"
    def tv_kapat(self):
        if(self.tv_durum=="Kapalı"):
            print("Televizyon Zaten Kapalı")
        else:
            print("Televizyon Kapatılıyor")
            self.tv_durum="Kapalı"
    def ses_ayarları(self):
        while True:
            cevap=input("Sesi Azalt: '-'\nSesi Artır: '+'\n Çıkış:çıkış")
            if(cevap=="-"):
                if(self.tv_ses!=0):
                    self.tv_ses-=1
                    print("Ses:",self.tv_ses)
            elif(cevap=="+"):
                    if(self.tv_ses!=31):
                        self.tv_ses+=1
                        print("Ses:", self.tv_ses)
            else:
                print("Ses Güncellendi:",self.tv_ses)
                break
    def kanal_ekle(self,kanal_ismi):
        print("Kanal ekleniyor...")
        time.sleep(1)
        #kanal_isimleri = input("Kanal isimlerini  ', 'ile ayırarak girin:")
        #kanal_listesi = kanal_isimleri.split(",")
        #for eklenecekler in kanal_listesi:
        #    kumanda.kanal_ekle(eklenecekler)

        self.kanal_listesi.append(kanal_ismi)
        print("Kanal eklendi")

    def kanal_degiştir(self):
        while True:
            if(self.tv_durum!="Kapalı"):

                cevap=input("Sonraki Kanal:'+'\nÖnceki Kanal:'-'\nÇıkış:'q'")

                if(cevap=="+"):
                    if (self.kanal == self.kanal_listesi[-1]):
                        print("Son kanal budur!...")
                        break
                    else:
                        for i in range(0,len(self.kanal_listesi)):
                            if (self.kanal_listesi[i] == self.kanal):
                                self.kanal = self.kanal_listesi[i+1]
                                break
                            else:
                                continue
                        print("Şu anki kanal:", self.kanal)
                elif(cevap=="-"):
                    if (self.kanal == self.kanal_listesi[0]):
                        print("İlk kanal budur!...")
                        break
                    else:
                        for i in range(0,len(self.kanal_listesi)):
                            if (self.kanal_listesi[i] == self.kanal):
                                self.kanal = self.kanal_listesi[i-1]
                                break
                            else:
                                continue
                        print("Şu anki kanal:", self.kanal)


            else:
                print("Televizyon Kapalı!")
                break


    def rastgele_kanal(self):
        rastgele=random.randint(0,len(self.kanal_listesi)-1)
        self.kanal=self.kanal_listesi[rastgele]
        print("Şu anki kanal:",self.kanal)
    def __len__(self):
        return len(self.kanal_listesi)
    def __str__(self):
        return "Tv Durumu:{}\nTv Ses:{}\nKanal Listesi:{}\nŞu anki kanal:{}".format(
            self.tv_durum,self.tv_ses,self.kanal_listesi,self.kanal
        )

kumanda=Kumanda()

print("""
Televizyon uygulaması

1.Tv Aç

2.Tv Kapat

3.Ses Ayarları

4.Kanal Ekle

5.Kanal Sayısını Ögren

6.Rastgele Kanala Geç

7.Tv Bilgileri

8.Kanal Değiştir

Çıkmak için 'q'ya basın
""")

while True:
    işlem=input("İşlemi Seçiniz:")
    if(işlem=="q"):
        print("program Sonlanıyor...")
        break
    elif(işlem=="1"):
        kumanda.tv_aç()
    elif(işlem=="2"):
        kumanda.tv_kapat()
    elif(işlem=="3"):
        kumanda.ses_ayarları()
    elif(işlem=="4"):
        kanal_isimleri=input("Kanal isimlerini  ', 'ile ayırarak girin:")
        kanal_listesi=kanal_isimleri.split(",")
        for eklenecekler in kanal_listesi:
            kumanda.kanal_ekle(eklenecekler)
    elif (işlem=="5"):
        print("Kanal Sayısı:",len(kumanda))
    elif(işlem=="6"):
        kumanda.rastgele_kanal()
    elif(işlem=="7"):
        print(kumanda)
    elif(işlem=="8"):
        kumanda.kanal_degiştir()
    else:
        print("Geçersiz işlem....")
