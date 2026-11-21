from map_uid import koli_karari, teslim_et, bos_sehirler

sonuclar = []

def kontrol(no, aciklama, gercek, beklenen):
    durum = "PASS" if gercek == beklenen else "FAIL"
    print(no, aciklama, "| beklenen:", beklenen, "| gerçek:", gercek, "|", durum)
    sonuclar.append(durum == "PASS")


# Başlangıç: bütün şehirler boş, hiç teslim yok
sehirler = bos_sehirler()
teslim = set()

# 1-4: Okuma ve tanıma
kontrol(1, "geçerli UID", koli_karari("04A31F7C", sehirler, teslim), ("GOTUR", "ankara"))
kontrol(2, "boşluklu/küçük harf", koli_karari("04 a3 1f 7c", sehirler, teslim), ("GOTUR", "ankara"))
kontrol(3, "sahte koli", koli_karari("04FF0001", sehirler, teslim), ("GECERSIZ", None))
kontrol(4, "boş okuma", koli_karari("", sehirler, teslim), ("OKUMA_HATASI", None))

# 5: Ankara'ya teslim et, sonra aynı koli tekrar okunsun
teslim_et("04A31F7C", "ankara", sehirler, teslim)
kontrol(5, "aynı koli tekrar", koli_karari("04A31F7C", sehirler, teslim), ("ZATEN_TESLIM", "ankara"))

# 6: Rakip Bursa'yı doldurdu
sehirler["bursa"] = True
kontrol(6, "rakip doldurdu", koli_karari("04B22E11", sehirler, teslim), ("SEHIR_DOLU", "bursa"))

# 7: Tamamen uydurma UID
kontrol(7, "uydurma UID", koli_karari("12345678", sehirler, teslim), ("GECERSIZ", None))

# 8: Başka geçerli koli hâlâ gidebiliyor mu?
kontrol(8, "konya kolisi", koli_karari("04C93A55", sehirler, teslim), ("GOTUR", "konya"))

# 9: Şehirlerin son durumu
kontrol(9, "şehir durumu", sehirler,
        {"ankara": True, "bursa": True, "konya": False, "adana": False, "samsun": False})

# 10: Altın kural — dolu şehre asla "GOTUR" denmemeli
yanlis = 0
for uid in ["04A31F7C", "04B22E11"]:
    karar, _ = koli_karari(uid, sehirler, teslim)
    if karar == "GOTUR":
        yanlis = yanlis + 1
kontrol(10, "dolu şehre gönderim yok", yanlis, 0)

print("\nSONUÇ:", sum(sonuclar), "/", len(sonuclar), "test geçti")