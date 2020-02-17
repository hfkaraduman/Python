# coding=utf-8
print("""******************
BEDEN KİTLE İNDEKSİ HESAPLAMA
******************
"""
)

boy=float(raw_input("Boyunuzu Giriniz:"))
kilo=float(raw_input("Kilonuzu Giriniz"))
beden_kitle_indeksi=kilo/(boy*boy)
print("Beden kitle indeksiniz:{:.2f}".format(beden_kitle_indeksi))

if beden_kitle_indeksi<18.5:
    print("ZAYIF")
elif beden_kitle_indeksi>18.5 and beden_kitle_indeksi<25:
    print ("NORMAL")
elif beden_kitle_indeksi>25 and beden_kitle_indeksi<30:
    print ("FAZLA KİLOLU")
else:
    print ("OBEZ")
