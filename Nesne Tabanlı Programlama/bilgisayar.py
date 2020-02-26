import time

class Bilgisayar():

    def __init__(self,pc_durum="Kapalı",ekran_parlaklığı=0,ses_ayarı=50,görev_listesi=["Cpu"],işlem="Cpu"):
        self.pc_durum=pc_durum
        self.ekran_parlaklığı=ekran_parlaklığı
        self.görev_listesi=görev_listesi
        self.işlem=işlem
        self.ses_ayarı=ses_ayarı
    def __str__(self):
        return "Pc Durumu:{}\nEkran Parlaklığı:{}\nSes Ayarı:{}\nGörev Listesi:{}\nİşlem:{}".format(
            self.pc_durum,self.ekran_parlaklığı,self.ses_ayarı,self.görev_listesi,self.işlem

        )
    def power(self):
        if(self.pc_durum=="Kapalı"):
            time.sleep(2)
            print("Bilgisayar Açılıyor")
            self.pc_durum="Açık"
            self.ekran_parlaklığı=30
            bilgisayar.başlangıç()


        else:
            print("Bilgisayar Kapatılıyor")
            time.sleep(2)
            self.pc_durum="Kapalı"
            self.ekran_parlaklığı=0
            bilgisayar.başlangıç()
    def ekran_ayarları(self):
        while True:
            if(self.pc_durum=="Açık"):
                cevap=input("Parlaklığı Artır:'+'\nParlaklığı Azalt:'-'\nÇıkış:'q'")
                if(cevap=="+"):
                    if(self.ekran_parlaklığı!=100):
                        self.ekran_parlaklığı+=10
                        print("Ekran Parlaklığı:",self.ekran_parlaklığı)
                elif(cevap=="-"):
                    if(self.ekran_parlaklığı!=0):
                        self.ekran_parlaklığı-=10
                        print("Ekran Parlaklığı:",self.ekran_parlaklığı)
                else:
                    break

    def ses_ayarları(self):
        while True:
            if(self.pc_durum=="Açık"):
                cevap=input("Sesi Artır:'+'\nSesi Azalt:'-'\nÇıkış:'q'")
                if(cevap=="+"):
                    if(self.ses_ayarı!=100):
                        self.ses_ayarı+=10
                        print("Ses Seviyesi:",self.ses_ayarı)
                elif(cevap=="-"):
                    if(self.ses_ayarı!=0):
                        self.ses_ayarı-=10
                        print("Ses Ayarı:",self.ses_ayarı)
                else:
                    break

    def görev_ekle(self,görev_ismi):
        if(self.pc_durum=="Açık"):
            time.sleep(1)
            self.görev_listesi.append(görev_ismi)

    def görev_değiştir(self):
        while True:
            if(self.pc_durum=="Açık"):
                cevap=input("Sonraki görev:'+'\nÖnceki Görev:'-'\nÇıkış:'q'")
                if(cevap=="+"):
                    for i in range(0,len(self.görev_listesi)):
                        if(self.görev_listesi[i]==self.işlem):
                            if (self.işlem == self.görev_listesi[-1]):
                                i=0
                                self.işlem = self.görev_listesi[i]
                                break
                            self.işlem = self.görev_listesi[i+1]
                            break
                        else:
                            continue
                    print("Şu Anki İşlem:",self.işlem)

                elif(cevap=="-"):
                    for i in range(0,len(self.görev_listesi)):
                        if(self.görev_listesi[i]==self.işlem):
                            self.işlem=self.görev_listesi[i-1]
                            break
                        else:
                            continue
                    print("Şu Anki İşlem:",self.işlem)
                else:
                    break


    def başlangıç(self):
        print("""
                    1.Power
                    2.Ekran Ayarları
                    3.Ses Ayarları
                    4.İşlemi Ögren
                    5.Görev Ekle
                    6.İşlemi Değiştir
                    7.Pc Bilgileri

                    Çıkmak için 'q'ya basın
                    """)
        while True:
            işlem = input("İşlem Seçiniz:")
            if (işlem == "1"):
                bilgisayar.power()
            elif (işlem == "2"):
                    bilgisayar.ekran_ayarları()
                    bilgisayar.başlangıç()
            elif (işlem == "3"):
                bilgisayar.ekran_ayarları()
                bilgisayar.başlangıç()
            elif (işlem == "4"):
                if (bilgisayar.pc_durum == "Açık"):
                    print("Şu Anki İşlem:", self.işlem)
                    bilgisayar.başlangıç()
                else:
                    bilgisayar.başlangıç()

            elif(işlem=="5"):
                if (bilgisayar.pc_durum == "Açık"):
                    görev_isimleri = input("Görev İsimlerini ',' ile ayırarak girin:")
                    görev_listesi = görev_isimleri.split(",")
                    for eklenecekler in görev_listesi:
                        bilgisayar.görev_ekle(eklenecekler)
                else:
                    bilgisayar.başlangıç()
                bilgisayar.başlangıç()
            elif(işlem=="6"):
                if (bilgisayar.pc_durum == "Açık"):
                    bilgisayar.görev_değiştir()
                    bilgisayar.başlangıç()
                else:
                    bilgisayar.başlangıç()

            elif(işlem=="7"):
                print(bilgisayar)
                bilgisayar.başlangıç()
            else:
                break

bilgisayar=Bilgisayar()
bilgisayar.başlangıç()







