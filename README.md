# Dokumentasi Algoritma Stream Cipher RC4

Repositori ini berisi implementasi sederhana dari algoritma kriptografi RC4 (Rivest Cipher 4) menggunakan bahasa pemrograman Python. Kode ini dirancang untuk mensimulasikan bagaimana teks biasa (*plaintext*) dapat diubah menjadi teks rahasia (*ciphertext*) dan sebaliknya menggunakan metode sandi aliran (*stream cipher*).

### Langkah-Langkah Eksekusi Kode

Program ini menjalankan urutan logika sebagai berikut:

1.  **Inisialisasi Key Scheduling Algorithm (KSA)**: Program mendefinisikan fungsi `ksa` untuk membuat array `S` (berisi nilai 0-255) dan mengacak array tersebut menggunakan kunci rahasia (*key*) yang diberikan.
2.  **Pembangkitan Keystream (PRGA)**: Program menggunakan fungsi `prga` (*Pseudo-Random Generation Algorithm*) untuk memproses array `S` yang telah diacak agar dapat menghasilkan deretan byte acak (*keystream*) secara terus-menerus menggunakan perintah `yield`.
3.  **Menu Interaktif**: Program menampilkan antarmuka berbasis CLI yang meminta pengguna memilih mode: Enkripsi, Dekripsi, atau Keluar.
4.  **Proses Enkripsi**:
    * Pengguna diminta memasukkan Kunci dan *Plaintext*.
    * Kunci dan teks diubah menjadi format bit/byte menggunakan *encoding* UTF-8.
    * Program mengeksekusi fungsi utama `rc4`, yang melakukan operasi XOR antara setiap bit data asli dengan bit *keystream*.
    * Hasilnya dikonversi menjadi string heksadesimal menggunakan fungsi `to_hex` agar *Ciphertext* dapat dibaca di layar terminal.
5.  **Proses Dekripsi**:
    * Pengguna diminta memasukkan Kunci dan *Ciphertext* dalam format heksadesimal.
    * *Ciphertext* heksadesimal dikembalikan ke bentuk bit/byte menggunakan fungsi `from_hex`.
    * Karena RC4 bersifat simetris, program kembali memanggil fungsi `rc4` untuk melakukan operasi XOR ulang antara data tersandi dengan *keystream*.
    * Hasil bit didekode kembali menjadi format teks UTF-8, dengan penanganan *error* untuk memproses kegagalan dekripsi jika kunci salah.

## Cara Menjalankan Program

### Prasyarat
Pastikan Anda telah menginstal **Python** (direkomendasikan versi 3.6 ke atas) di perangkat Anda. Anda dapat mengeceknya dengan menjalankan `python --version` di terminal.

### Instruksi Menjalankan
1. Buka Terminal (Linux/Mac) atau Command Prompt / PowerShell (Windows).
2. Arahkan (*navigate*) ke direktori tempat Anda menyimpan file `RC4.py`.
3. Jalankan skrip dengan perintah berikut:
   ```bash
   python RC4.py
