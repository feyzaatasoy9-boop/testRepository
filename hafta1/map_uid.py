UID_TABLOSU = {
    "04A31F7C": "ankara",
    "04B22E11": "bursa",
    "04C93A55": "konya",
    "04D17B20": "adana",
    "04E58C33": "samsun",
}

SAHADAKI_KOLILER = [
    "04A31F7C", "04B22E11", "04C93A55", "04D17B20", "04E58C33",
    "04FF0001", "04FF0002",
]


def bos_sehirler():
    """5 şehrin hepsi boş olan yeni bir sözlük döndürür."""
    return {"ankara": False, "bursa": False, "konya": False,
            "adana": False, "samsun": False}


def uid_temizle(ham_uid):
    """'04 a3 1f 7c' gibi yazımları '04A31F7C' haline getirir."""
    return ham_uid.replace(" ", "").replace(":", "").strip().upper()


def koli_karari(ham_uid, sehirler, teslim_edilenler):
    """Okunan koli için karar verir. (karar, şehir) döndürür."""
    uid = uid_temizle(ham_uid)
    if uid == "":
        return "OKUMA_HATASI", None
    if uid not in UID_TABLOSU:
        return "GECERSIZ", None
    if uid in teslim_edilenler:
        return "ZATEN_TESLIM", UID_TABLOSU[uid]
    sehir = UID_TABLOSU[uid]
    if sehirler[sehir]:
        return "SEHIR_DOLU", sehir
    return "GOTUR", sehir


def teslim_et(ham_uid, sehir, sehirler, teslim_edilenler):
    """Koliyi teslim edilmiş olarak işaretler."""
    sehirler[sehir] = True
    teslim_edilenler.add(uid_temizle(ham_uid))


def oled_goster(ham_uid, karar, sehir):
    """Robotun OLED ekranını taklit eder."""
    uid = uid_temizle(ham_uid)
    if karar == "GOTUR":
        satir1, satir2 = "ID: " + uid, "SEHIR: " + sehir.upper()
    elif karar == "SEHIR_DOLU":
        satir1, satir2 = "SEHIR DOLU", sehir.upper()
    elif karar == "ZATEN_TESLIM":
        satir1, satir2 = "ZATEN TESLIM", sehir.upper()
    elif karar == "GECERSIZ":
        satir1, satir2 = "GECERSIZ KOLI", uid
    else:
        satir1, satir2 = "OKUMA HATASI", "TEKRAR OKUT"

    print("+------------------+")
    print(f"| {satir1:<17}|")
    print(f"| {satir2:<17}|")
    print("+------------------+")


if __name__ == "__main__":
    sehirler = bos_sehirler()
    teslim_edilenler = set()
    puan = 0

    while True:
        print("\n--- ROBOT ---")
        print("1) Koli oku (UID gir)")
        print("2) Rakip bir şehri doldurdu")
        print("3) Durumu göster")
        print("4) Çıkış")
        secim = input("Seçimin: ")

        if secim == "1":
            uid = input("UID: ")
            karar, sehir = koli_karari(uid, sehirler, teslim_edilenler)
            oled_goster(uid, karar, sehir)

            if karar == "GOTUR":
                cevap = input("Teslim edildi mi? (e/h): ").strip().lower()
                if cevap == "e":
                    teslim_et(uid, sehir, sehirler, teslim_edilenler)
                    puan = puan + 15
                    print("+15 puan! Toplam:", puan)

        elif secim == "2":
            sehir = input("Rakip hangi şehri doldurdu? ").strip().lower()
            if sehir in sehirler:
                sehirler[sehir] = True
                print(sehir, "artık dolu (rakip).")
            else:
                print("Böyle bir şehir yok.")

        elif secim == "3":
            for s, dolu in sehirler.items():
                print(s, "-> DOLU" if dolu else "-> boş")
            print("Teslim edilen koliler:", teslim_edilenler)
            print("Puan:", puan)

        elif secim == "4":
            print("Kapanıyor. Toplam puan:", puan)
            break

        else:
            print("Yanlış seçim.")