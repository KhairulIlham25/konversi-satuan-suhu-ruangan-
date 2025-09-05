from utils import konversi_suhu

print("=== KONVERSI SUHU ===")

#input dari user
try:
    nilai = float(input("Masukkan nilai suhu: ").strip())
except ValueError:
    print("Nilai suhu harus berupa angka.")
    exit()
satuan_asal = input("Dari satuan (C/F/K): ").strip()
satuan_tujuan = input("Ke satuan (C/F/K): ").strip()

#konversi suhu
hasil = konversi_suhu(nilai, satuan_asal, satuan_tujuan)

#tampilkan hasil
if isinstance(hasil, str):
    print(hasil)
else:
    print(f"asil: {nilai} {satuan_asal.upper()} = {hasil:.1f} {satuan_tujuan.upper()}")