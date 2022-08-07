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
    
    
    st.write("Ini adalah hackathon project kami dalam mengikuti pelatihan *Women in Tech: Cybersecurity and Python* dari Program Digital Talent Scholarship yang diselenggarakan oleh Kementerian Komunikasi dan Informatika (Kominfo) Republik Indonesia, yang bermitra dengan Cisco Networking. \n\n")
    st.write("[Read More about the academy>](https://digitalent.kominfo.go.id/detail/pelatihan/3161?akademiId=146)")    
    st_lottie(lottie_coding, height=300, key="coding")

    
    # CODE LOTTIE
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
    lottie_hp = load_lottieurl("https://assets4.lottiefiles.com/packages/lf20_af77tbqx.json")
    
    st.markdown(""" <style> .font {
    font-size:35px ; font-family: 'Cooper Black'; text-align: center; color: #66FCF1;} 
    </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font">Cyber Security in Aviation Industry</p>', unsafe_allow_html=True)  
    st_lottie(lottie_biru, height=300, key="airplane")
    
    # SUBPAGE 1 
    with st.container():
        st.write("---")
        left_column, right_column = st.columns(2)
        with left_column:
            st.markdown("<h2 style='text-align: left; color: #81D8D0;'>Cyber Security</h2>", unsafe_allow_html=True)
            st.write("*Cyber security* merupakan sebuah proses perlindungan program, data, sistem, maupun jaringan dari ancaman atau serangan digital. Semua, data baik itu perusahaan maupun organisasi saat ini sudah melalui sistem digital atau terkomputerisasi. Dengan ketergantungan pemakaian tersebut, mengakibat munculnya berbagai ancaman siber (*cyber attack*). Pendekatan *cyber security* yang sukses dikarenakan memiliki banyak lapisan perlindungan. Dimulai dari perlindungan pada perangkat komputer itu sendiri, jaringan, data program maupun data yang dijaga oleh keamanan.")
        with right_column:
            st_lottie(lottie_sc, height=300, key="code")
    
    # SUBPAGE 2
    with st.container():
        st.write("---")
        st.markdown("<h2 style='text-align: center; color: #81D8D0;'>Konsep dalam Cyber Security</h2>", unsafe_allow_html=True)
        st.write("Konsep dasar *cyber security* mengikuti praktik CIA Triad yang meliputi *confidentiality* (kerahasiaan), *integrity* (integritas), dan *availability* (ketersediaan).")
        if st.checkbox("Read more.."):
            st.markdown("<h4 style='text-align: left; color: #008B8B; font-weight: bold;'>Confidentiality</h4>", unsafe_allow_html=True)
            st.write("  Sesuai dengan namanya, *confidentiality* ini merupakan upaya untuk menjaga atau merahasiakan sebuah informasi maupun data, demi mencegah kebocoran atau pencurian data.")
            st.markdown("<h4 style='text-align: left; color: #008B8B; font-weight: bold;'>Integrity</h4>", unsafe_allow_html=True)
            st.write("  *Integrity* adalah memastikan bahwa semua data yang akan diakses oleh pengguna merupakan data yang akurat, konsisten dan tetap terpercaya.")
            st.markdown("<h4 style='text-align: left; color: #008B8B; font-weight: bold;'>Availability</h4>", unsafe_allow_html=True)
            st.write("  Pengertian *availability* adalah memastikan ketersediaan data. Dimana pengguna bisa mengakses data yang ingin dicari dengan lancar, mudah dan tanpa halangan.")


    # SUBPAGE 3
    with st.container():
        st.write("---")
        left_column, right_column = st.columns(2)
        with right_column:
            st.markdown("<h2 style='text-align: left; color: #81D8D0;'>Aviation Cyber Security</h2>", unsafe_allow_html=True)
            st.write("Transportasi udara merupakan sarana paling aman dibandingkan moda transportasi lainnya. Hal ini karena transportasi menggunakan pesawat terbang syarat akan peraturan dan dilakukan oleh petugas- petugas profesional yang berlisensi dibidangnya. Seperti gambar dibawh ini pelayanan sektor penerbangan  mulai dari Airport and airline management, Air Traffic control, alat bantu sistem navigasi,  sistem avionics pesawat semuanya saling terhubung menggunakan  serangkaian teknologi canggih  mencapai keselamatan penerbangan.")
        with left_column:
            st_lottie(lottie_hp, height=300, key="sc")
    
    # SUBPAGE 4
    with st.container():
        st.write("---")
        st.markdown("<h2 style='text-align: center; color: #81D8D0;'>Pentingnya Aviation Cyber Security</h2>", unsafe_allow_html=True)
        st.markdown("<h4 style='text-align: center; color: #008B8B;'>Bidang Apa Saja yang Perlu Dilindungi?</h4>", unsafe_allow_html=True)
        st.write("*Aviation cyber security* mencakup banyak hal yang dilindungi demi terjalinnya keamanan penerbangan, baik keamanan penerbangan sebelum penerbangan hingga berakhirnya proses penerbangan.")
        st.write("Berikut merupakan penjelasan singkat mengenai apa saja yang terkait dalam *aviation cyber security*")
        video1 = open("./img/aviation.mp4", "rb")
        st.video(video1)
        st.write("Credit to: https://www.youtube.com/watch?v=VXp9zaf6CT8")
        st.write("##")
        st.markdown("<h4 style='text-align: center; color: #77BFC7;'>Kompleksitas Ekosistem Penerbangan</h4>", unsafe_allow_html=True)
        st.write("Bagian-bagian dalam ekosistem penerbangan yang memerlukan penjagaan.")
        image1 = Image.open("./img/bandara.jpg")
        st.image(image1, caption="Credit to: [World Economic Forum](https://www.weforum.org/)")

    # SUBPAGE 5 - TANTANGAN ANCAMAN SIBER
    with st.container():
        st.write("---")
        st.markdown("<h2 style='text-align: center; color: #81D8D0;'>Jenis Ancaman Siber (Cyberthreat) dalam Dunia Penerbangan</h2>", unsafe_allow_html=True)
        st.write("Ancaman siber paling umum yang dihadapi industri penerbangan adalah sebagai berikut.")
        st.write("##")
        left_column, right_column = st.columns(2)
        with left_column:
            image_threat = Image.open("./img/threat.png")
            st.image(image_threat, width=330)
        with right_column:
            st.write("Click the button to read more:")
            if st.button ("Ransomware"):
                st.write("Dalam serangan ransomware, penjahat dunia maya dapat mengenkripsi dan menyandera aset digital, seperti file atau sistem komputer, dan kemudian meminta tebusan dari korban untuk mendapatkan kembali akses. Misalnya, pada Januari 2020, penjahat dunia maya meretas jaringan salah satu vendor / pihak ketiga Bandara Albany dan kemudian menyebarkan malware ke server manajemen bandara. Bandara harus membayar para peretas itu untuk memulihkan operasi.")
            if st.button ("Internal Security Threats"):
                st.write("Seorang karyawan di Bandara Heathrow mendapat ancaman cyber karena kehilangan USB yang berisi data rahasia,  yang kemudian ditemukan oleh anggota masyarakat. Laporan mengatakan bahwa USB berisi informasi tentang rute Ratu dan data pribadi sekitar 50 staf keamanan bandara.")
            if st.button ("Social Engineering : Phishing, Spoofing, and Fraud"):
                st.write("Pada Juli 2020, FBI memperingatkan domain yang memalsukan situs web bandara Amerika., setelah staf bandara dan penumpang menjadi korban email phishing dengan mengklik tautan yang terinfeksi. Pelaku berpura-pura sebagai otoritas bandara, untuk menipu penumpang yang tidak menaruh curiga. Contoh lain Pada tahun 2018, terjadi peretasan di salah satu perusahaan Australia yang mengeluarkan PAS bandara / kartu identitas keamanan kepada staf bandara yang dapat mengakses pesawat dan zona bandara yang terlarang, hal ini sangat membahayakan keamanan bandara.")
            if st.button ("Attacks on Payment System"):
                st.write("Peretas mencuri detail kartu pembayaran dan informasi pribadi lainnya dari setengah juta pelanggan British Airways. Kebocoran tersebut dapat mengakibatkan kerusakan reputasi, dan potensi kehilangan pelanggan. Untuk insiden di atas, British Airways membayar denda GDPR sebesar £183 juta untuk keamanan data yang lemah.")

    # SUBPAGE 6 - STRATEGI
    with st.container():
        st.write("---")
        st.markdown("<h2 style='text-align: center; color: #81D8D0;'>Aviation Cyber Security Strategy</h2>", unsafe_allow_html=True)
        st.markdown("<h6 style='text-align: justify; font-weight: lighter; color: white;'>ICAO (International Civil Aviation Organization), sebuah organisasi penyedia layanan cyber security dalam industri penerbangan, mengamankan sektor penerbangan  terhadap serangan cyber security secara global. Berikut strategi-strategi yang dapat diterapkan dalam aviation cyber security menurut ICAO.</h6>", unsafe_allow_html=True)
        st.write("1. Kerjasama internasional")
        st.write("2. Pemerintahan")
        st.write("3. Perundang-undangan dan peraturan yang efektif")
        st.write("4. Kebijakan tentang *cyber security*")
        st.write("5. Saling berbagi informasi")
        st.write("6. Manajemen dan perencanaan insiden darurat *cyber security*")
        st.write("7. Peningkatan kapasitas dan pelatihan tentang *cyber security*")
        st.write("##")
        st.write("Untuk lebih lengkapnya, silakan klik [disini](https://www.icao.int/cybersecurity/Pages/Cybersecurity-Strategy.aspx) dan [disini](https://www.icao.int/cybersecurity/Documents/AVIATION%20CYBERSECURITY%20STRATEGY.EN.pdf)")
    
    # SUBPAGE 7 - SOLUSI
    with st.container():
        st.write("---")
        st.markdown("<h2 style='text-align: center; color: #81D8D0;'>Cyber Resilience: Principles and Tools for Boards</h2>", unsafe_allow_html=True)
        st.markdown("<h6 style='text-align: justify; font-weight: lighter; color: white;'>World Economic Forum dalam rangka membangun ketahanan siber (*cyber resilience*) dalam industri penerbangan, pada pertengahan September 2020 hingga pertengahan Januari 2021 melakukan pelatihan terhadap perwakilan berbagai industri penerbangan benua dan menghasilkan prinsip-prinsip penerbangan berikut untuk mendukung cyber resilience.</h6>", unsafe_allow_html=True)
        image2 = Image.open("./img/res1.jpg")
        st.image(image2)
        image3 = Image.open("./img/res2.jpg")
        st.image(image3, caption="Credit to: World Economic Forum (https://www.weforum.org/)")
        
# ---- DATA PAGE ----            
elif choose == "Data":
    st.markdown(""" <style> .font {
    font-size:35px ; font-family: 'Cooper Black'; color: #66FCF1;} 
    </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font">Data Cases</p>', unsafe_allow_html=True)
    st.write('---')
    
    tab1, tab2 = st.tabs(["🪤Kasus", "🔓Risiko"])
    with tab1:
        st.subheader('Kasus Ancaman Keamanan dalam *Aviation Cyber Security* Tahun 2003-2021')
        st.write('Berikut merupakan kasus ancaman keamanan (*cyber attack*) yang pernah terjadi di dunia penerbangan internasional.')
    
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
        AgGrid(df)
        st.write("Credit to: [Jurnal MDPI](https://www.researchgate.net/publication/359155431_Cyber-Security_Challenges_in_Aviation_Industry_A_Review_of_Current_and_Future_Trends)")
    with tab2:    
        st.markdown("<h3 style='text-align: center; color: #77BFC7;'>Risiko Manajemen Industri Penerbangan dalam Aviation Cyber Security</h3>", unsafe_allow_html=True)
        st.markdown("<h6 style='text-align: justify; font-weight: lighter; color: white;'>Laporan World Economic Forum menjelaskan bahwa risiko sistemik secara inheren berbeda dengan risiko non-sistemik karena konsekuensinya lebih luas. Risiko sistemik adalah risiko kerusakan di seluruh sistem, dibandingkan dengan kerusakan di bagian-bagian individu dan komponen. Risiko ini lebih kompleks karena banyak variabel, koneksi, ketergantungan, dan saling ketergantungan menghasilkan konsekuensi yang berjenjang, seringkali tidak terduga. Industri penerbangan menghadapi tantangan yang terkait dengan risiko sistemik akibatnya juga semakin saling terkait, meluas, dan kompleks. Dengan begitu, manajemen risiko dalam industri penerbangan menjadi lebih matang menghadapi tantangan ancaman siber (cyberthreat), lebih memahami risiko dan mitigasi, dan membangun industri penerbangan yang lebih tangguh.</h6>", unsafe_allow_html=True)
        image4 = Image.open("./img/risk.jpg")
        st.image(image4)
    
    
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
            st.write("Hello, I'm a colleger in Telecommunication Engineering. I'm excited to learn new things especially in tech field. In this project, I contribute to providing content.")
            st.write("Motto: *Speak with honesty, think with sincerity, act with integrity*")
            st.caption("Instagram: [@irasepnanda](https://instagram.com/irasepnanda/)")
            st.caption("LinkedIn: [linkedin.com/in/ira-naintin-sepnanda-17951718b](https://www.linkedin.com/in/ira-naintin-sepnanda-17951718b/)")
            

        with col2:
            st.image("./img/vita1.png")
            st.write("<h4 style='text-align: center; color: white;'>Vita Tri Utami</h4>", unsafe_allow_html=True)
            st.write("I'm a freshgraduate majoring in Regional Development. I'm a fast-learner and ambitious. Currently, I'm seeking opportunities that will allow me to improve knowledge in this revolution industry era.")
            st.write("Motto: *Think outside the box. Better yet, burn the box and dance on the ashes*")
            st.caption("Instagram: [@heyvita__tr](https://instagram.com/heyvita__tr/)")
            st.caption("LinkedIn: [linkedin.com/in/vita-tri-utami-792a16139](https://www.linkedin.com/in/vita-tri-utami-792a16139//)")
            

        with col3:
            st.image("./img/putri.png")
            st.write("<h4 style='text-align: center; color: white;'>Putri Meliana Sari</h4>", unsafe_allow_html=True)
            st.write("I'm a student majoring in Information Technology. I'm currently focused on data and digital security.")
            st.write("Motto: *Vision withou execution is hallucination*")
            st.caption("Instagram: [@poetshoeoet](https://instagram.com/poetshoeoet/)")
            st.caption("LinkedIn: [linkedin.com/in/putrims](https://www.linkedin.com/in/putrims/)")
            
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
