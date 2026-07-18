lll# 📊 Perhitungan SAW (Simple Additive Weightin

Script Python ini digunakan untuk menghitung dan menentukan peringkat berdarkan metode **SAW (Simple Additive Weighting)**. W adalah salah satu metode ngambilan keputusmultikrit (MCDM) yang umum nan untu
| Kr
| Ca
| Asset    | 0.
| Annn

## 🧠 Metodn
1. **N
   - **Cash & Asset**: 
   - **Age**: `nilai minimu
2. **Hitung Nilai V (skor akh
   ```
   V = (w_cash × norm_cash) + (w_ass × norm_asset) + (w_age × norm_age)
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
