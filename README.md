# **LIBRARY MANAGEMENT SYSTEM (LMS) SEDERHANA**

## Learning Objective
1. Membuat program LMS menggunakan Python
2. Membuat program python yang dapat terhubung ke database relational
3. Mengaplikasikan pembuatan program dengan paradigma pemrograman berbasis
4. fungsi atau pemrograman berbasis objek
5. Mengaplikasikan penulisan kode yang bersih (mengacu ke PEP 8)

## Deskripsi task
1. membuat fungsi koneksi antara python dan mysql
- user dan password harus disesuaikan dengan yang ada di local sendiri
2. fungsi membuat database
3. funsi mebuat koneksi dengan database
4. membuat kursor
5. membuat table user, buku, peminjam dan stock
6. membuat fungsi pendaftaran baru:
- fungsi akan menerima input dan memasukan data user ke table_user dan meng-autogenerate id_user
7. membuat fungsi pendaftaran buku:
- fungsi akan menerima input dari user dan memasukan data ke table buku
8. membuat fungsi peminjaman:
- fungsi akan meminta id user, nama user, kode buku dan judul buku yang akan dipinjam, jumlah buku yang akan dipinjam, tanggal pengembalian
- jika buku berhasil dipinjam maka data user akan ada di daftar peminjaman dan stock buku akan berkurang
- id_peminjaman bisa dilihat di daftar peminjaman
9. membuat fungsi menampilkan daftar buku:
- fungsi akan menampilkan informasi buku seperti: kode buku, judul buku, kategori dan stok
10. membuat fungsi menampilkan datar user:
- fungsi akan menampilkan informasi user seperti: id user, nama, umur, pekerjaan, alamat, tanggal bergabung
11. membuat fungsi menampilkan daftar peminjaman:
- fungsi akan menampilkan informasi setiap peminjaman seperti: id peminjaman, id user, nama user, kode buku, nama buku, jumlah buku yg dipinjam, tanggal peminjaman dan pengembalian
12. membuat fungsi pengembalian:
- fungsi akan menerima input data
- jika buku berhasil dikembalikan data user akan dihapus dari daftar peminjaman dan stok buku akan kembali bertambah
13. fungsi pencarian buku:
- fungsi akan menerima input dari user lalu menampilkan data buku yang sesuai
14. fungsi main:
- fungsi ini dibuat untuk menampilkan menu dam dapat menerima input sebagai perintah dari user 

## Cara Running
1. run `./lms_main.py` di terminal
2. user harus menyesuaikan user dan password mysql sendiri sebelum running

## Saran Perbaikan
1. output dari program ini belum berupa tabel
2. code belum terlalu rapih
