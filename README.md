# 🧠 Sistem Pakar Diagnosa Awal Penyakit Ginjal  
**Metode Forward Chaining – Berbasis Streamlit**

## 📌 Deskripsi
Aplikasi ini merupakan **sistem pakar diagnosa awal penyakit ginjal** yang dibangun menggunakan bahasa pemrograman **Python** dan framework **Streamlit**.  
Sistem ini menerapkan metode **Forward Chaining** untuk menentukan kemungkinan penyakit ginjal berdasarkan gejala yang dipilih oleh pengguna.

Aplikasi ditujukan sebagai **alat bantu diagnosa awal**, bukan sebagai pengganti tenaga medis profesional.

---

## 🎯 Tujuan Sistem
- Membantu pengguna mengenali kemungkinan penyakit ginjal secara dini  
- Mengimplementasikan metode **Forward Chaining** dalam sistem pakar  
- Memberikan contoh penerapan aturan **IF–THEN** berbasis gejala  
- Menjadi media pembelajaran sistem pakar berbasis web

---

## 🧠 Metode yang Digunakan
### Forward Chaining
Forward Chaining adalah metode inferensi yang bekerja dengan cara:
- Memulai dari **fakta awal (gejala yang dipilih pengguna)**
- Mencocokkannya dengan **aturan (rules)**
- Menarik **kesimpulan berupa penyakit**

Aturan menggunakan operator **AND**, artinya **seluruh gejala dalam satu rule harus terpenuhi** agar penyakit dapat disimpulkan.

---

## 🗂️ Basis Pengetahuan (Knowledge Base)

### 1. Daftar Penyakit
| Kode | Nama Penyakit |
|-----|--------------|
| PG1 | Infeksi Ginjal |
| PG2 | Batu Ginjal |
| PG3 | Gagal Ginjal Akut |
| PG4 | Gagal Ginjal Kronis |
| PG5 | Nefropati Diabetik |
| PG6 | Sindrom Nefrotik |

### 2. Daftar Gejala
Gejala diberi kode **G1 – G27** agar memudahkan proses inferensi dan demonstrasi sistem.

Contoh:
- G1 : Bau urine tidak normal  
- G2 : Sakit pinggang  
- G20 : Urine berbusa  
- G27 : Berat badan bertambah akibat penumpukan cairan  

(Keseluruhan daftar gejala terdapat di dalam source code)

---

## ⚙️ Cara Kerja Sistem
1. Pengguna memilih gejala melalui checkbox
2. Sistem mengumpulkan gejala terpilih sebagai fakta awal
3. Mesin inferensi mencocokkan fakta dengan rule
4. Jika semua gejala dalam satu rule terpenuhi → penyakit ditampilkan
5. Jika tidak ada rule yang cocok → sistem menampilkan pesan gagal diagnosa

---

## 🖥️ Tampilan Aplikasi
- Checkbox menampilkan **kode gejala + deskripsi**
- Tombol **Diagnosa Penyakit**
- Menampilkan:
  - Gejala yang dipilih
  - Hasil diagnosa (jika ada)

---

## 🚀 Cara Menjalankan Aplikasi
### 1. Clone Repository
```bash
git clone https://github.com/username/nama-repository.git
cd nama-repository
