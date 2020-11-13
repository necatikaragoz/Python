"""
2. dereceden bir bilinmeyenli denklemin köklerini bulma

Denklem : ax^2 + bx + c1

Deltayı Hesaplama:  b ** 2 -  4 * a * c

Birinci Kök : (-b - delta ** 0.5) / (2*a)
İkinci Kök : (-b + delta ** 0.5) / (2*a)
"""

print("Denklem : ax^2 + bx + c")
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

delta = (b*b) - (4*(a*c))

print("delta = ", delta)

first = (-b - (delta) ** 0.5) / (2*a)
second = (-b + (delta) ** 0.5) / (2*a)

print("birinci kök = {}\n ikinci kök  = {} \n" .format(first,second))
