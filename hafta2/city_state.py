# city_state.py
# Hafta 2 teslimi: 5 şehrin dolu/boş durumunu tutar,
# hedefin geçerli olup olmadığına karar verir.

sehir_durum = {
    "Ankara": "boş",
    "İzmir": "boş",
    "Bursa": "boş",
    "Konya": "boş",
    "Adana": "boş",
}

print("Teslimat simülasyonu. Çıkmak için 'q' yaz.")

while True:
    hedef = input("\nHedef şehir: ").strip().title()

    if hedef == "Q":
        print("Çıkılıyor.")
        break

    if hedef == "":
        print("HATA: Boş giriş")
    elif hedef not in sehir_durum:
        print("GEÇERSİZ: Bilinmeyen şehir →", hedef)
    elif sehir_durum[hedef] == "dolu":
        print("REDDEDİLDİ:", hedef, "zaten dolu, puan yok")
    else:
        sehir_durum[hedef] = "dolu"
        print("TESLİM EDİLDİ:", hedef, "(+15 puan)")

    # Her denemeden sonra güncel tablo
    dolu_sayisi = 0
    for sehir, d in sehir_durum.items():
        print("  ", sehir, "→", d)
        if d == "dolu":
            dolu_sayisi += 1
    print("Dolu:", dolu_sayisi, "/", len(sehir_durum))

    if dolu_sayisi == len(sehir_durum):
        print("Tüm şehirler dolu, görev bitti!")
        break