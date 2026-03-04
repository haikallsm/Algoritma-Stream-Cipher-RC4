def ksa(key_bytes):
    S = list(range(256))
    j = 0
    keylen = len(key_bytes)
    for i in range(256):
        j = (j + S[i] + key_bytes[i % keylen]) & 0xFF
        S[i], S[j] = S[j], S[i]
    return S

def prga(S):
    i = j = 0
    while True:
        i = (i + 1) & 0xFF
        j = (j + S[i]) & 0xFF
        S[i], S[j] = S[j], S[i]
        K = S[(S[i] + S[j]) & 0xFF]
        yield K

def rc4(key: bytes, data: bytes) -> bytes:
    S = ksa(key)
    stream = prga(S)
    return bytes([b ^ next(stream) for b in data])

def to_hex(b: bytes) -> str:
    return b.hex()

def from_hex(s: str) -> bytes:
    return bytes.fromhex(s)

def menu():
    print(" Pilih Mode:")
    print(" 1. Enkripsi")
    print(" 2. Dekripsi")
    print(" 3. Keluar")

def formEnkripsi():
    while True:
        key = input("Masukkan Kunci : ")
        if key:
            break
        print("Kunci tidak boleh kosong")

    while True:
        plaintext = input("Masukkan Plaintext : ")
        if plaintext:
            break
        print("Plaintext tidak boleh kosong")
    
    try:
        keyBytes = key.encode('utf-8')
        ct = rc4(keyBytes, plaintext.encode('utf-8'))

        print(f"Key         : {key}")
        print(f"Plaintext   : {plaintext}")
        print(f"Ciphertext  : {to_hex(ct)}")
    
    except Exception as e:
        print(f"error: {e}")

def formDekripsi():
    while True:
        key = input("Masukkan Kunci     : ")
        if key:
            break
        print("Kunci tidak boleh kosong")

    while True:
        ciphertext = input("Masukkan Ciphertext : ")
        if not ciphertext:
            print("Ciphertext tidak boleh kosong")
            continue
        try:
            from_hex(ciphertext)
            break
        except ValueError:
            print("Ciphertext salah")

    try:
        keyBytes = key.encode('utf-8')
        ct = from_hex(ciphertext)
        pt = rc4(keyBytes, ct)
        hasil = pt.decode('utf-8', errors='replace')

        print(f"Key         : {key}")
        print(f"Ciphertext  : {ciphertext}")
        print(f"Plaintext   : {hasil}")
    
    except Exception as e:
        print(f"error: {e}")

def main():
    while True:
        menu()

        choice = input(" Pilih (1/2/3): ").strip()

        if choice == '1':
            formEnkripsi()
        elif choice == '2':
            formDekripsi()
        elif choice =='3':
            break
        else:
            print('pilihan tidak valid, coba lagi')

if __name__ == "__main__":
    main()