'''
print("Hello World")
print("hello world 2")
i=10
a = 4
b = 3.5
#a,b = b,a
#yorum satırı
"""
zxjkfzkl>
"""
print("a = ", a)
print(b)

print(a / b)

a=4
b = 64 ** (1/4)
print("b = ", b )

str = "necati"
str2 = "karagoz"

str3 = str + "_" + str2

print(str3)
print(str[0])

print(str[-1])

print(str[:3])

print(str3[5:])

print("last one = ", str3[:-1])

print(str3[::1])


print("ters çevir = ", str3[::-1])

print("string boyu ", len(str3))

print("harf değiştir", str)

a= "python"

print("carpma  = ", a*3)

b = "necati"
b = b + "karagoz"

print(b)

#verileri değiştirme

a = 43
float(a)
print(a)

print("-----------------------------------")

print(type(12))

print(3,4,5,6,sep="")

print("Python")

print(*"Python")
print(*"Python", sep = ".")

print("T","B","M","M", sep = ".")
print(*"TBMM", sep = ".")
print(*"TBMM", sep = ".")

print( "{} + {}  olabilir" .format(3,4))

print( "{:.2f} + {:.3f}  olabilir" .format(3.1426,5.3245))
'''

'''
liste = ["elma", 35, "Merhaba", 3.14, 5]
liste2 = list()
print(liste2)
print(liste)
print(type(liste))
print(len(liste))

liste3 = list("merhaba")

print(liste3)
print(len(liste3))


liste4 = [1,2,3,4,5,6,7,8,9]

print(liste4[2])
print(liste4[-1])

print(liste4[len(liste4)-1])


print("[start point :  stop point : atlama miktarı]")
print("2 ye kadar elemanları al")
print(liste4[:2])

print("2 den itibaren elemanları al")
print(liste4[2:])

print("2 den itibaren elemanları al")
print(liste4[::2])

print("1 ile 5 arası  2 atlayarak al")
print(liste4[1:5:2])
print("tersten yaz")
print(liste4[::-1])

liste4.append(10)
print(liste4)
liste4.pop()

print(liste4)

liste4.pop(0)

print(liste4)

liste5 = [11,3,4,5,6]
print(liste5)
liste5.sort()

print(liste5)
liste5.sort(reverse = True)
print(liste5)

liste6 = ["php", "python", "java", "C"]

liste6.sort()
print(liste6)
liste6.sort(reverse = True)

print(liste6)

'''

'''
turple1  = (0,1,2,3,4,5)

print(turple1)

print(type(turple1))
'''
'''
sözlük1 = {"sıfır": 0, "bir" :1, "iki":2}

print(type(sözlük1))

print(sözlük1)

sözlük2 = dict()

print(sözlük1["sıfır"])

sözlük3 = {1:"bir",2:"iki", 3:"üç"}

print(sözlük3[3])

sözlük1["dört"] = 4


print(sözlük1["dört"])

'''
x = input("lütfen bir sayı giriniz")
print(type(x) )

y = int(input("lütfen bir sayı giriniz"))
print(type(y) )
print("x = ", y*3)

a = int(input("lütfen bir sayı giriniz 1"))
b = int(input("lütfen bir sayı giriniz 2"))
c = int(input("lütfen bir sayı giriniz 3"))

print("sayı = ", a*b*c )