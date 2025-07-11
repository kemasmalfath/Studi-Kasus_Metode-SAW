# 📊 Perhitungan SAW (Simple Additive Weighting)

Script Python ini digunakan untuk menghitung dan menentukan peringkat berdasarkan metode **SAW (Simple Additive Weighting)**. SAW adalah salah satu metode pengambilan keputusan multikriteria (MCDM) yang umum digunakan untuk menilai beberapa alternatif berdasarkan sejumlah kriteria dengan bobot tertentu.

---

## ✅ Tujuan
Menilai dan merangking beberapa orang (Andi, Budi, Cici, Dedi) berdasarkan:
- **Cash (uang tunai)** — *semakin besar semakin baik (benefit)*
- **Asset (aset)** — *semakin besar semakin baik (benefit)*
- **Age (usia)** — *semakin kecil semakin baik (cost)*

---

## 🧮 Bobot Kriteria

| Kriteria | Bobot |
|----------|--------|
| Cash     | 0.3    |
| Asset    | 0.4    |
| Age      | 0.3    |

---

## 🧠 Metodologi

1. **Normalisasi Nilai:**
   - **Cash & Asset**: `nilai / nilai maksimum`
   - **Age**: `nilai minimum / nilai`

2. **Hitung Nilai V (skor akhir):**
   \[
   V = (w_{cash} \times norm\_cash) + (w_{asset} \times norm\_asset) + (w_{age} \times norm\_age)
   \]

3. **Peringkat Alternatif:**
   - Diurutkan berdasarkan nilai `V` dari yang tertinggi ke terendah.

---

## 📄 Contoh Output

