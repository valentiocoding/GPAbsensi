import streamlit as st


input = st.Page(
    page = "input.py",
    title = "CMC Gerbang Pujian - Absensi   ",
    icon = "📊"
)

pg = st.navigation({
    "Absensi": [input],
    
})

pg.run()