gecerlı_uidler=["04A31F7C", "04B22E11", "04C93A55"]
while True:
    print("\n--- ROBOT MENÜSÜ ---")
    print("1) Robot durumu")
    print("2) Koli oku")
    print("3) Çıkış")
    print("4) Koli sayısını göster")

    secim=input("Seçimin:")
    if secim=="1":
       print("Robot hazır.Pil:12.8V")
    elif secim=="2":
        uid=input("Koli UID'sini gir:")
        if uid in gecerlı_uidler:
            print("GEÇERLİ KOLİ:", uid)
        else:
            print("GEÇERSİZ KOLİ!")

    elif secim=="3":
        print("Robot kapanıyor...")
        break
    elif secim=="4":
        print("Kayıtlı koli sayısı:",len(gecerlı_uidler))
    else:
        print("Yanlış seçim,tekrar dene.")
    