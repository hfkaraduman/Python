print("""
*************************
Kullanıcı Girişi Programı
*************************
""")

sys_kullanici_adi="hasan"
sys_parola="1234"
giris_hakki=3

while True:
    kullanici_adi=input("Kullanıcı Adı:")
    parola=input("Parola:")
    if(kullanici_adi != sys_kullanici_adi and parola==sys_parola):
        print("Kullanıcı Adı Hatalı...")
        giris_hakki-=1
    elif(kullanici_adi == sys_kullanici_adi and parola!=sys_parola):
        print("Parola Hatalı...")
        giris_hakki-=1
    elif (kullanici_adi != sys_kullanici_adi and parola != sys_parola):
        print("Kullanıcı Adı ve Parola Hatalı...")
        giris_hakki -= 1
    else:
        print("Sisteme Başarıyla Giriş Yapıldı...")
        break
    if(giris_hakki == 0):
        print("Giriş Hakkınız Bitti...")
        break