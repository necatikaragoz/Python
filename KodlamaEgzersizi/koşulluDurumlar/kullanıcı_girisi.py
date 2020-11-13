print("""********************

kullanıcı girişi

********************""")

sys_username = "necati"
sys_password = "12345"

user_username = input("lütfen kullanıcı adını giriniz")
user_password = input("lütfen şifrenizi giriniz")


if(sys_username == user_username and sys_password != user_password):
    print("şifre hatalı.")
elif(sys_username != user_username and sys_password == user_password):
    print("kullanıcı adı hatalı.")
else:
    print("giriş başarılı")
