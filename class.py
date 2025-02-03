"""
**  Bank isminde bir sınıf tanımlayınız.
**  Üretilen her bir nesne "owner" isminde biz özelliğe sahip olmalıdır. Bank("Sadık Turan")
**  Üretilen her bir nesne "wallet" isminde bir özelliğe sahip olup başlangıçta 0.0 değerinde olmalıdır.
**  Üretilen her bir nesne için "yatir" metodu oluşturun ve dışarıdan yatırılacak miktar bilgisini alıp bakiye
    üzerine ekleyin ve bakiye miktarını geriye döndürün.
**  Üretilen her bir nesne için "cek" metodu oluşturun ve dışarıdan çekilecek miktar bilgisini alıp wallet
    değerinden çıkarıp geriye döndürün.

    hesap = Bank("Sadık Turan")
    hesap.owner => Sadık Turan
    hesap.wallet => 0.0
    hesap.yatir (1000) => 1000.0
    hesap.cek (500) => 500.0
"""

class Bank:
    # Attribute & Property
    def __init__(self,name):    
        self.owner = name
        self.wallet = 0.0


    #FONKSİYONLAR
    #Para Yatırma Fonksiyonu
    def yatir(self,value):
        return value + self.wallet
    
    #Para Çekme Fonksiyonu
    def cek(self,value):
        return self.wallet - value



# MENÜ
def menu(user):
    print("--------------HOŞGELDİNİZ--------------")

    print("\n Hangi İşlemi Yapmak İstersiniz?")
    print("1) Bakiye Sorgulama")
    print("2) Para Yatırma")
    print("3) Para Çekme")
    print("4) Çıkış")

    select = int(input("Lütfen Bir Seçenek Seçiniz: "))

    if(select==1):
        print(f"Mevcut Bakiyeniz={user.wallet}")
        k = input("\n<Devam Etmek İçin Enter Tuşuna Basınız>\n")
    elif(select==2):
        price=int(input("Yatıracağınız Miktarı Giriniz: "))
        user.wallet = user.yatir(price)
        print("\nİşleminiz Başarıyla Gerçekleşti!\n")
        k = input("\n<Devam Etmek İçin Enter Tuşuna Basınız>\n")
    elif(select==3):
        price=int(input("Çekeceğiniz Miktarı Giriniz: "))
        if user.cek(price)<0:
            print("\n!!!YETERSİZ BAKİYE!!!\n")
            k = input("\n<Devam Etmek İçin Enter Tuşuna Basınız>\n")
        else:
            user.wallet = user.cek(price)
            print("|Paranızı Alandan Almayı Unutmayın|")
            k = input("\n<Devam Etmek İçin Enter Tuşuna Basınız>\n")
    elif(select==4):
        print("--------------İYİ GÜNLER DİLERİZ--------------")
        return 1
    else:
        print("\n\n\n!!!!Hatalı İşlem, Lütfen Tekrar Deneyin!!!!\n\n\n")


isim=input("İsim Giriniz: ")
user = Bank(isim) #class oluşturuldu.

#LOOP
while(True):
    flag = menu(user)
    if(flag == 1):
        break