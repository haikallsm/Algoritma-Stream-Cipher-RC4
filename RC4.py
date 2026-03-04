# func KSA atau Key Scheduling Algorithm digunakan untuk mengacak array s menggunakan key
def ksa(key_bytes):
    S = list(range(256)) # inisialisasi S sebagai array 0-255
    j = 0
    keylen = len(key_bytes)
    for i in range(256): 
        j = (j + S[i] + key_bytes[i % keylen]) & 0xFF # J lama + S[i] + nilai key posisi i mod panjang dari key, lalu di mod lagi denga 256
        S[i], S[j] = S[j], S[i] # digunakan untuk mengacak array S
    return S

# PRGA atau Pseudo-Random Generation Algorithm berfungsi untuk menghasilkan keystream atau deretan byte acak dari arrat S yang sudah diacak sebelumnya oleh KSA
def prga(S):
    i = j = 0 
    while True: 
        i = (i + 1) & 0xFF # geser i maju 1, lalu muter kembali ke 0 setelah 255
        j = (j + S[i]) & 0xFF # geser j berdasarkan nilai S[i] saat ini
        S[i], S[j] = S[j], S[i] # tukar S[i] dan S[j] untuk terus mengacak array S
        K = S[(S[i] + S[j]) & 0xFF] # ambil bit keystream dari posisi gabungan S[i] + S[j]
        yield K # yield digunakan untuk mengembalikan nilai K tapi fungsinya tidak berhenti, akan lanjut ke iterasi selanjutnya jika next() dipanggil lagi

# Ini adalah fungsi utama yang menggabungkan KSA dan PRGA untuk enkripsi atau dekripsi 
def rc4(key: bytes, data: bytes) -> bytes:
    S = ksa(key) # panggil KSA untuk mengacak array S berdasarkan key
    stream = prga(S) # generator keystream dari S hasil KSA
    return bytes([b ^ next(stream) for b in data]) # XOR setiap bit data dengan bit keystream berikutnya

# buat ngeconvert bit ke str hexadecimal untuk menampilkan ciphertext agar bisa dibaca
def to_hex(b: bytes) -> str: 
    return b.hex()

# buat ngeconvert str hexadecimal kembali ke bit, ini untuk proses dekripsi
def from_hex(s: str) -> bytes:
    return bytes.fromhex(s)

def menu():
    print(" Pilih Mode:")
    print(" 1. Enkripsi")
    print(" 2. Dekripsi")
    print(" 3. Keluar")

# fungsi inputan enkripsi 
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
        keyBytes = key.encode('utf-8') # buat ubah str key jadi bit menggunakan encoding utf-8 karena kriptografi beroperasi pada level bit bukan string
        ct = rc4(keyBytes, plaintext.encode('utf-8')) # manggil fungsi rc4 untuk ngubah teks asli jadi bit

        print(f"Key         : {key}")
        print(f"Plaintext   : {plaintext}")
        print(f"Ciphertext  : {to_hex(ct)}") # buat nampilkan hasil convert enkripsi dari data bit ke str hexadecimal agar bisa dibaca
    
    except Exception as e:
        print(f"error: {e}")

# fungsi inputan dekripsi
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
        keyBytes = key.encode('utf-8') # sama seperti enkripsi, ini buat ubah str key jadi bit menggunakan encoding utf-8
        ct = from_hex(ciphertext) # buat ubah str hexadecimal yg diinput jadi bit untuk proses dekripsi
        pt = rc4(keyBytes, ct) # panggil fungsi rc4 untuk ngubah ciphertext yang sudah diubah jadi bit kembali ke bentuk plaintext, karena RC4 itu simetris jadi proses enkripsi dan dekripsi sama saja, yang membedakan hanya input datanya saja
        hasil = pt.decode('utf-8', errors='replace') # buat ubah hasil dekripsi yang masih dalam bentuk bit jadi str, karena hasil dekripsi bisa jadi tidak valid utf-8 jika key salah, maka gunakan parameter errors='replace' untuk mengganti karakter yang tidak bisa didecode agar program tidak error saat mencoba mendecode bit yang tidak valid

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