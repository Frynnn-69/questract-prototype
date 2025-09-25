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
                {"label": "Laki-laki", "box": (1517, 1022, 30, 30)},
                {"label": "Perempuan", "box": (1871, 1014, 30, 30)}
            ]
        },
        {
            "nama": "pendidikan_terakhir",
            "tipe": "checkbox",
            "opsi": [
                {"label": "SD", "box": (1522, 1122, 30, 30)},
                {"label": "SMP", "box": (1704, 1116, 30, 30)},
                {"label": "SMA", "box": (1932, 1122, 30, 30)},
                {"label": "SMK", "box": (2166, 1114, 30, 30)},
                {"label": "Diploma", "box": (2402, 1109, 30, 30)},
                {"label": "Perguruan Tinggi", "box": (2721, 1110, 30, 30)},
            ]
        },
        {
            "nama": "bidang_pendidikan",
            "tipe": "checkbox",
            "opsi": [
                {"label": "Kesehatan", "box": (1518, 1304, 30, 30)},
                {"label": "Nonkesehatan", "box": (1888, 1303, 30, 30)},
            ]
        },
        {
            "nama": "pekerjaan",
            "tipe": "checkbox",
            "opsi": [
                {"label": "Pelajar", "box": (1527, 1401, 30, 30)},
                {"label": "Ibu Rumah Tangga", "box": (1799, 1398, 30, 30)},
                {"label": "Tidak Bekerja", "box": (2390, 1399, 30, 30)},
                {"label": "Karyawan Swasta", "box": (2843, 1389, 30, 30)},
                {"label": "PNS", "box": (2014, 1498, 30, 30)},
                {"label": "TNI", "box": (2228, 1492, 30, 30)},
                {"label": "Polri", "box": (2434, 1491, 30, 30)},
                {"label": "Buruh", "box": (2655, 1491, 30, 30)},
                {"label": "Pekerja Lepas", "box": (2910, 1485, 30, 30)},
                {"label": "Wirausaha", "box": (1916, 1592, 30, 30)},
                {"label": "Lainnya", "box": (2283, 1588, 30, 30)},
            ]
        },
        {
            "nama": "bidang_pekerjaan",
            "tipe": "checkbox",
            "opsi": [
                {"label": "Kesehatan", "box": (1537, 1701, 30, 30)},
                {"label": "Pendidikan", "box": (1895, 1696, 30, 30)},
                {"label": "Teknologi", "box": (2280, 1690, 30, 30)},
                {"label": "Bisnis", "box": (2637, 1688, 30, 30)},
                {"label": "Hukum", "box": (2892, 1687, 30, 30)},
                {"label": "Seni", "box": (1537, 1795, 30, 30)},
                {"label": "Lainnya", "box": (1753, 1787, 30, 30)},
            ]
        },

        # 2. Sikap Terhadap Kontrasepsi untuk remaja
        # {
        #     "nama": "pernyataan_1",
        #     "tipe": "checkbox",
        #     "opsi": [
        #         {"label": "1", "box": (x, y, 30, 30)},
        #         {"label": "2", "box": (x, y, 30, 30)},
        #         {"label": "3", "box": (x, y, 30, 30)},
        #         {"label": "4", "box": (x, y, 30, 30)},
        #         {"label": "5", "box": (x, y, 30, 30)},
        #     ]
        # },

    ],
    "settings": {
        "pixel_threshold": 20,
        "min_contour_area": 15
        # "shrink_factor": 0.8,
        # "morph_kernel": (2, 2)
    }
}
