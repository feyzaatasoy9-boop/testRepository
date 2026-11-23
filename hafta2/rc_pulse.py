pulse = int(input("RC pulse değerini gir (µs): "))
if pulse<1000 or pulse>2000:
    print("Geçersiz")
elif pulse<1300:
    print("Düşük")
elif pulse <=1700:
    print("Orta")
else:
    print("Yüksek")