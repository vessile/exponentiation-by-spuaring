def ters_cevir(metin):
    sayac = 0
    sonuc = ""
    for i in range(len(metin) - 1, -1, -1):
        sonuc += metin[i]
        sayac += 1
    print("İşlenen karakter:", sayac)
    return sonuc


def ters_cevir_index(metin):
    sayac = 0
    sonuc = ""
    for i in range(len(metin)):
        sonuc += metin[len(metin) - 1 - i]
        sayac += 1
    print("İşlenen karakter:", sayac)
    return sonuc


def ters_cevir_while(metin):
    sayac = 0
    sonuc = ""
    i = len(metin) - 1
    while i >= 0:
        sonuc += metin[i]
        sayac += 1
        i -= 1
    print("İşlenen karakter:", sayac)
    return sonuc

def testler():
    test_metinler = [
        "a",
        "ab",
        "abc",
        "12345",
        "Python",
        "",
        " ",
        "Veri Yapıları",
        "123abc",
        "!!!",
        "Uzun bir cümle",
        "BÜYÜK HARF",
        "küçük harf",
        "1234abcDEF",
        "abcdefghijklmnopqrstuvwxyz" * 4
    ]

    for metin in test_metinler:
        print("Orijinal:", metin)
        print("ters_cevir:", ters_cevir(metin))
        print("ters_cevir_index:", ters_cevir_index(metin))
        print("ters_cevir_while:", ters_cevir_while(metin))
        print("-" * 30)

  def main():
    metin = input("Metni giriniz: ")
    print("Ters hali:", ters_cevir(metin))


if __name__ == "__main__":
    testler()
    main()
  # Zaman karmaşıklığı: O(n)
# Neden: Her karakter bir kez işlenir.
# Bellek karmaşıklığı: O(n)
# Daha hızlı yöntem: Yok, tüm karakter okunmalı.
