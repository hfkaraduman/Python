# coding=utf-8
#Kullanicinin beden kitle indeksini hesaplama

boy=float(raw_input("Boyunuzun uzunluğunu giriniz:"))
kilo=float(raw_input("Kilonuzu giriniz:"))
beden_kitle_indeksi=(kilo/boy**2)
print("Beden kitle indeksiniz:{:.2f}".format((beden_kitle_indeksi)))