from synop_functions import *
from functions_00UTC import *

import streamlit as st
import pandas as pd
import re


# Main Streamlit
def main_st():
    st.set_page_config(layout="wide")
    img = st.image('login2.png', width=180)
    st.title("Validator Synop Sederhana")
    #st.image('login2.png',use_column_width=True)
    
    # Dropdown untuk memilih jam
    # selected_hour = st.selectbox("Pilih Jam", ["--Pilih Jam--", "00.00", "01.00", "02.00"])  # Tambahkan jam-jam lain yang diinginkan
    
    # Input teks dari pengguna
    synop_code = st.text_area("Masukkan sandi synop", height=100)
    
    # Process button
    if st.button("Proses"):
        # None input
        if not synop_code.strip():
            st.error("Masukkan input sandi synop yang valid")
        else:
            # prepare sandi  
            kode_stamet = "https://raw.githubusercontent.com/novitangrn/dataset/main/Kode%20Stasiun%20Indonesia.csv"
            df_kode = pd.read_csv(kode_stamet, sep=';')
            
            # prepare sandi  
            heading_list, section_0_list, section_1_list, section_3_list = input_sandi(synop_code, df_kode)
    
            # check time to run the corresponding functions
            selected_hour = check_time(heading_list)

            # Display selected hour
            st.success(f"Jam yang dipilih: {selected_hour}.00")
            #st.markdown(f"<h3>Jam yang terdeteksi: {selected_hour}</h3>", unsafe_allow_html=True)
    
            # 00UTC
            if selected_hour == "00":
                try:
                    # Memeriksa apakah part terakhir dari keseluruhan sandi mengandung tanda "="
                    pattern = r'=\s*$'  # Pola ekspresi reguler untuk mencocokkan tanda "=" di akhir teks
                    if re.search(pattern, synop_code):
                        df_seksi_0, df_seksi_1, df_seksi_3 = main_00UTC(heading_list, section_0_list, section_1_list, section_3_list)
                    else:
                        st.warning("Part terakhir dari sandi synop tidak memiliki tanda '='")
                        df_seksi_0, df_seksi_1, df_seksi_3 = main_00UTC(heading_list, section_0_list, section_1_list, section_3_list)
                except ValueError:
                    st.error("Masukkan sandi synop yang valid")
            # elif selected_hour == "01.00":
            #     df = main_01UTC(synop_code)
            # elif selected_hour == "02.00":
            #     df = main_02UTC(synop_code)
            else:
                st.error("Jam yang dipilih tidak valid")

        # Memeriksa apakah semua kolom 'Output' pada DataFrame tidak berisi pesan apapun
        if 'df_seksi_0' in locals() and 'df_seksi_1' in locals() and 'df_seksi_3' in locals():
            if (df_seksi_0['Output'].astype(bool).sum() == 0 and
                df_seksi_1['Output'].astype(bool).sum() == 0 and
                df_seksi_3['Output'].astype(bool).sum() == 0):
                st.success("Sandi synop sudah benar")
                st.markdown("<br>", unsafe_allow_html=True)  # Menambahkan baris kosong setelah pesan
            else:
                st.warning("Sandi synop mengandung kesalahan")
                st.markdown("<br>", unsafe_allow_html=True)  # Menambahkan baris kosong setelah pesa
        
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
