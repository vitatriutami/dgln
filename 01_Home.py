from email.mime import image
from lib2to3.pgen2.pgen import DFAState
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
from streamlit_option_menu import option_menu
import streamlit.components.v1 as html
from st_aggrid import AgGrid
import cv2
import plotly as plt
import plotly.express as px
import io
from openpyxl import Workbook


# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
local_css("./style/style.css")

# ---- NAVBAR MENU -----
choose = option_menu(None, ["Home", "Project", "Data", "About Us", "Contact"],
                     icons=['house', 'camera fill', 'kanban', 'book','person lines fill'],
                     menu_icon="app-indicator", default_index=0, orientation="horizontal",
                     styles={
    "container": {"padding": "7!important", "background-color": "#45a29e"},
    "icon": {"color": "red", "font-size": "18px"}, 
    "nav-link": {"font-size": "14px", "text-align": "left", "margin":"0px", "--hover-color": "#3b4e64"},
    "nav-link-selected": {"background-color": "#1f2833"},}
)


    

# ---- HOME PAGE ----

    # CODE LOTTIE
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# LOAD ASSETS
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
logo = Image.open(r'C:\Streamlit\stenv\img\logo1.png')

if choose == "Home":
    col1, col2 = st.columns( [0.8, 0.2])
    with col1:               # To display the header text using css style
        st.markdown(""" <style> .font {
        font-size:35px ; font-family: 'Cooper Black'; color: #66FCF1;} 
        </style> """, unsafe_allow_html=True)
        st.markdown('<p class="font">Welcome to Our Project!</p>', unsafe_allow_html=True)    
    with col2:               # To display brand log
        st.image(logo, width=130 )
    
    
    st.write("Ini adalah hackathon project kami dalam mengikuti pelatihan Women in Tech: Cybersecurity and Python dari Program Digital Talent Scholarship yang diselenggarakan oleh Kementerian Komunikasi dan Informatika (Kominfo) Republik Indonesia, yang bermitra dengan Cisco Networking. \n\n")
    st.write("[Read More about the academy>](https://digitalent.kominfo.go.id/detail/pelatihan/3161?akademiId=146)")    
    st_lottie(lottie_coding, height=300, key="coding")

    
    # ----- CODE LOTTIE ----
    def load_lottieurl(url):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()

    # ---- LOAD ASSETS ----

    # ---- HEADER SECTION ----
    with st.container():
        st.write("---")
        st.subheader("Instructor at Class S :school:")
        st.write("- Dr. Sitti Yani, M.Si.")
        st.write("- I Made Adhi Wiryawan, S.T.")

    
    
# ---- PROJECT ----
elif choose == "Project":
    # ----- CODE LOTTIE ----
    def load_lottieurl(url):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()

    # ---- LOAD ASSETS ----
    lottie_biru = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_cbvtefpb.json")
    lottie_apjalan = load_lottieurl("https://assets4.lottiefiles.com/private_files/lf30_45kfqk4d.json")
    lottie_sc = load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_2w2xmpvk.json")
    
    
    st.markdown(""" <style> .font {
    font-size:35px ; font-family: 'Cooper Black'; text-align: center; color: #66FCF1;} 
    </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font">Cybersecurity in Aviation Industry</p>', unsafe_allow_html=True)  
    st_lottie(lottie_biru, height=300, key="airplane")
    
    
    with st.container():
        st.write("---")
        left_column, right_column = st.columns(2)
        with left_column:
            st.header("Fungsi")
            st.write("##")
        with right_column:
            st_lottie(lottie_apjalan, height=300, key="code")
    with st.container():
        st.write("---")
        st.markdown("<h2 style='text-align: center; color: white;'>Smaller headline in black </h2>", unsafe_allow_html=True)
        st.header("Solusi")
        st.write("iya tuh")


    # ---- PENJELASAN -----
    with st.container():
        st.write("---")
        left_column, right_column = st.columns(2)
        with right_column:
            st.header("Fungsi")
            st.write("##")
            st.write(
                """
                Kami membuat streamlit 
                """ 
            )
            st.write("[Youtube Channel >](https://youtube.com/)")
        with left_column:
            st_lottie(lottie_sc, height=300, key="sc")



# ---- DATA PAGE ----            
elif choose == "Data":
    st.markdown(""" <style> .font {
    font-size:35px ; font-family: 'Cooper Black'; color: #66FCF1;} 
    </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font">Upload your project plan</p>', unsafe_allow_html=True)
    st.write('---')
    st.header('Data Kasus 2003-2021')
    st.subheader('Data kasus dan keterangan')
    
    # LOAD DATAFRAME
    df = pd.read_excel(
        io = './Data_Kasus.xlsx',
        engine = 'openpyxl',
        sheet_name = 'Sheet1',
        skiprows = 0,
        usecols = 'A:D',
        nrows = 27,        
    )
    
    print(df)
    

# ---- ABOUT US ----
elif choose == "About Us":
    st.markdown(""" <style> .font {
    font-size:35px ; font-family: 'Cooper Black'; color: #66FCF1; text-align: center;} 
    </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font">Get to know more about us</p>', unsafe_allow_html=True)

    with st.container():
        col1, col2, col3 = st.columns(3)

        with col1:
            st.image("./img/Ira.png")
            st.write("<h4 style='text-align: center; color: white;'>Ira Naintin Sepnanda</h4>", unsafe_allow_html=True)
            st.write("Seorang wanita")
            st.caption("Instagram: [@irasepnanda](https://instagram.com/irasepnanda/)")
            st.caption("LinkedIn: [linkedin.com/in/ira-naintin-sepnanda-17951718b](https://www.linkedin.com/in/ira-naintin-sepnanda-17951718b/)")
            

        with col2:
            st.image("./img/vita1.png")
            st.write("<h4 style='text-align: center; color: white;'>Vita Tri Utami</h4>", unsafe_allow_html=True)
            st.write("Seorang wanita")
            st.caption("Instagram: [@heyvita__tr](https://instagram.com/heyvita__tr/)")
            st.caption("LinkedIn: [linkedin.com/in/vita-tri-utami-792a16139](https://www.linkedin.com/in/vita-tri-utami-792a16139//)")
            

        with col3:
            st.image("./img/Ira.png")
            st.write("<h4 style='text-align: center; color: white;'>Putri Meliana Sari</h4>", unsafe_allow_html=True)
            st.write("Seorang wanita")
            st.caption("Instagram: [@irasepnanda](https://instagram.com/irasepnanda/)")
            st.caption("LinkedIn: [linkedin.com/in/ira-naintin-sepnanda-17951718b](linkedin.com/in/ira-naintin-sepnanda-17951718b/)")
            
# ---- CONTACT US ----
elif choose == "Contact":
    st.markdown(""" <style> .font {
    font-size:35px ; font-family: 'Cooper Black'; color: #66FCF1;} 
    </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font">Contact Form</p>', unsafe_allow_html=True)
    with st.form(key='columns_in_form2',clear_on_submit=True): #set clear_on_submit=True so that the form will be reset/cleared once it's submitted
        #st.write('Please help us improve!')
        Name=st.text_input(label='Please Enter Your Name', placeholder='Your name') #Collect user feedback
        Email=st.text_input(label='Please Enter Email',  placeholder='Your email') #Collect user feedback
        Message=st.text_input(label='Please Enter Your Message',  placeholder='Your message') #Collect user feedback
        submitted = st.form_submit_button('Submit')
        if submitted:
            st.write('Thanks for your contacting us. We will respond to your questions or inquiries as soon as possible!')
