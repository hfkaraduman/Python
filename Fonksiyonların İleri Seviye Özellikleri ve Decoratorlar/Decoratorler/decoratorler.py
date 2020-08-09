def ekstra(fonk):
    def wrapper(sayılar):
        çiftler_toplamı=0
        tekler_toplamı=0
        çift_sayılar=0
        tek_sayılar=0

        for sayı in sayılar:
            if (sayı % 2 == 0):
                çiftler_toplamı+=sayı
                çift_sayılar+=1
            else:
                tekler_toplamı+=sayı
                tek_sayılar+=1

        print("Teklerin Ortalaması:",tekler_toplamı/tek_sayılar)
        print("Çiftlerin Ortalması",çiftler_toplamı/çift_sayılar)

        fonk(sayılar)
    return wrapper

@ekstra
def ortalama(sayılar):

    toplam=0

    for sayı in sayılar:
        toplam+=sayı
    print("Genel ortalama:",toplam/len(sayılar))

ortalama([1,2,3,4,5,6,7,8,9,10])