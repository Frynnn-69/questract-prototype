import cv2
import numpy as np

FILE_NAME = 'test_images/template_kuesioner_2.jpg'

KOTAK_TERCENTANG = (190, 200, 30, 30) # "Laki-laki"
KOTAK_KOSONG = (330, 200, 30, 30)    # "Perempuan"

SHRINK_FACTOR = 0.8
# [PERUBAHAN] Menurunkan ambang batas ke nilai yang lebih aman setelah kalibrasi.
AMBANG_BATAS_PIKSEL_HITAM = 40

# --- FUNGSI UTAMA (VERSI 3.0) ---

def analisis_checkbox(gambar, koordinat):
    """
    Fungsi untuk menganalisis checkbox dengan tambahan langkah pembersihan gambar.
    """
    # 1. Potong gambar & susutkan area
    x, y, w, h = koordinat
    area_kotak_awal = gambar[y:y+h, x:x+w]
    shrink_w = int(w * SHRINK_FACTOR)
    shrink_h = int(h * SHRINK_FACTOR)
    offset_x = (w - shrink_w) // 2
    offset_y = (h - shrink_h) // 2
    area_dalam = area_kotak_awal[offset_y:offset_y+shrink_h, offset_x:offset_x+shrink_w]

    # 2. Grayscale & Thresholding Adaptif
    grayscale = cv2.cvtColor(area_dalam, cv2.COLOR_BGR2GRAY)
    biner = cv2.adaptiveThreshold(
        grayscale, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY_INV, 11, 2
    )

    # 3. [LANGKAH BARU] Pembersihan Gambar (Operasi Morfologis "Opening")
    # Kernel ini seperti ukuran 'mata amplas' kita
    kernel = np.ones((2,2), np.uint8)
    gambar_bersih = cv2.morphologyEx(biner, cv2.MORPH_OPEN, kernel)

    # 4. Hitung piksel putih pada gambar yang SUDAH BERSIH
    jumlah_piksel_putih = cv2.countNonZero(gambar_bersih)

    return jumlah_piksel_putih, biner, gambar_bersih

# --- EKSEKUSI SKRIP ---

img = cv2.imread(FILE_NAME)
if img is None:
    print(f"ERROR: File '{FILE_NAME}' tidak ditemukan.")
    exit()

# Analisis kedua kotak
jumlah_putih_tercentang, img_biner_tc, img_bersih_tc = analisis_checkbox(img, KOTAK_TERCENTANG)
jumlah_putih_kosong, img_biner_k, img_bersih_k = analisis_checkbox(img, KOTAK_KOSONG)

print("--- HASIL ANALISIS (VERSI 3.1 - Final) ---")
print(f"[*] Menganalisis kotak 'Laki-laki' (yang tercentang)...")
print(f"    -> Jumlah piksel aktif terdeteksi: {jumlah_putih_tercentang}")

print(f"\n[*] Menganalisis kotak 'Perempuan' (yang kosong)...")
print(f"    -> Jumlah piksel aktif terdeteksi: {jumlah_putih_kosong}")

print("\n--- KESIMPULAN ---")
if jumlah_putih_tercentang > AMBANG_BATAS_PIKSEL_HITAM:
    print(f"[✓] SUKSES: Kotak 'Laki-laki' teridentifikasi sebagai 'TERCENTANG'.")
else:
    print(f"[!] GAGAL: Kotak 'Laki-laki' teridentifikasi sebagai 'KOSONG'.")

if jumlah_putih_kosong > AMBANG_BATAS_PIKSEL_HITAM:
    print(f"[!] GAGAL: Kotak 'Perempuan' teridentifikasi sebagai 'TERCENTANG'.")
else:
    print(f"[✓] SUKSES: Kotak 'Perempuan' teridentifikasi sebagai 'KOSONG'.")

# --- VISUAL DEBUGGING ---
print("\n--- Menampilkan Jendela Debugging ---")
print("Tekan tombol 'q' untuk menutup.")

cv2.imshow('Kotak Tercentang (SEBELUM Dibersihkan)', img_biner_tc)
cv2.imshow('Kotak Tercentang (SETELAH Dibersihkan)', img_bersih_tc)
cv2.imshow('Kotak Kosong (SEBELUM Dibersihkan)', img_biner_k)
cv2.imshow('Kotak Kosong (SETELAH Dibersihkan)', img_bersih_k)

key = cv2.waitKey(0)
if key == ord('q'):
    cv2.destroyAllWindows()
