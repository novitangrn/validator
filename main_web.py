from synop_functions import *
from functions_00UTC import *

import streamlit as st
import pandas as pd


def main_st():
    img = st.image('login2.png', width=120)
    st.title("Validator Synop Sederhana")
    #st.image('login2.png',use_column_width=True)
    
    # Dropdown untuk memilih jam
    selected_hour = st.selectbox("Pilih Jam", ["--Pilih Jam--", "00.00", "01.00", "02.00"])  # Tambahkan jam-jam lain yang diinginkan

    # Input teks dari pengguna
    synop_code = st.text_area("Masukkan sandi synop", height=100)

    # Tombol untuk memproses data
    if st.button("Proses"):
        # Memeriksa apakah input kosong atau hanya mengandung spasi
        if not synop_code.strip():
            st.error("Masukkan input sandi synop yang valid")
        else:
            # 00UTC
            if selected_hour == "00.00":
                df_seksi_0, df_seksi_1, df_seksi_3 = main_00UTC(synop_code)
            # elif selected_hour == "01.00":
            #     df = main_01UTC(synop_code)
            # elif selected_hour == "02.00":
            #     df = main_02UTC(synop_code)
            else:
                st.error("Jam yang dipilih tidak valid")

        # Menampilkan DataFrame jika ada
        if 'df_seksi_0' in locals():
            st.markdown("<h2>Seksi 0</h2>", unsafe_allow_html=True)
            st.dataframe(highlight_df(df_seksi_0), height=300, width=700)
        if 'df_seksi_1' in locals():
            st.markdown("<h2>Seksi 1</h2>", unsafe_allow_html=True)
            st.dataframe(highlight_df(df_seksi_1), height=450, width=700)
        if 'df_seksi_3' in locals():
            st.markdown("<h2>Seksi 3</h2>", unsafe_allow_html=True)
            st.dataframe(highlight_df(df_seksi_3), height=500, width=700)

def highlight_df(df):
    def highlight(row):
        # Menggunakan warna kuning untuk baris dengan nilai pada kolom output
        # Ganti 'output_column_name' dengan nama kolom output yang relevan
        if row['Output'] != "":
            return ['background-color: yellow'] * len(row)
        return [''] * len(row)

    return df.style.apply(highlight, axis=1)

if __name__ == '__main__':
    main_st()
