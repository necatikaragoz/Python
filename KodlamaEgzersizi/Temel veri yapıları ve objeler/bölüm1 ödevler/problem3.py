print("Bir aracın kilometrede ne kadar yaktığı ve kaç kilometre yol yaptığı bilgilerini alın \n ve sürücünü toplam ne kadar ödemesini gerektiğini hesaplayın.")

metricUcret = float(input("lütfen aracınızın kmde ne kadar yaktığını belirtin"))
km = int(input("lütfen kaç km yaptığınızı belirtin"))

print("Ödemeniz gereken tutar = {}".format(km*metricUcret))