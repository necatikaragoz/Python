print("This program check numbers is perfect or not")
print(" press q for exit")

"""
Kullanıcıdan aldığınız bir sayının mükemmel olup olmadığını bulmaya çalışın.

Bir sayının kendi hariç bölenlerinin toplamı kendine eşitse bu sayıya "mükemmel sayı" denir. Örnek olarak, 6 mükemmel bir sayıdır. (1 + 2 + 3 = 6)
"""

while True:

    number = input("please insert a number")

    if(number == "q"):
        print("exit is occured")
        break
    else:
        nb = int(number)

        bolenList = list()
        toplam = 0
        for i in range(1,nb):
            if( (nb % i) == 0):
                toplam += i
                bolenList.append(i)
                print("i = " ,i )

        if(toplam == nb):
            print("this number is a perfect number")
        else:
            print("this number isn't a perfect number")




