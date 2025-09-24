import cv2
import numpy as np

def _analyze_checkbox(image_roi, settings):
    """
    Fungsi internal untuk menganalisis satu area ROI checkbox.
    Mengembalikan JUMLAH PIKSEL AKTIF yang terdeteksi.
    """
    grayscale = cv2.cvtColor(image_roi, cv2.COLOR_BGR2GRAY)
    binary = cv2.adaptiveThreshold(
        grayscale, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY_INV, 11, 2
    )
    kernel = np.ones(settings["morph_kernel"], np.uint8)
    cleaned_image = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel)
    pixel_count = cv2.countNonZero(cleaned_image)
    return pixel_count

def process_image(image, blueprint):
    """
    Fungsi utama untuk memproses seluruh gambar berdasarkan blueprint.
    """
    results = {}
    settings = blueprint["settings"]
    shrink_factor = settings["shrink_factor"]

    for field in blueprint["fields"]:
        field_name = field["nama"]

        if field["tipe"] == "checkbox":
            best_option_label = "TIDAK TERDETEKSI"
            highest_pixel_count = settings["pixel_threshold"]

            # [UPGRADE DEBUG] Simpan skor untuk setiap opsi
            all_options_scores = []

            for option in field["opsi"]:
                x, y, w, h = option["box"]
                roi_awal = image[y:y+h, x:x+w]

                shrink_w = int(w * shrink_factor)
                shrink_h = int(h * shrink_factor)
                offset_x = (w - shrink_w) // 2
                offset_y = (h - shrink_h) // 2
                roi_dalam = roi_awal[offset_y:offset_y+shrink_h, offset_x:offset_x+shrink_w]

                current_pixel_count = _analyze_checkbox(roi_dalam, settings)
                all_options_scores.append({"label": option["label"], "score": current_pixel_count, "box": option["box"]})

                if current_pixel_count > highest_pixel_count:
                    highest_pixel_count = current_pixel_count
                    best_option_label = option["label"]

            results[field_name] = {
                "jawaban": best_option_label,
                "laporan_debug": all_options_scores
            }

    return results
