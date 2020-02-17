# coding=utf-8
print("""**************
HARF NOTU HESAPLATMA
""")

vize1=float(raw_input("1.Vize Notunuzu Giriniz:"))
vize2=float(raw_input("2.Vize Notunuzu Giriniz:"))
final=float(raw_input("Final Notunuzu Giriniz:"))

toplam_not=(vize1*0.3)+(vize2*0.3)+(final*0.4)

if toplam_not>=90:
    print("Harf Notunuz AA")
elif toplam_not>=85:
    print("Harf Notunuz BA")
elif toplam_not>=80:
    print ("Harf Notunuz BB")
elif toplam_not>=75:
    print ("Harf Notunuz CB")
elif toplam_not>=70:
    print ("Harf Notunuz CC")
elif toplam_not>65:
    print ("Harf Notu DC")
elif toplam_not > 60:
    print ("Harf Notu DD")
elif toplam_not>55:
    print ("Harf Notu FD")
elif toplam_not<55:
    print ("Harf Notunuz FF")
else:
    print ("Harf Notunuz Hesaplanamadı")
