print("This program check that number is a Armstrong number")
print(" press q for exit")



while True:

    number = input("please insert a number: ")

    if(number == "q"):
        print("exit is occured")
        break
    else:
        sum = 0
        size = len(number)
        for char in number:
            print("char = ", char)
            sum += pow(int(char), size)

        if(sum == int(number)):
            print("number" , number, "is a Armstrong number", "sum equal to ", sum)
        else:
            print("number",  number, "isn't a Armstrong number", "sum equal to ", sum)


