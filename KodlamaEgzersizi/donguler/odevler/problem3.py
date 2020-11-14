print("This program write  multiplier table")
print(" press q for exit")

"""
1'den 10'kadar olan sayılarla ekrana çarpım tablosu bastırmaya çalışın.

İpucu: İç içe 2 tane for döngüsü kullanın. Aynı zamanda sayıları range() fonksiyonunu kullanarak elde edin.
"""

liste = [i for i in range (1,10)]
print(liste)

for i in liste:
    for j in liste:
        print("{} x {} = {}".format(i,j,i*j))



