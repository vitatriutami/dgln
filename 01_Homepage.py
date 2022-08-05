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





# HOMPEPAGE
st.markdown("# Welcome to Our Web App :wave:")
st.sidebar.markdown("<h1 style='text-align: center; color: red;'>Homepage</h1>", unsafe_allow_html=True)
st.sidebar.markdown("")
st.sidebar.markdown("")
st.sidebar.markdown("")
st.sidebar.markdown("")
st.sidebar.markdown("")
st.sidebar.markdown("")
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
                        

st.text_input("Your name:", key = "name")
st.write(":sunglasses: :sunglasses: Hello,", st.session_state.name)
st.title('\n')


if st.button ("Mulai"):
    st.text("Yuk!")
    st.balloons()
    
st.title('\n')
st.title('\n')
    
        
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

    
lottie_hello = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_calza6zj.json")

