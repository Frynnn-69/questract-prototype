import cv2
from boxdetect import pipelines, config
import numpy as np
import json

# --- KONFIGURASI ---
IMAGE_PATH = 'test_images/template_kuesioner_base.png'
# Nama file output untuk blueprint yang dihasilkan
OUTPUT_JSON_PATH = 'generated_config.json'
# Toleransi (dalam piksel) untuk menganggap dua kotak berada di baris yang sama
Y_TOLERANCE = 15

print("Memulai proses pembangkitan blueprint cerdas...")

# Muat gambar
img = cv2.imread(IMAGE_PATH, cv2.IMREAD_COLOR)

if img is None:
    print(f"Error: Tidak bisa membuka gambar di '{IMAGE_PATH}'")
else:
    # 1. [PERBAIKAN KUNCI] Menggunakan metode deteksi yang akurat dan teruji
    #    dari skrip 'automated_finder.py' sebelumnya.
    cfg = config.PipelinesConfig()
    cfg.width_range = (20, 50)
    cfg.height_range = (20, 50)
    cfg.scaling_factors = [1.0]
    cfg.wh_ratio_range = (0.5, 1.5)
    cfg.dilation_iterations = 0

    checkboxes_raw = pipelines.get_checkboxes(img, cfg=cfg, plot=False)

    # 2. Ekstrak hanya koordinat (x, y, w, h) dan saring derau
    boxes = [item[0] for item in checkboxes_raw if item[0][2] > 15 and item[0][3] > 15]
    print(f"Ditemukan dan disaring {len(boxes)} kotak yang valid.")

    # 3. Urutkan kotak dari atas ke bawah
    boxes.sort(key=lambda box: box[1])

    # 4. Kelompokkan kotak ke dalam baris menggunakan Spatial Clustering
    rows = []
    if boxes:
        current_row = [boxes[0]]
        last_y = boxes[0][1]

        for box in boxes[1:]:
            current_y = box[1]
            if abs(current_y - last_y) < Y_TOLERANCE:
                current_row.append(box)
            else:
                rows.append(current_row)
                current_row = [box]
            last_y = current_y
        rows.append(current_row)

    # 5. Urutkan kotak di dalam setiap baris dari kiri ke kanan
    for row in rows:
        row.sort(key=lambda box: box[0])

    # 6. Hasilkan struktur data Python yang rapi
    generated_fields = []
    for i, row in enumerate(rows):
        options = []
        for j, box in enumerate(row):
            box_list = list(box)
            options.append({"label": f"GANTI_LABEL_{j+1}", "box": box_list})

        generated_fields.append({
            "nama": f"GANTI_NAMA_FIELD_{i+1}",
            "tipe": "checkbox",
            "opsi": options
        })

    final_blueprint = {"fields": generated_fields}

    # 7. Simpan ke file JSON
    with open(OUTPUT_JSON_PATH, 'w') as f:
        json.dump(final_blueprint, f, indent=4)

    print("\n--- PROSES SELESAI ---")
    print(f"✅ Blueprint JSON yang terstruktur telah berhasil dibuat!")
    print(f"   Silakan buka file: '{OUTPUT_JSON_PATH}'")
    print("-" * 50)


    # (Opsional) Visualisasi
    out_img = img.copy()
    for i, row in enumerate(rows):
        color = tuple(np.random.randint(0, 255, 3).tolist())
        for j, box in enumerate(row):
            x, y, w, h = box
            cv2.rectangle(out_img, (x, y), (x + w, y + h), color, 2)
            cv2.putText(out_img, f"R{i}", (x - 40, y + h), cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)

    cv2.imshow("Hasil Pengelompokan Spasial - Tekan 'q' untuk keluar", out_img)
    while True:
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cv2.destroyAllWindows()
