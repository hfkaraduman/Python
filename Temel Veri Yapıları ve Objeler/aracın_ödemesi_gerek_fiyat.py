# coding=utf-8
#Bir aracın kilometrede ne kadar yaktığı ve kaç kilometre yol yaptığı bilgilerini alın
# ve sürücünü toplam ne kadar ödemesini gerektiğini hesaplayın.
kilometrede_yaktigi=float(raw_input("Aracinizin kilometrede yaktiği fiyati giriniz:"))
kilomete=float(raw_input("Aracınızın kaç km yol yaptığını giriniz:"))
print("Sürücünün toplam ödemesi gereken fiyat:{:.2f} liradır".format(kilometrede_yaktigi*kilomete))