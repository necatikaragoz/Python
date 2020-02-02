print("oyuncu kaydetme programı")

isim = input("oyuncunun adı : ")
soyad = input("oyuncunun soyadı :")
takım = input("oyuncunun Takımı : ")

bilgiler = [isim, soyad, takım]

print("bilgiler kaydediliyor...")

print("oyuncunun Adı : {}\n oyuncunun Soyadı : {} \n Oyuncunun Takımı : {} \n ".format(bilgiler[0],bilgiler[1],bilgiler[2]))

print("bilgiler kaydedildi")