# Sezar Şifreleme Yöntemi

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)

Sezar Şifreleme, genellikle mesajları belirli bir pozisyon sayısı kadar harfleri kaydırarak kodlamak için kullanılan basit bir şifreleme tekniğidir. Bu uygulama, bir liste tamsayılarla oluşturulan bir anahtar kullanarak her harfi belirli bir miktarda kaydırmak için kullanır.

## Sezar Şifreleme Yöntemi

Sezar şifreleme yöntemi, adını Romalı İmparator Jül Sezar'dan almaktadır ve basit bir şifreleme yöntemidir. Bu yöntemde, bir mesajın her harfi belirli bir sayı kadar kaydırılır ve şifreli mesaj oluşturulur. Şifreli mesajı çözmek için ise aynı sayı kadar geriye kaydırmak yeterlidir.

Örneğin, mesajımız "MERHABA" olsun ve her harfi 3 harf ileri kaydıralım. Böylece şifreli mesajımız "PHUKDEĞ" olacaktır.

Bu yöntem oldukça basit olduğundan, kolaylıkla çözülebilir ve güvenli bir şifreleme yöntemi değildir. Ancak tarihte askeri haberleşme ve diplomatik yazışmalarda kullanılmıştır.

## Kullanım

Kod, Sezar Şifreleme yöntemini kullanarak bir kelime listesini şifrelemek için kullanılabilir. Bunun için sadece bir kelime listesi ve bir tamsayı listesi sağlayın. Anahtar listesi, kelime listesiyle aynı uzunluğa sahip olmalıdır ve anahtar listesindeki her tamsayı, kelime listesindeki karşılık gelen kelimenin kaç pozisyona kaydırılması gerektiğini temsil eder.

```Python
kelimeler = ['ONE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE', 'TEN', 'ELEVEN', 'TWELVE']
anahtarlar = [5, 8, 3, 2, 7, 1, 9, 4, 6, 0, 11, 10]

# Encrypt each word
sifreli_kelimeler = []
for i, kelime in enumerate(kelimeler):
    anahtar = anahtarlar[i] % 26  
    sifreli_harf_listesi = []
    for harf in kelime:
        sifreli_harf_ascii = ord(harf) + anahtar
        if harf.isupper():
            sifreli_harf = chr((sifreli_harf_ascii - 65) % 26 + 65)
        else:
            sifreli_harf = chr((sifreli_harf_ascii - 97) % 26 + 97)
        sifreli_harf_listesi.append(sifreli_harf)
    sifreli_kelimeler.append("".join(sifreli_harf_listesi))

print(sifreli_kelimeler)
```

Kodun çıktısı şifrelenmiş kelimelerin bir listesi olacaktır.

## Açıklama

Koddaki her kelime, belirli bir pozisyon sayısı kadar her harfi kaydırarak şifrelenir. Bu sayı, anahtar listesindeki karşılık gelen tamsayı tarafından belirlenir.

Örneğin, 'BİR' kelimesi anahtar olarak kullanılan 5 ile şifrelenir. Bu, kelime içindeki her harfin sağa doğru 5 pozisyona kaydırılması anlamına gelir. Böylece, 'B' 'G' olur, 'İ' 'N' olur ve 'R' 'W' olur. Sonuçta şifrelenmiş kelime 'GNW' olacaktır .Benzer şekilde, 'İKİ' kelimesi 8 ile şifrelenir. Bu, kelime içindeki her harfin sağa doğru 8 pozisyona kaydırılması anlamına gelir. Böylece, 'İ' 'Q' olur, 'K' 'S' olur ve 'İ' 'Q' olur. Sonuçta şifrelenmiş kelime 'QSÇ' olacaktır.

Bu işlem girdi listesindeki her kelime için tekrarlanır ve şifrelenmiş kelimelerin bir listesi oluşur.

## Gereksinimler

- Python


## Kurulum

`git clone https://github.com/username/project-name.git`

## Lisans

Bu proje, ayrıntılar için LICENSE.md dosyasına bakınız, MIT Lisansı altında lisanslanmıştır.

