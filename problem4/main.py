def ubah_huruf(sentence) :
    alphabet_bob = "KLMNOPQRSTUVWXYZABCDEFGHIJ"
    pattern = ""
    for char in sentence :
        if char.isalpha() :
            index = ord(char.upper()) - ord('A')
            enkripsi_char = alphabet_bob[index]
            pattern += enkripsi_char
        else :
            pattern += char
    return pattern

if __name__ == '__main__':
    print(ubah_huruf("SEPULSA OKE")) # COZEVCK YUO
    print(ubah_huruf("ALTERRA ACADEMY")) # KVDOBBK KMKNOWI
    print(ubah_huruf("INDONESIA")) # SXNYXOCSK
    print(ubah_huruf("GOLANG")) # QYVKXQ
    print(ubah_huruf("PROGRAMMER")) # ZBYQBKWWOB
