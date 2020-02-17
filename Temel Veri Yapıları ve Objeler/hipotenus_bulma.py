# coding=utf-8
#dik üçgende hipotenus uzunlugunu bulma

birinci_kenar=float(raw_input("Birinci kenarı degerini giriniz:"))
ikinci_kenar=float(raw_input("İkinci kenar degerini giriniz:"))
hipotenus=(birinci_kenar**2+ikinci_kenar**2)**0.5
print("Hipotenüs uzunluğu:{:.2f}".format(hipotenus))