import cv2
import numpy as np

FILE_NAME = 'test_images/template_kuesioner_2.jpg'

KOTAK_TERCENTANG = (190, 200, 30, 30)  # "Male" checkbox
KOTAK_KOSONG = (330, 200, 30, 30)      # "Female" checkbox

SHRINK_FACTOR = 0.8
AMBANG_BATAS_PIKSEL_HITAM = 40

def analisis_checkbox(gambar, koordinat):
    # 1. Crop ROI and shrink to inner area (avoid border noise)
    x, y, w, h = koordinat
    area_kotak_awal = gambar[y:y+h, x:x+w]
    shrink_w = int(w * SHRINK_FACTOR)
    shrink_h = int(h * SHRINK_FACTOR)
    offset_x = (w - shrink_w) // 2
    offset_y = (h - shrink_h) // 2
    area_dalam = area_kotak_awal[offset_y:offset_y+shrink_h, offset_x:offset_x+shrink_w]

    # 2. Grayscale & Adaptive Thresholding
    grayscale = cv2.cvtColor(area_dalam, cv2.COLOR_BGR2GRAY)
    biner = cv2.adaptiveThreshold(
        grayscale, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY_INV, 11, 2
    )

    # 3. Morphological Opening (noise removal)
    kernel = np.ones((2,2), np.uint8)
    gambar_bersih = cv2.morphologyEx(biner, cv2.MORPH_OPEN, kernel)

    jumlah_piksel_putih = cv2.countNonZero(gambar_bersih)

    return jumlah_piksel_putih, biner, gambar_bersih

img = cv2.imread(FILE_NAME)
if img is None:
    print(f"ERROR: File '{FILE_NAME}' not found.")
    exit()

jumlah_putih_tercentang, img_biner_tc, img_bersih_tc = analisis_checkbox(img, KOTAK_TERCENTANG)
jumlah_putih_kosong, img_biner_k, img_bersih_k = analisis_checkbox(img, KOTAK_KOSONG)

print("--- ANALYSIS RESULTS ---")
print(f"[*] Analyzing 'Male' checkbox (checked)...")
print(f"    -> Active pixels detected: {jumlah_putih_tercentang}")

print(f"\n[*] Analyzing 'Female' checkbox (empty)...")
print(f"    -> Active pixels detected: {jumlah_putih_kosong}")

print("\n--- CONCLUSION ---")
if jumlah_putih_tercentang > AMBANG_BATAS_PIKSEL_HITAM:
    print(f"[✓] SUCCESS: 'Male' checkbox identified as 'CHECKED'.")
else:
    print(f"[!] FAILED: 'Male' checkbox identified as 'EMPTY'.")

if jumlah_putih_kosong > AMBANG_BATAS_PIKSEL_HITAM:
    print(f"[!] FAILED: 'Female' checkbox identified as 'CHECKED'.")
else:
    print(f"[✓] SUCCESS: 'Female' checkbox identified as 'EMPTY'.")

cv2.imshow('Checked Box (BEFORE Cleaning)', img_biner_tc)
cv2.imshow('Checked Box (AFTER Cleaning)', img_bersih_tc)
cv2.imshow('Empty Box (BEFORE Cleaning)', img_biner_k)
cv2.imshow('Empty Box (AFTER Cleaning)', img_bersih_k)

key = cv2.waitKey(0)
if key == ord('q'):
    cv2.destroyAllWindows()
