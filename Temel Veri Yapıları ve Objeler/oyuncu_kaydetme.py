print("Oyuncu Kaydetme Programi")

ad = raw_input("Oyuncunun adi:")
soyad = raw_input("Oyuncunun soyadi")
takimi = raw_input("Oyuncunun takimi")

bilgiler = [ad,soyad,takimi]

print("Bilgiler Kaydediliyor...")

print("Oyuncunun adi:{}\nOyuncunun soyadi:{}\nOyuncunun takimi:{}".format(bilgiler[0],bilgiler[1],bilgiler[2]))

print("Bilgiler Kaydedildi.")