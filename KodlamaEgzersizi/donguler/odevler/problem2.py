print("This program check that number is a Armstrong number")
print(" press q for exit")
"""
Kullanıcıdan aldığınız bir sayının "Armstrong" sayısı olup olmadığını bulmaya çalışın.

Örnek olarak, Bir sayı eğer 4 basamaklı ise ve oluşturan rakamlardan herbirinin 4. kuvvetinin toplamı( 3 basamaklı sayılar için 3.kuvveti ) o sayıya eşitse bu sayıya "Armstrong" sayısı denir.

Örnek olarak : 1634 = 1^4 + 6^4 + 3^4 + 4^4

"""


while True:

    number = input("please insert a number: ")

    if(number == "q"):
        print("exit is occured")
        break
    else:
        sum = 0
        size = len(number)
        for char in number:
            print("char = ", char)
            sum += pow(int(char), size)

        if(sum == int(number)):
            print("number" , number, "is a Armstrong number", "sum equal to ", sum)
        else:
            print("number",  number, "isn't a Armstrong number", "sum equal to ", sum)


