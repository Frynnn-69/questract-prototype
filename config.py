# Blueprint Template Base for Questionnaire Form

# Format koordinat(x, y, w, h)
# x = jarak dari kiri, y = jarak dari atas

KUESIONER_V1_BLUEPRINT = {
    "nama": "Kuesioner Sikap Kontrasepsi",
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
        {
            "nama": "pernyataan_1",
            "tipe": "checkbox",
            "opsi": [
                {"label": "1", "box": (2722, 2762, 75, 175)},
                {"label": "2", "box": (2819, 2765, 75, 175)},
                {"label": "3", "box": (2914, 2764, 75, 175)},
                {"label": "4", "box": (3002, 2762, 75, 175)},
                {"label": "5", "box": (3098, 2760, 75, 175)},
            ]
        },
        {
            "nama": "pernyataan_2",
            "tipe": "checkbox",
            "opsi": [
                {"label": "1", "box": (2727, 2940, 75, 175)},
                {"label": "2", "box": (2824, 2941, 75, 175)},
                {"label": "3", "box": (2919, 2937, 75, 175)},
                {"label": "4", "box": (3006, 2940, 75, 175)},
                {"label": "5", "box": (3104, 2930, 75, 175)},
            ]
        },
        {
            "nama": "pernyataan_3",
            "tipe": "checkbox",
            "opsi": [
                {"label": "1", "box": (2730, 3104, 75, 175)},
                {"label": "2", "box": (2825, 3105, 75, 175)},
                {"label": "3", "box": (2919, 3107, 75, 175)},
                {"label": "4", "box": (3008, 3103, 75, 175)},
                {"label": "5", "box": (3104, 3103, 75, 175)},
            ]
        },
        {
            "nama": "pernyataan_4",
            "tipe": "checkbox",
            "opsi": [
                {"label": "1", "box": (2732, 3278, 75, 175)},
                {"label": "2", "box": (2828, 3282, 75, 175)},
                {"label": "3", "box": (2921, 3278, 75, 175)},
                {"label": "4", "box": (3007, 3268, 75, 175)},
                {"label": "5", "box": (3106, 3275, 75, 175)},
            ]
        },

        #beda ukuran box
        {
            "nama": "pernyataan_5",
            "tipe": "checkbox",
            "opsi": [
                {"label": "1", "box": (2730, 3439, 75, 85)},
                {"label": "2", "box": (2828, 3442, 75, 85)},
                {"label": "3", "box": (2922, 3435, 75, 85)},
                {"label": "4", "box": (3017, 3438, 75, 85)},
                {"label": "5", "box": (3114, 3438, 75, 85)},
            ]
        },
        {
            "nama": "pernyataan_6",
            "tipe": "checkbox",
            "opsi": [
                {"label": "1", "box": (2741, 3530, 75, 175)},
                {"label": "2", "box": (2829, 3532, 75, 175)},
                {"label": "3", "box": (2926, 3535, 75, 175)},
                {"label": "4", "box": (3016, 3536, 75, 175)},
                {"label": "5", "box": (3109, 3526, 75, 175)},
            ]
        },
        {
            "nama": "pernyataan_7",
            "tipe": "checkbox",
            "opsi": [
                {"label": "1", "box": (2737, 3708, 75, 175)},
                {"label": "2", "box": (2844, 3706, 75, 175)},
                {"label": "3", "box": (2927, 3717, 75, 175)},
                {"label": "4", "box": (3023, 3710, 75, 175)},
                {"label": "5", "box": (3123, 3711, 75, 175)},
            ]
        },
        # 8, 9, 10 - 15 it's same

        # Confirm Interview
        {
            "nama": "confirm_interview",
            "tipe": "checkbox",
            "opsi": [
                {"label": "Ya", "box": (4024, 1395, 30, 30)},
                {"label": "Tidak", "box": (4202, 1392, 30, 30)}
            ]
        },

    ],
    "settings": {
        "pixel_threshold": 20,
        "min_contour_area": 15
        # "shrink_factor": 0.8,
        # "morph_kernel": (2, 2)
    }
}
