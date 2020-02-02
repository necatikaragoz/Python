print("Kullanıcıdan bir dik üçgenin dik olan iki kenarını(a,b) alın ve hipotenüs uzunluğunu bulmaya çalışın." 
"Hipotenüs Formülü: a^2 + b^2 = c^2" )

dikkenar = float(input("lütfen dikkener uzunluğunu cm olarak giriniz"))
yataykenar = float(input("lütfen yataykenar uzunluğunu cm olarak giriniz"))

hipotenüs = ((dikkenar**2) + (yataykenar **2))**0.5

print("hipotenüs = {}".format(hipotenüs))