print("deben kitle indexsi bulma")

boy = int(input("lütfen boyunuzu cm olarak giriniz = "))
kilo = int(input("lütfen kilonuzu giriniz = "))

endex = kilo / ((boy/100) ** 2)
print("vücut kitle engeksiniz = {}".format(endex))