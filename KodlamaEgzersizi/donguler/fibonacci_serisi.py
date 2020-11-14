print("fibonacci bulma sistemine hoşgeldiniz")

print("""********************

programdan çıkmak için "q" tuşuna basınız.

********************""")

a = 1
b = 1

fibonaccisayisi = int(input("fibonacci serisi miktarını giriniz : "))

fibonacci = [a,b]
for i in range (fibonaccisayisi):
    a, b = b, a+b
    fibonacci.append(b)
    print("a:", a, "b:", b)

print(fibonacci)