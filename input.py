import streamlit as st
from database import get_data, input_data
from datetime import datetime
import pandas as pd

st.title("CMC Gerbang Pujian")
st.divider()
st.subheader("Daftar Kehadiran")

# Mendapatkan data dan pastikan dalam bentuk pandas DataFrame
raw_data = get_data("Data")
data = pd.DataFrame(raw_data)  # Konversi ke DataFrame jika belum

# Format tanggal hari ini sesuai dengan format di spreadsheet (MM/DD/YYYY)
today = datetime.now().strftime("%m/%d/%Y")

# Filter data untuk tanggal hari ini
if not data.empty and 'Tanggal' in data.columns:
    # Pastikan kolom Tanggal adalah string dan strip whitespace
    data['Tanggal'] = data['Tanggal'].astype(str).str.strip()
    today_data = data[data['Tanggal'] == today]
else:
    today_data = pd.DataFrame()  # DataFrame kosong jika tidak ada data

st.dataframe(today_data)

with st.form("Daftar", clear_on_submit=True):
    tanggal = st.date_input("Tanggal Ibadah")
    nama = st.text_input("Nama Lengkap", placeholder="Masukkan Nama Lengkap")
    cmc = st.text_input("Asal CMC", placeholder="contoh: CMC Gerbang Pujian")

    if st.form_submit_button("Absen"):
        if not nama:
            st.warning("Isi Nama Terlebih Dahulu")
        elif not cmc:
            st.warning("Isi Asal CMC!")
        else:
            try:
                date = tanggal.strftime("%m/%d/%Y")
                input_data(date, nama, cmc)
                st.success("Berhasil Absen")
                st.rerun()  # Refresh tampilan
            except Exception as e:
                st.error(f"Terjadi kesalahan: {e}")