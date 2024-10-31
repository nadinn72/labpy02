Latihan 3: Buat program python untuk kasus berikut:
**Soal Kasus 1: Program Pemesanan Tiket Bioskop**

Buat program yang menghitung harga tiket bioskop. Tiket reguler berharga Rp50.000,
sedangkan tiket VIP berharga Rp100.000. Jika user memiliki kartu member, mereka
mendapatkan diskon 20% dari harga tiket. Program ini harus meminta tipe tiket dan status
member dari user, lalu menghitung total harga yang harus dibayar.
Petunjuk:
● Gunakan if else dan operator ternary.

**Jawaban**
Berikut ini adalah flowchart dari kasus 1 dan langkah-langkahnya
![Bioskop](https://github.com/user-attachments/assets/8be8f816-7cdd-4820-bdc0-1458de1284aa)

1. **Mulai**  
   Program dimulai.

2. **Tampilkan menu program pemesanan tiket**  
   Program akan menampilkan menu atau pilihan untuk pemesanan tiket. Pengguna dapat melihat informasi awal dan memilih jenis tiket yang diinginkan.

3. **Input Tipe Tiket**  
   Pengguna diminta memasukkan jenis tiket yang ingin dibeli. Misalnya, tiket bisa berupa "VIP" atau "Reguler".

4. **Cek Tipe Tiket Valid atau Tidak**  
   Program akan memeriksa apakah tipe tiket yang dimasukkan adalah valid atau sesuai dengan opsi yang ada.
   - Jika **tidak valid** (misalnya pengguna salah mengetik), program akan meminta pengguna memasukkan kembali tipe tiket.
   - Jika **valid**, program akan lanjut ke langkah berikutnya.

5. **Input Status Member**  
   Pengguna diminta memasukkan status keanggotaan, apakah mereka anggota (member) atau bukan. Keanggotaan ini dapat memberi pengaruh pada harga akhir tiket.

6. **Cek Status Member Valid atau Tidak**  
   Program memeriksa apakah status member yang dimasukkan valid atau tidak.
   - Jika **tidak valid** (misalnya pengguna memasukkan data yang salah), program akan meminta pengguna memasukkan kembali status member.
   - Jika **valid**, program akan lanjut ke langkah berikutnya.

7. **Hitung Harga Tiket**  
   Program mulai menghitung harga tiket berdasarkan tipe tiket yang dipilih.

8. **Cek Apakah Tipe Tiket adalah VIP**  
   Program akan memeriksa tipe tiket:
   - Jika **VIP**, maka harga dasar tiket adalah **Rp 100.000**.
   - Jika **bukan VIP** (misalnya tipe tiket reguler), maka harga dasar tiket adalah **Rp 50.000**.

9. **Cek Apakah Pengguna adalah Member**  
   Program akan memeriksa apakah pengguna adalah anggota (member).
   - Jika **ya** (pengguna adalah member), maka pengguna akan mendapatkan **diskon sebesar 20% dari harga dasar**.
   - Jika **tidak** (pengguna bukan member), maka **diskon = 0** atau tidak ada diskon yang diberikan.

10. **Hitung Harga Akhir**  
    Program akan menghitung total harga tiket yang harus dibayar oleh pengguna dengan mengurangi harga dasar dengan diskon (jika ada). Rumusnya adalah:
    \[
    \text{Harga Akhir} = \text{Harga Dasar} - \text{Diskon}
    \]

11. **Tampilkan Detail Pembayaran**  
    Program akan menampilkan rincian pembayaran kepada pengguna, termasuk:
    - **Tipe Tiket**: Apakah tiket yang dibeli VIP atau reguler.
    - **Status Member**: Apakah pengguna adalah member atau bukan.
    - **Harga Dasar**: Harga awal tiket sebelum diskon.
    - **Diskon Member**: Jumlah diskon yang didapatkan jika pengguna adalah member.
    - **Total Pembayaran**: Jumlah akhir yang harus dibayar oleh pengguna setelah diskon.

12. **Selesai**  
    Program selesai dan transaksi pemesanan tiket selesai dilakukan.

**Soal Kasus 2: Program Kalkulator Sederhana**

Buat program kalkulator yang menerima dua angka dan satu operator aritmatika dari
pengguna (penjumlahan, pengurangan, perkalian, atau pembagian). Program akan
menghitung hasil sesuai dengan operator yang dipilih.
Petunjuk:
● Gunakan if elif else untuk menentukan operasi aritmatika.

**Jawaban**
Berikut ini adalah flowchart dari kasus 1 dan langkah-langkahnya
![kalkulator](https://github.com/user-attachments/assets/673b6f26-0764-47d5-a241-24db4459b708)

1. **Start**: Flowchart dimulai dari titik "Start".

2. **Tampilkan Judul Kalkulator**: Program menampilkan judul kalkulator, misalnya "Kalkulator Sederhana".

3. **Tampilkan Operator yang Tersedia**: Program menampilkan operator yang bisa dipilih, seperti `+`, `-`, `*`, dan `/`.

4. **Input Angka Pertama**: Pengguna memasukkan angka pertama untuk perhitungan.

5. **Validasi Input Angka Pertama**:
   - Program mengecek apakah input angka pertama valid (misalnya, apakah benar-benar angka).
   - Jika **tidak valid**, pengguna diminta memasukkan angka pertama lagi.
   - Jika **valid**, lanjut ke langkah berikutnya.

6. **Input Operator**: Pengguna memilih operator untuk operasi (misalnya, `+`, `-`, `*`, atau `/`).

7. **Input Angka Kedua**: Pengguna memasukkan angka kedua.

8. **Validasi Input Angka Kedua**:
   - Program mengecek apakah input angka kedua valid.
   - Jika **tidak valid**, pengguna diminta memasukkan angka kedua lagi.
   - Jika **valid**, lanjut ke langkah berikutnya.

9. **Cek Operator**: Program mengecek operator yang dipilih untuk menentukan jenis operasi yang akan dilakukan (penjumlahan, pengurangan, perkalian, atau pembagian).

10. **Perhitungan Berdasarkan Operator**:
    - Jika operator adalah **+**: Program menghitung penjumlahan `a + b`.
    - Jika operator adalah **-**: Program menghitung pengurangan `a - b`.
    - Jika operator adalah **\***: Program menghitung perkalian `a * b`.
    - Jika operator adalah **/**: Program mengecek apakah angka kedua (`b`) sama dengan 0:
      - Jika **`b = 0`** (pembagian dengan nol), program menampilkan pesan **"Error: Pembagian dengan nol!"** karena pembagian dengan nol tidak bisa dilakukan.
      - Jika **`b != 0`**, program menghitung hasil pembagian `a / b`.
    - Jika operator tidak sesuai dengan salah satu dari `+`, `-`, `*`, atau `/`, program menampilkan pesan **"Error: Operator tidak valid!"**.

11. **Tampilkan Hasil Perhitungan**: Setelah perhitungan selesai, program menampilkan hasil perhitungan kepada pengguna.

12. **Finish**: Program selesai dan flowchart berakhir.
