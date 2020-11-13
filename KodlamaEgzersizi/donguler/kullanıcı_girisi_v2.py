print("""********************

kullanıcı girişi

********************""")

sys_username = "necati"
sys_password = "12345"

check_cnt = 3


while True:
    user_username = input("Kullanıcı adı:")
    user_password = input("Parola :")

    if(sys_username == user_username and sys_password != user_password):
        print("şifre hatalı.")
        check_cnt -= 1
    elif(sys_username != user_username and sys_password == user_password):
        print("kullanıcı adı hatalı.")
        check_cnt -= 1
    else:
        print("giriş başarılı")
        break

    if(check_cnt == 0):
        print("giriş hakkınız bitti")
        break
    else:
        print("kalan giriş hakkınız =  {} ".format(check_cnt))




