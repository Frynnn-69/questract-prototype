# Blueprint Template Base for Questionnaire Form

# Format koordinat(x, y, lebar, tinggi)
# x = jarak dari kiri, y = jarak dari atas

KUESIONER_V1_BLUEPRINT = {
    "nama": "Kuesioner Sikap Kontrasepsi V1",
    # 1. Karakteristik Responden
    "fields": [
        {
            "nama": "jenis_kelamin",
            "tipe": "checkbox",
            "opsi": [
                {"label": "Laki-laki", "box": (190, 200, 30, 30)},
                {"label": "Perempuan", "box": (330, 200, 30, 30)}
            ]
        },
        {
            "nama": "pendidikan_terakhir",
            "tipe": "checkbox",
            "opsi": [
                {"label": "SD", "box": (190, 245, 30, 30)},
                {"label": "SMP", "box": (255, 245, 30, 30)},
                {"label": "SMA", "box": (320, 245, 30, 30)},
                {"label": "SMK", "box": (385, 245, 30, 30)},
                {"label": "Diploma", "box": (2397, 1117, 30, 30)},
                {"label": "Perguruan Tinggi", "box": (2723, 1117, 30, 30)},
            ]
        },
        {
            "nama": "bidang_pendidikan",
            "tipe": "checkbox",
            "opsi": [
                {"label": "Kesehatan", "box": (1526, 1306, 30, 30)},
                {"label": "Nonkesehatan", "box": (1889, 1300, 30, 30)},
            ]
        },
        {
            "nama": "pekerjaan",
            "tipe": "checkbox",
            "opsi": [
                {"label": "Pelajar", "box": (1527, 1408, 30, 30)},
                {"label": "Ibu Rumah Tangga", "box": (1800, 1410, 30, 30)},
                {"label": "Tidak Bekerja", "box": (2389, 1398, 30, 30)},
                {"label": "Karyawan Swasta", "box": (2837, 1390, 30, 30)},
                {"label": "PNS", "box": (2010, 1498, 30, 30)},
                {"label": "TNI", "box": (2224, 1491, 30, 30)},
                {"label": "Polri", "box": (2429, 1489, 30, 30)},
                {"label": "Buruh", "box": (2655, 1484, 30, 30)},
                {"label": "Pekerja Lepas", "box": (2908, 1492, 30, 30)},
                {"label": "Wirausaha", "box": (1915, 1589, 30, 30)},
                {"label": "Lainnya", "box": (2285, 1597, 30, 30)},
            ]
        },
        # {
        #     "nama": "bidang_pekerjaan",
        #     "tipe": "checkbox",
        #     "opsi": [
        #         {"label": "Kesehatan", "box": (190, 245, 30, 30)},
        #         {"label": "Pendidikan", "box": (2397, 1117, 30, 30)},
        #         {"label": "Teknologi", "box": (2723, 1117, 30, 30)},
        #         {"label": "Bisnis", "box": (2723, 1117, 30, 30)},
        #         {"label": "Hukum", "box": (2723, 1117, 30, 30)},
        #         {"label": "Seni", "box": (2723, 1117, 30, 30)},
        #         {"label": "Lainnya", "box": (2723, 1117, 30, 30)},
        #     ]
        # }
    ],
    "settings": {
        "shrink_factor": 0.8,
        "pixel_threshold": 40,
        "morph_kernel": (2, 2)
    }
}
