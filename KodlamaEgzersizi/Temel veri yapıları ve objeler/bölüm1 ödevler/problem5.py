print("Kullanıcıdan iki tane sayı isteyin ve bu sayıların değerlerini birbirleriyle değiştirin.")

a = input("ilk sayıyı giriniz")
b = input("ikinci sayıyı giriniz")

a,b = b,a

print("ilk sayı = {}, ikinci sayı = {}, " .format(a,b))
