#Fonksiyon Tanımlıyoruz
def ara_bul(sayilar,hedef):
    #Eğer Değerimiz Sayilar Listesinde varsa indexini yazdırıyoruz.
    if hedef in sayilar:
        print (sayilar.index(hedef))
    #Listemizde yoksa yapılacaklar
    else:
        #Değeri Ekliyoruz
        sayilar.append(hedef)
        #Listeyi Yeniden sıralıyoruz
        sayilar.sort()
        #indexi yazdırıyoruz.
        print(sayilar.index(hedef))
ara_bul([1,2,4,8],4)
ara_bul([2,4,5,8],3)