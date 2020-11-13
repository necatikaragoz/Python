print("""**************************

hesap makinası

toplama için 1 e basınız.
çıkarma için 2 e basınız.
çarpma için 3 e basınız.
bölme için 4 e basınız."

************************""")

a = int(input('Bir sayi giriniz.') )
b = int(input('Bir sayi daha giriniz.') )

selector = input("işlem numarası giriniz")

if(selector == "1"):
    print(" {} ile {} nin toplamı = {} dır".format(a, b, a+b))
elif(selector == "2"):
    print(" {} ile {} nin farkı = {} dır".format(a, b, a - b))
elif(selector == "3"):
    print(" {} ile {} nin çarpımı = {} dır".format(a, b, a * b))
elif(selector == "4"):
    print(" {} ile {}  bölümü = {} dır".format(a, b, a / b))
else:
    print("Lütfen geçerli bir işlem giriniz...")

