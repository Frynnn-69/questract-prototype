import cv2
import numpy as np
import sys

def _analyze_checkbox(image_roi, min_contour_area):
    """
    Fungsi internal untuk menganalisis checkbox menggunakan
    Deteksi Kontur DENGAN FILTER DERAU.
    """
    if image_roi is None or image_roi.size == 0:
        return 0

    grayscale = cv2.cvtColor(image_roi, cv2.COLOR_BGR2GRAY)
    _, binary = cv2.threshold(grayscale, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if not contours:
        return 0

    filtered_contours = [c for c in contours if cv2.contourArea(c) > min_contour_area]

    if not filtered_contours:
        return 0

    total_area = sum(cv2.contourArea(c) for c in filtered_contours)
    return total_area


def process_image(image, blueprint):
    """
    Fungsi utama untuk memproses seluruh gambar berdasarkan blueprint.
    """
    results = {}
    settings = blueprint["settings"]
    img_height, img_width, _ = image.shape

    min_contour_area = settings.get("min_contour_area", 15)

    for field in blueprint["fields"]:
        field_name = field["nama"]
        if field["tipe"] == "checkbox":
            best_option_label = "TIDAK TERDETEKSI"
            highest_score = settings.get("pixel_threshold", 10)
            all_options_scores = []

            for option in field["opsi"]:
                x, y, w, h = option["box"]

                if x + w > img_width or y + h > img_height:
                    continue

                roi_awal = image[y:y+h, x:x+w]

                if roi_awal is None or roi_awal.size == 0:
                    continue

                current_score = _analyze_checkbox(roi_awal, min_contour_area)
                all_options_scores.append({"label": option["label"], "score": current_score, "box": option["box"]})

                if current_score > highest_score:
                    highest_score = current_score
                    best_option_label = option["label"]

            results[field_name] = {
                "result": best_option_label,
                "debug_report": all_options_scores
            }

    return results
