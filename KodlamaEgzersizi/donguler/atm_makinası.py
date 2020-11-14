print("atm sistemine hoşgeldiniz")

print("""********************

işlemler

1. Bakiye sorgulama
2. Para Yatırma
3. Para çekme

programdan çıkmak için "q" tuşuna basınız.

********************""")



bakiye = 1000 #bakiyemiz 1000 tl olsun


while True:
    command = input("işlemi giriniz...")

    if(command == "q"):
        print("cıkıs yapılıyor")
        break
    elif(command == "1"):
        print("bakiyeniz {} tl dir.".format(bakiye))
    elif(command == "2"):
        yatırılacakpara = int(input("yatıracağınız miktarı giriniz : ") )

        bakiye += yatırılacakpara
    elif(command == "3"):
        cekilecek_miktar = int(input("cekmek istediğiniz tutarı giriniz : ") )

        if(cekilecek_miktar > bakiye):
            print("hesabınızda yeterli miktarda para bulunmamaktadır")
            print("hesabınızda {} Tl bulunmaktadır".format(bakiye))
        else:
            bakiye -= cekilecek_miktar
            print("hesabınızda {} Tl kalmıştır".format(bakiye))

    else:
        print("lütfen geçerli bir işlem giriniz")


