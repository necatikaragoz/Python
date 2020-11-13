print("""********************

Beden kitle endeksi

********************""")


kilo = int(input("lütfen kilonuzu kg giriniz") )
boy = float(input("lütfen boyunuz m olarak giriniz") )

if (boy != 0):

    bki = kilo / (boy * boy)
    if(bki >= 30 ):
        print("obez")
    elif (bki >= 25 ):
        print("fazla kilolu")
    elif (bki >= 18.5 ):
        print("Normal")
    else:
        print("zayıf")
else:
    print("boy degeri geçersiz")


