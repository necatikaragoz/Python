print("faktöriyel bulma sistemine hoşgeldiniz")

print("""********************


programdan çıkmak için "q" tuşuna basınız.

********************""")

"""
liste = [i for i in range (2,6)]
print(liste)
print(* range (2,6) )
"""


while True:
    giris = input("faktöriyel bulmak istediğiniz sayıyı giriniz : ")
    if(giris == "q"):
        print("cıkıd yapılıyor")
        break
    else:

        deger = int(giris)
        faktöriyel = 1
        for i in range(2, deger +1 ):
            faktöriyel *= i

    print("girdiniz sayının faktöriyeli = {} ".format(faktöriyel) )
