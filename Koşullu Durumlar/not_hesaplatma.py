# coding=utf-8
system_kullanici_adi="Hasan"
system_kullanici_sifresi=123

kullanici_adi=raw_input("Kullanıcı Adınızı Giriniz:")
kullacici_sifresi=int(raw_input("Şifrenizi Giriniz:"))

if kullanici_adi==system_kullanici_adi and kullacici_sifresi==system_kullanici_sifresi:
    print("Hoşgeldiniz")
elif kullanici_adi!=system_kullanici_adi and kullacici_sifresi==system_kullanici_sifresi:
    print("Kullanıcı Adını Yanlış Girdiniz!")
elif kullanici_adi==system_kullanici_adi and kullacici_sifresi!=system_kullanici_sifresi:
    print("Şifrenizi Yanlış Girdiniz!")
else :
    print("Kullanıcı Adı ve Şifrenizi Yanlış Girdiniz")

