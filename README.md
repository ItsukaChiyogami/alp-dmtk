# Implementasi Teori Graf Menggunakan Python

## Deskripsi Proyek
Proyek ini bertujuan untuk membuat sistem berbasis Python untuk mempelajari teori graf menggunakan library **NetworkX**. Sistem ini mendukung operasi dasar seperti:

- Menambah node dan edge
- Mengecek keterhubungan graf
- Menghitung jalur terpendek
- Menampilkan visualisasi graf

## Fitur Utama

1. **Menambah Node**
   Tambahkan node baru ke dalam graf.

2. **Menambah Edge**
   Hubungkan dua node dengan bobot tertentu.

3. **Visualisasi Graf**
   Tampilkan graf dengan edge dan bobotnya.

4. **Jalur Terpendek**
   Hitung jalur terpendek antara dua node berdasarkan bobot edge.

5. **Visualisasi Jalur Terpendek**
   Tampilkan jalur terpendek di atas visualisasi graf.

6. **Metode Tambahan**:
   - Mengecek apakah graf terhubung.
   - Menghitung derajat node tertentu.
   - Menampilkan koefisien clustering untuk setiap node.
   - Menghitung jalur terpendek untuk semua pasangan node.
   - Menampilkan pohon rentang minimum.

## Cara Menjalankan Program

### Prasyarat
1. **Python 3.x** harus terinstal. Unduh dari [python.org](https://www.python.org/).
2. Instalasi pustaka yang diperlukan:
   ```bash
   pip install networkx matplotlib
   ```

### Langkah-langkah
1. Clone repositori atau salin kode ke file Python, misalnya `graf.py`.
2. Jalankan file menggunakan perintah berikut di terminal:
   ```bash
   python graf.py
   ```
3. Output akan menampilkan analisis graf, jalur terpendek, dan visualisasi graf.

## Contoh Penggunaan

### Menambah Node dan Edge
Kode berikut menambahkan node dan edge ke graf:
```python
# Membuat objek graf
graph = Graf()

# Menambah node
graph.add_node(1)
graph.add_node(2)

# Menambah edge dengan bobot
graph.add_edge(1, 2, weight=4.5)
```

### Visualisasi Graf
Untuk menampilkan graf:
```python
graph.visualize_graph()
```

### Jalur Terpendek
Untuk menghitung dan menampilkan jalur terpendek antara dua node:
```python
path = graph.shortest_path(1, 2)
print("Jalur terpendek:", path)
graph.visual_shortest_path(1, 2)
```

## Hasil Visualisasi
Program ini menghasilkan visualisasi graf lengkap dengan bobot edge dan jalur terpendek yang ditandai dalam warna merah.

## Lisensi
Proyek ini dilisensikan di bawah lisensi MIT. Silakan gunakan dan modifikasi sesuai kebutuhan.

---
**Dibuat oleh:**
- Nama: [Isi Nama Anda]
- Proyek untuk: Discrete Mathematics - Implementasi Teori Graf
