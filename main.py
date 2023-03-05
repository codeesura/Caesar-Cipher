kelimeler = ['ONE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE', 'TEN', 'ELEVEN', 'TWELVE']
anahtarlar = [5, 8, 3, 2, 7, 1, 9, 4, 6, 0, 11, 10]

# Her kelimeyi şifreliyoruz
sifreli_kelimeler = []
for i, kelime in enumerate(kelimeler):
    anahtar = anahtarlar[i] % 26  # Anahtar, 26'ya bölünerek mod alınarak 0-25 arasında bir sayıya çevrilir.
    sifreli_harf_listesi = []
    for harf in kelime:
        # Harfleri anahtar kadar kaydırıyoruz
        sifreli_harf_ascii = ord(harf) + anahtar
        # 'Z' harfinden sonra 'A' harfine dönmek için mod 26 kullanıyoruz
        if harf.isupper():
            sifreli_harf = chr((sifreli_harf_ascii - 65) % 26 + 65)
        else:
            sifreli_harf = chr((sifreli_harf_ascii - 97) % 26 + 97)
        sifreli_harf_listesi.append(sifreli_harf)
    sifreli_kelimeler.append("".join(sifreli_harf_listesi))

print(sifreli_kelimeler)
