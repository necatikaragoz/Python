print("""********************

problem 3 : Notu bul

********************""")


vize1 = float(input("1. vize notunu giriniz"))
vize2 = float(input("2. vize notunuz giriniz"))
final = float(input("final notunu giriniz"))

grade = (vize1 * 0.3) + (vize2 * 0.3) + (final * 0.6)

print("grade = {}".format(grade) )


if(grade >= 90):
    print("AA")
elif(grade >= 85):
    print("BA")
elif(grade >= 80):
    print("BB")
elif(grade >= 75):
    print("CB")
elif(grade >= 70):
    print("CC")
elif(grade >= 65):
    print("DC")
elif(grade >= 60):
    print("DD")
elif(grade >= 55):
    print("FD")
else:
    print("FF")
