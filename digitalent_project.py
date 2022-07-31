from email.mime import image
import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

# Add a placeholder
st.balloons()

def main_page():
    st.markdown("# KEAMANAN SIBER DI BANDARA :airplane: :dash:")
    st.sidebar.markdown("<h1 style='text-align: center; color: yellow;'>Definisi</h1>", unsafe_allow_html=True)
    st.sidebar.markdown(":rose: :rose: :rose: :rose: :rose: :rose: :rose: :rose: :rose: :rose: :rose: :rose:")
    st.sidebar.markdown("<h2 style='text-align: center; color: black;'>Informasi Tambahan</h2>", unsafe_allow_html=True)
    st.sidebar.markdown("""
                        <p style='color: black;'>Contributor Kelompok Cosmos:</p>
                        <ol style='color:black;'>
                            <li>Ira Naintin Sepnanda</li>
                            <li>Putri Meliana Sari</li>
                            <li>Vita Tri Utami</li>
                        </ol>
                        """, unsafe_allow_html=True)
    st.sidebar.markdown("")
    st.sidebar.markdown("<h3 style='text-align: center; color: black;'>Powered by:</h3>", unsafe_allow_html=True)
    st.sidebar.markdown("""
                        <p align="center">
                            <img style="width: 160px; height: 80px;" src="https://d2n98vq36tw7n9.cloudfront.net/s3fs-public/2021-05/cisco-logo.png?VersionId=wQqav3uAWA.RGwElj6k2QtwbQL0qZcpo">
                            <img style="width: 160px; height: 60px;" src="https://web.kominfo.go.id/sites/default/files/users/12/DTS.png">
                            <img style="width: 70px; height: 60px;" src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a2/Logo_of_Ministry_of_Communication_and_Information_Technology_of_the_Republic_of_Indonesia.svg/1200px-Logo_of_Ministry_of_Communication_and_Information_Technology_of_the_Republic_of_Indonesia.svg.png">
                        </p>
                        """, unsafe_allow_html=True)
    st.sidebar.markdown("<h4 style='text-align: center; color: black;'>Copyright &copy; 2022</h4>", unsafe_allow_html=True)
                        


    # 1 SET TITLE
    st.header('Bandara :airplane: :dash:')
    st.caption('Disusun oleh Kelompok Cosmos :hibiscus:')

    # Media Elements st.image
    st.image("https://nelysis.com/wp-content/uploads/2019/06/cybersecurity-for-airports.jpg")



    st.title('\n')
    st.title('\n')

def page2():
    st.markdown("# Halaman Kedua :smile:")
    st.sidebar.markdown("<h1 style='text-align: center; color: yellow;'>Keamanan Siber Bandara Dunia</h1>", unsafe_allow_html=True)
    st.sidebar.markdown(":blossom: :blossom: :blossom: :blossom: :blossom: :blossom: :blossom: :blossom: :blossom: :blossom: :blossom: :blossom:")
    st.write("Haloo ini halaman ke-2")
    st.write("asik")
    
    from PIL import Image
    
    
def page3():
    st.markdown("# Halaman Ketiga :smile:")
    st.sidebar.markdown("<h1 style='text-align: center; color: yellow;'>Keamanan Siber Bandara Indonesia</h1>", unsafe_allow_html=True)
    st.sidebar.markdown(":small_airplane: :flag-id:")
    st.write("Haloo ini halaman ke-3")
    st.write("seru")
    
    from PIL import Image
    
    
page_names_to_func = {
    "Halaman Utama": main_page,
    "Halaman Kedua": page2,
    "Halaman Ketiga": page3,
}

st.sidebar.header("Keamanan Siber Bandara")
selected_page = st.sidebar.selectbox ("Pilih Halaman", page_names_to_func.keys())
page_names_to_func[selected_page]()