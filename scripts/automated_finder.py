import cv2
from boxdetect import pipelines, config
import sys

# --- KONFIGURASI ---
IMAGE_PATH = 'test_images/template_kuesioner_base.png'

print("Memulai proses deteksi kotak otomatis...")

# Muat gambar
img = cv2.imread(IMAGE_PATH, cv2.IMREAD_COLOR)

if img is None:
    print(f"Error: Tidak bisa membuka gambar di '{IMAGE_PATH}'")
else:
    try:
        cfg = config.PipelinesConfig()
        cfg.width_range = (20, 40)
        cfg.height_range = (20, 40)
        cfg.scaling_factors = [1.0]
        cfg.wh_ratio_range = (0.8, 1.2)
        cfg.dilation_iterations = 0

        print("Konfigurasi berhasil dibuat. Menjalankan deteksi...")

        checkboxes = pipelines.get_checkboxes(img, cfg=cfg, plot=False)

        print(f"Deteksi selesai. Ditemukan {len(checkboxes)} kandidat kotak.")

        out_img = img.copy()

        # [PERBAIKAN] Mengubah cara kita membongkar data
        # 'checkboxes' adalah daftar dari tuple. Setiap tuple berisi (koordinat, flag, gambar_potongan)
        # Kita hanya tertarik pada elemen pertama, yaitu 'koordinat'.
        for item in checkboxes:
            # Ambil hanya elemen pertama (koordinat) dari setiap item
            box = item[0]
            # Sekarang 'box' berisi tuple (x, y, w, h) yang kita harapkan
            x, y, w, h = box
            cv2.rectangle(out_img, (x, y), (x + w, y + h), (0, 0, 255), 2)

        cv2.imshow("Hasil Deteksi Kotak - Tekan 'q' untuk keluar", out_img)
        print("Tekan tombol 'q' pada jendela gambar untuk menutup.")

        while True:
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        cv2.destroyAllWindows()

    except Exception as e:
        print(f"\n--- TERJADI EROR DALAM EKSEKUSI ---\n Tipe Eror: {type(e).__name__}\n Pesan Eror: {e}\n------------------------------------")
