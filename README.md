# Tugas Kecil 1 IF2211 Strategi Algoritma - Queens Solver

Penyelesaian Permainan Queens LinkedIn menggunakan Algoritma Brute Force (Exhaustive Search).

## a. Penjelasan Singkat
Program ini adalah aplikasi berbasis **Graphical User Interface (GUI)** yang dirancang untuk mencari solusi dari permainan logika **Queens** yang tersedia pada platform LinkedIn. Dengan menggunakan strategi **Brute Force murni (Exhaustive Search)**, program akan mengeksplorasi seluruh kemungkinan kombinasi penempatan Queen tanpa menggunakan heuristik apa pun. Program memastikan bahwa konfigurasi akhir memenuhi aturan:
1. Terdapat hanya satu Queen pada tiap baris.
2. Terdapat hanya satu Queen pada tiap kolom.
3. Terdapat hanya satu Queen pada tiap daerah warna.
4. Tidak ada dua Queen yang bersentuhan secara horizontal, vertikal, maupun diagonal (tetangga dekat).

## b. Requirement dan Instalasi
* **Python 3.8+**: Pastikan Python sudah terinstal di sistem Anda.
* **Tkinter**: Library standar Python untuk antarmuka grafis (biasanya sudah termasuk dalam instalasi Python standar).
* **Threading & Time**: Library standar Python untuk manajemen proses asinkron dan perhitungan waktu.

**Instalasi:**
Cukup unduh atau *clone* repositori ini ke komputer Anda. Tidak diperlukan instalasi library pihak ketiga karena program menggunakan library bawaan Python.

## c. Cara Mengkompilasi Program
Program ini menggunakan bahasa pemrograman **Python** yang bersifat *interpreted*, sehingga **tidak memerlukan tahap kompilasi** manual ke dalam biner. Program dapat langsung dijalankan dari kode sumbernya menggunakan interpreter Python.

## d. Cara Menjalankan dan Menggunakan
1. Buka terminal atau *command prompt*.
2. Masuk ke direktori utama proyek (`Tucil1_13524120`).
3. Jalankan perintah berikut:
   ```bash
   python src/main.py
4. Setelah jendela aplikasi muncul:
    Klik tombol "LOAD FILE" untuk memilih berkas konfigurasi papan (.txt) dari folder test.
    Klik tombol "SOLVE" untuk memulai algoritma pencarian.
    Pantau proses Live Update pada grid papan yang memvisualisasikan proses brute force secara real-time.
    Setelah solusi ditemukan, program akan menampilkan waktu eksekusi (ms) dan banyak kasus yang ditinjau.
    Jika ingin menyimpan hasil, klik "Ya" pada dialog konfirmasi untuk menyimpan solusi ke dalam berkas solusi.txt.

## e. Author
      Jonathan Alveraldo Bangun
      13524120
      Teknik Informatika
      Institut Teknologi Bandung
