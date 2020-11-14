print("This program find sum of the input numbers")
print(" press q for exit")
"""
Her bir while döngüsünde kullanıcıdan bir sayı alın ve kullanıcının girdiği sayıları "toplam" isimli bir değişkene ekleyin. Kullanıcı "q" tuşuna bastığı zaman döngüyü sonlandırın ve ekrana "toplam değişkenini" bastırın.

İpucu : while döngüsünü sonsuz koşulla başlatın ve kullanıcı q'ya basarsa döngüyü break ile sonlandırın.
"""

sum = 0

while True:

    number = input("please insert a number: ")

    if(number == "q"):
        print("exit is occured")
        break
    else:
       sum += int(number)


print("sum = ", sum)