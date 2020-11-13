print("""********************

En büyük sayıyı bul

********************""")


a = int(input("bir sayı giriniz"))
b = int(input("ikinci sayı giriniz"))
c = int(input("ücüncü sayı giriniz"))

if(a>= b and a >=c):
    print("en büyük sayı = {}".format(a))
elif(b>=a and b >= c):
    print("en büyük sayı = {}".format(b))
elif(c>=a and c >= b):
    print("en büyük sayı = {}".format(c))
