# Caesar Cipher Encryption Method

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)

The Caesar Cipher is a simple encryption technique that is often used to encode messages by shifting the letters in the message by a certain number of positions. This implementation uses a key generated by a list of integers to shift each letter in the message by a specific amount.

## Usage

The code can be used to encrypt a list of words using the Caesar Cipher method. To do this, simply provide a list of words and a list of integers as the encryption key. The key list should have the same length as the word list, and each integer in the key list represents the number of positions by which the corresponding word in the word list should be shifted.

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

The output of the code will be a list of encrypted words.

## Explanation

In the code, each word in the input list is encrypted by shifting each letter in the word by a certain number of positions. This number is determined by the corresponding integer in the key list.

For example, the word 'ONE' is encrypted using the integer 5 as the key. This means that each letter in the word is shifted 5 positions to the right. So 'O' becomes 'T', 'N' becomes 'S', and 'E' becomes 'J'. The resulting encrypted word is 'TJS'.

Similarly, the word 'TWO' is encrypted using the integer 8 as the key. This means that each letter in the word is shifted 8 positions to the right. So 'T' becomes 'C', 'W' becomes 'E', and 'O' becomes 'W'. The resulting encrypted word is 'CEW'.

This process is repeated for each word in the input list, resulting in a list of encrypted words.

## Requirements

- Python


## Installation

`git clone https://github.com/username/project-name.git`

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.
