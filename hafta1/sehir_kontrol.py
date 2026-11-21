sehirler={
    "ankara":False,
    "bursa":False,
    "konya":False,
    "adana":False,
    "samsun":False,
}
while True:
 print("\n--- TESLİMAT MENÜSÜ ---")
 print("1) Şehirlerin durumunu göster")
 print("2) Koli teslim et")
 print("3) Çıkış")
 print("4) Puanı göster") 

 secim=input("Seçimin:")
 if secim=="1":
  for sehir,dolu in sehirler.items():
    if dolu:
      print(sehir,"->DOLU")
    else:
      print(sehir,"-> boş")

 elif secim=="2":
   hedef=input("Hangi şehre?".strip().lower())
   if hedef not in sehirler:
     print("GEÇERSİZ SEHİR",hedef)
   else:
     sehirler[hedef] = True
     puan = puan + 15
     print("TESLİM EDİLDİ:", hedef, "(+15 puan)")
     if all(sehirler.values()):
        print("TÜM ŞEHİRLER DOLU! Görev tamamlandı.")


 elif secim=="3":
   print("Çıkılıyor...")
   break
 else:
   print("Yanlış seçim.")