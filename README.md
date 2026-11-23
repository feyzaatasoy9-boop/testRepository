# Robolig

Benim Robolig öğrenme repom. Her haftanın çalışmaları kendi klasöründe duruyor.

## Klasör yapısı

```
Robolig/
├── hafta1/                  Python temelleri
│   ├── merhaba_robot.py     Değişkenler ve print
│   ├── menu.py              while döngüsü, input, if/elif/else, liste
│   ├── sehir_kontrol.py     Şehir teslimat menüsü (sözlük kullanımı)
│   ├── map_uid.py           Koli UID → şehir eşleştirme ve karar mantığı
│   ├── map_uid_test.py      map_uid.py için 10 test
│   ├── test_sonuclari.txt   Test çıktısı (10/10 geçti)
│   ├── kurulum.md           Kurulum notları ve karşılaştığım hatalar
│   ├── senaryolar.md        Şehir kontrol test senaryoları
│   └── gorseller/           Ekran görüntüleri
└── hafta2/
    └── zaman_asimi.py       Robot kolu için zaman aşımı kontrolü
```

## Çalıştırma

```bash
cd hafta1
python3 merhaba_robot.py
python3 map_uid.py          # robot menüsü
python3 map_uid_test.py     # testleri çalıştırır

cd ../hafta2
python3 zaman_asimi.py
```
