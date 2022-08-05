from email.mime import image
from tokenize import Name
from unicodedata import name
from urllib import request
import pandas as pd
import numpy as np
from PIL import Image
import time
import json
import requests
import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_lottie import st_lottie_spinner
import matplotlib.pyplot as plt


st.markdown("# CYBERSECURITY IN AVIATION INDUSTRY :small_airplane:")
st.sidebar.markdown("<h1 style='text-align: center; color: red;'>Perlindungan dalam Keamanan Siber Bandara</h1>", unsafe_allow_html=True)
st.sidebar.markdown(":blossom: :blossom: :blossom: :blossom: :blossom: :blossom: :blossom: :blossom: :blossom: :blossom: :blossom: :blossom:")
st.write("Sangat penting untuk menjaga")
st.write("...")
    
    
# 1 SET TITLE
st.header('KEAMANAN SIBER BANDARA :airplane: :dash:')
st.caption('Disusun oleh Kelompok Cosmos :hibiscus:')

# Media Elements st.image
st.image("https://nelysis.com/wp-content/uploads/2019/06/cybersecurity-for-airports.jpg")
st.caption("Credit to nelysis.com")



st.title('\n')
st.title('\n')


    
# add video
st.write("""
        ## Bidang apa saja yang perlu dilindungi?
        """)
video1 = open("./img/Cyber security for aviation.mp4", "rb")
st.video(video1)
st.caption("Credit to: https://www.youtube.com/watch?v=VXp9zaf6CT8")
