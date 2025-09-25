import streamlit as st
import cv2
import numpy as np
from PIL import Image

from config import KUESIONER_V1_BLUEPRINT
from questract.extractor import process_image

st.set_page_config(page_title="Questract Prototype", layout="wide")
st.title("🚀 Prototipe Questract")
st.write("Unggah gambar kuesioner yang sudah diisi untuk memulai proses ekstraksi.")

col1, col2 = st.columns(2)

with col1:
    st.header("1. Unggah Gambar")
    uploaded_file = st.file_uploader("Pilih file gambar (JPG atau PNG)", type=['jpg', 'png'])

    debug_mode = st.checkbox("Tampilkan Mode Debug Visual")

    if uploaded_file is not None:
        image_bytes = uploaded_file.getvalue()
        st.image(image_bytes, caption="Gambar yang Diunggah", width='stretch')

with col2:
    st.header("2. Hasil Ekstraksi")
    if uploaded_file is not None:
        if st.button("✨ Mulai Proses Ekstraksi"):
            file_bytes = np.frombuffer(image_bytes, np.uint8)
            opencv_image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

            with st.spinner("Mesin sedang bekerja... Menganalisis piksel..."):
                if opencv_image is not None:
                    extracted_data = process_image(opencv_image, KUESIONER_V1_BLUEPRINT)
                    st.success("Proses ekstraksi selesai!")

                    final_answers = {key: value["jawaban"] for key, value in extracted_data.items()}
                    st.json(final_answers)

                    if debug_mode:
                        st.subheader("🕵️ Laporan Debug Visual")
                        debug_image = opencv_image.copy()

                        for field, data in extracted_data.items():
                            for option_report in data["laporan_debug"]:
                                box = option_report["box"]
                                score = option_report["score"]
                                x, y, w, h = box

                                cv2.rectangle(debug_image, (x, y), (x + w, y + h), (0, 255, 0), 2)
                                cv2.putText(debug_image, str(score), (x + w, y + h), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)

                        st.image(debug_image, channels="BGR", caption="Gambar dengan Anotasi Debug", width='stretch')
                        st.write("Laporan Skor Mentah:")
                        st.json(extracted_data)

                else:
                    st.error("Gagal memproses gambar.")
    else:
        st.info("Silakan unggah gambar terlebih dahulu.")
