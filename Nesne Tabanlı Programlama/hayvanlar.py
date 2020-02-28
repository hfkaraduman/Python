

class hayvan():
    def __init__(self,isim,ayak_sayısı,yaşı,rengi):
        self.isim=isim
        self.ayak_sayısı=ayak_sayısı
        self.yaşı=yaşı
        self.rengi=rengi
    def bilgilerigöster(self):
        print("İsim:{}\nAyak Sayısı:{}\n"
              "Yaşı:{}\nRengi:{}".format(self.isim,self.ayak_sayısı,self.yaşı,self.rengi))

class köpek(hayvan):
    def __init__(self,isim,ayak_sayısı,yaşı,rengi,cinsi):
        super().__init__(isim,ayak_sayısı,yaşı,rengi)
        self.cinsi=cinsi
    def bilgileri_göster(self):
        super().bilgilerigöster()
        print("Cinsi:{}".format(self.cinsi))


köpek1=köpek("ateş",4,3,"kırmızı","kurt")
köpek1.bilgileri_göster()
