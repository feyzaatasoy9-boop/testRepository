import time
import random
ZAMAN_ASIMI=3.0
BASARI_IHTIMALI=0.2
def kol_en_altta_mi():
    return random.random()<BASARI_IHTIMALI

print("Kol iniyor...")
baslangıc=time.time()
while True:
    gecen=time.time()-baslangıc
    if kol_en_altta_mi():
        print(f"Kol en altta! Süre:{gecen:.2f} sn")
        durum="GRIP_PACKAGE"
        break
    if gecen>ZAMAN_ASIMI:
        print(f"ZAMAN AŞIMI! {ZAMAN_ASIMI} sn geçti, kol takıldı.")
        durum="FAULT"
        break
    print(f" bekleniyor...{gecen:.1f} sn")
    time.sleep(0.5)
print("Yeni durum:", durum)