import streamlit as st


input = st.Page(
    page = "input.py",
    title = "input",
    icon = "📊"
)

pg = st.navigation({
    "Absensi": [input],
    
})

pg.run()