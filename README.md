lll# 📊 Perhitungan SAW (Simple Additive Weightin

Script Python ini digunakan untuk menghitung dan menentukan peringkat berdasarkan metode **SAW (Simple Additive Weighting)**. SAW adalah salah satu metode pengambilan keputusmultikriteria (MCDM) yang umum digunakan untuk menilai beberapa alternatif berdasarkan sejumlah kriteria dengan bobot 
## ✅ Tuju
Menilai dan merangking beberapa orang (Andi, Budi, Cici, Dedi) berdasarka
- **Cash (uang tunai)** — *semakin bes sbaik (ben
- **Asset (aset)** — *semakin besar sembaik (b
- **Age (usia)** — *
## 🧮 Bobot Kriter
| Kriteria | Bob
|----------|----
| Cash     | 0.
| Asset    | 0.4    |
| Age      | 0.3    |


-
## 🧠 Metodologi

1. **Normalisasi Nilai:**
   - **Cash & Asset**: `nilai / nilai maksimum`
   - **Age**: `nilai minimum / nilai`

2. **Hitung Nilai V (skor akhir):**
   ```
   V = (w_cash × norm_cash) + (w_asset × norm_asset) + (w_age × norm_age)
   ```

3. **Peringkat Alternatif:**
   - Diurutkan berdasarkan nilai `V` dari yang tertinggi ke terendah.



## 📄 Contoh Output


===== HASIL PERHITUNGAN SAW =====
1. Cici: V = 0.924
2. Andi: V = 0.837
3. Budi: V = 0.800
4. Dedi: V = 0.645




## 🗂 Struktur Data

Data setiap orang disimpan dalam dictionary seperti berikut:

```python
data = {
    "Andi": {"cash": 100, "asset": 500, "age": 35},
    "Budi": {"cash": 200, "asset": 300, "age": 40},
    "Cici": {"cash": 150, "asset": 700, "age": 28},
    "Dedi": {"cash": 50, "asset": 200, "age": 45}
}
```



## ▶️ Cara Menjalankan

1. Pastikan Python sudah terinstall.
2. Simpan script ini sebagai `saw.py`.
3. Jalankan di terminal:
   ```bash
 saw.py
   ```



## 📚 Referensi

- Metode SAW (Simple Additive Weighting) – Metode pengambilan keputusan multikriteria berbasis pembobotan dan normalisasi.



## 🧑‍💻 Author

Script ini disusun sebagai latihan pengambilan keputusan berbasis kriteria dengan Python dan metode SAW
