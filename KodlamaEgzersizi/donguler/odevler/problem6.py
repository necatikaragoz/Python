"""
Buradaki problemin çözümünü derslerimizde özellikle öğrenmedik. Burada mantık yürüterek ve list comprehension kullanarak 1'den 100'e kadar olan sayılardan sadece çift sayıları bir listeye atmayı yapmayı çalışın.

"""

print("This program write  multiplier table")
print(" press q for exit")


liste = [ x for x in range(1,100) if x % 2 == 0]

print(liste)