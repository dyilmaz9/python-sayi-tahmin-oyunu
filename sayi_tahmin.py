import random

tutulan_sayi = random.randint(1, 100)
hak = 5
tahmin_sayisi = 0

print("1 ile 100 arasında bir sayı tuttum!")
print("5 hakkın var, bol şans 😄")

while hak > 0:
    tahmin = int(input("Tahminin: "))
    tahmin_sayisi += 1

    if tahmin < tutulan_sayi:
        hak -= 1
        print("Daha büyük bir sayı dene 🔼")
    elif tahmin > tutulan_sayi:
        hak -= 1
        print("Daha küçük bir sayı dene 🔽")
    else:
        print("🎉 Tebrikler! Sayıyı doğru tahmin ettin!")
        print(f"Toplam tahmin sayısı: {tahmin_sayisi}")
        break

    print(f"Kalan hak: {hak}")

if hak == 0:
    print("❌ Hakkın bitti! Kaybettin.")
    print(f"Tutulan sayı: {tutulan_sayi}")
    print(f"Toplam tahmin sayısı: {tahmin_sayisi}")