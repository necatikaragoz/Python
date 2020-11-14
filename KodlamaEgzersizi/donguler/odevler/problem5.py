
print("This program write  multiplier table")

"""
1'den 100'e kadar olan sayılardan sadece 3'e bölünen sayıları ekrana bastırın. Bu işlemi continue ile yapmaya çalışın.
"""

print(" press q for exit")



for i in range(1,100):
    if( i%3 != 0):
        continue
    else:
        print("{} sayısı 3 e tam bölünebilir".format(i))
