# Fonksiyon Tanımlıyoruz
def ara_bul(sayilar, hedef):
    # Eğer Değerimiz Sayilar Listesinde varsa indexini yazdırıyoruz.
    if hedef in sayilar:
        print(sayilar.index(hedef))
    # Listemizde yoksa yapılacaklar
    else:
        index = 0
        for sayi in sayilar:
            if sayi > hedef:
                sayilar.insert(index, hedef)
                print(index)
                break
            index += 1
#Kullanıcıdan değer aldık
sayilar = input("Sayıları girin (virgülle ayrılmış): ").split(",")
sayilar = [int(sayi) for sayi in sayilar]
hedef = int(input("Hedef sayıyı girin: "))
#Aldığımız Değerleri Fonksiyona gönderdik.
ara_bul(sayilar, hedef)