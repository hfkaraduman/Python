print("""
*************************
Faktöriyel Bulma

Çıkmak için 'q'ya basın

************************
""")
while True:
    sayi=input("Sayı:")
    if(sayi=="q"):
        print("Program Sonlanıyor...")
        break
    else:
        sayi=int(sayi)
        faktoriyel=1

        for i in range(1,sayi+1):
            faktoriyel=faktoriyel*i
        print("Faktoriyel",faktoriyel)