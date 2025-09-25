# -*- coding: utf-8 -*-
# --- Questract Coordinate Finder v6.0 (Definitif) ---
#
# --- PERUBAHAN PENTING (v6.0) ---
# [+] DESAIN ULANG TOTAL UNTUK STABILITAS TRACKPAD: Kembali ke alur kerja
#     yang hanya menggunakan KLIK KIRI untuk semua aksi.
# [+] ALUR KERJA BARU:
#     1. KLIK KIRI pertama: Menandai titik awal (lingkaran hijau).
#     2. KLIK KIRI kedua: Menandai titik akhir, yang otomatis membuat
#        kotak merah permanen dan menyelesaikan tugas.
# [+] JEJAK VISUAL PERMANEN: Semua kotak merah yang sudah jadi akan tetap ada.
# [+] TERMINOLOGI DIPERBAIKI: Output di terminal lebih jelas.
#
import cv2
import sys

# --- State Management ---
start_point = None
current_mouse_pos = None
defined_boxes = []
needs_redraw = True
WINDOW_NAME = "Questract Coordinate Finder v6.0 (Definitif)"

def mouse_event_handler(event, x, y, flags, params):
    """Menangani logika event mouse dan memperbarui state."""
    global start_point, needs_redraw, current_mouse_pos

    current_mouse_pos = (x, y)
    needs_redraw = True

    if event == cv2.EVENT_LBUTTONDOWN:
        if start_point is None:
            # Ini adalah klik pertama untuk memulai kotak baru
            start_point = (x, y)
            print(f"Titik awal ditandai di (x, y): {start_point}")
        else:
            # Ini adalah klik kedua untuk menyelesaikan kotak
            end_point = (x, y)

            x1, y1 = start_point
            x2, y2 = end_point
            box = (min(x1, x2), min(y1, y2), abs(x1 - x2), abs(y1 - y2))

            defined_boxes.append(box)
            start_point = None # Reset untuk persiapan kotak selanjutnya

            print("-" * 30)
            print(f"Kotak #{len(defined_boxes)} berhasil dibuat!")
            print(f'   Hasil kalkulasi "box": {box[:4]}')
            print("-" * 30)

# --- Inisialisasi ---
if len(sys.argv) > 1:
    IMAGE_PATH = sys.argv[1]
else:
    IMAGE_PATH = 'test_images/template_kuesioner_base.png'

original_image = cv2.imread(IMAGE_PATH)
if original_image is None:
    print(f"Error: Tidak bisa membuka gambar di '{IMAGE_PATH}'")
    sys.exit()

cv2.namedWindow(WINDOW_NAME, cv2.WINDOW_NORMAL)
cv2.setMouseCallback(WINDOW_NAME, mouse_event_handler)

print("--- Questract Coordinate Finder v6.0 ---")
print("KLIK KIRI untuk titik awal, KLIK KIRI lagi untuk titik akhir.")
print("Tekan 'r' untuk RESET | Tekan 'q' untuk KELUAR.")
print("-" * 30)

# --- Loop Utama (Event Loop) ---
while True:
    if needs_redraw:
        display_buffer = original_image.copy()

        # Gambar semua kotak yang sudah jadi
        for box in defined_boxes:
            x, y, w, h = box
            cv2.rectangle(display_buffer, (x, y), (x + w, y + h), (0, 0, 255), 2)

        # Gambar titik awal jika ada
        if start_point:
            cv2.circle(display_buffer, start_point, 7, (0, 255, 0), -1)

        # Gambar crosshair
        if current_mouse_pos:
            h, w, _ = display_buffer.shape
            cv2.line(display_buffer, (0, current_mouse_pos[1]), (w, current_mouse_pos[1]), (255, 255, 0), 1)
            cv2.line(display_buffer, (current_mouse_pos[0], 0), (current_mouse_pos[0], h), (255, 255, 0), 1)

        cv2.imshow(WINDOW_NAME, display_buffer)
        needs_redraw = False

    key = cv2.waitKey(20) & 0xFF
    if key == ord('q'):
        break
    elif key == ord('r'):
        print("--- Semua penandaan di-reset ---")
        start_point = None
        defined_boxes = []
        needs_redraw = True

cv2.destroyAllWindows()
