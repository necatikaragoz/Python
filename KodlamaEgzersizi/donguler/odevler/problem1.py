print("This program check numbers is perfect or not")
print(" press q for exit")

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




