print("""
****************************************
1'den 10'a Kadar Sayıları Çarpım Tablosu
****************************************
""")

for i in range(1,11):
    print("\n")
    for j in range(1,11):
        print("{}x{}={}".format(i,j,i*j))