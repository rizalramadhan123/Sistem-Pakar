# Sistem-Pakar
Fuzzy Logic banyak diaplikasikan dalam berbagai bidang, salah satunya adalah sebagai alat bantu pengambil keputusan

* contoh nya Terdapat data penghasilan/bulan dan hutang 100 kepala keluarga. Diharuskan mencari 20
kepala keluarga paling optimum untuk mendapatkan Bantuan Langsung Tunai (BLT).
Pencarian dilakukan berdasarkan data penghasilan dan hutang yang dihitung menggunakan
algoritma Fuzzy Logic untuk memilih 20 orang dengan nilai potensi paling besar.

* Fuzzy Rules

    #1 = ya
    #2 = mungkin
    #3 = tidak

* pendapatan = hutang = potensi
tinggi = besar = mungkin
tinggi = lumayan = tidak
tinggi = sedikit = tidak
menengah = besar = ya
menangah = lumayan = mungkin
menengah = sedikit = tidak
rendah = besar = ya
rendah = lumayan = ya
rendah = sedikit = mungkin

* Range sumbu Y (0-1) menandakan poin membership dari setiap titik. Poin nol
menandakan titik tersebut tidak memiliki poin pada sumbu yang ditentukan. Poin satu
menandakan kepemilikan penuh dari setiap titik. Sumbu X menandakan persentase
terhadap pendapatan/hutang. Nol menandakan pendapatan/hutang terendah, dan satu
menandakan pendapatan/hutang tertinggi. Dengan demikian, penentuan poin
pendapatan/hutang dilakukan dengan rumus : ((xmax-xmin) * persentase ) + xmin ), untuk x =
pendapatan/hutang.
