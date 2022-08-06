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
import matplotlib.pyplot as plt
from streamlit_option_menu import option_menu
import streamlit.components.v1 as html
from st_aggrid import AgGrid
import cv2
import plotly.express as px
import io


choose = option_menu(None, ["Home", "Project", "Planning", "About Us", "Contact"],
                     icons=['house', 'camera fill', 'kanban', 'book','person lines fill'],
                     menu_icon="app-indicator", default_index=0, orientation="horizontal",
                     styles={
    "container": {"padding": "7!important", "background-color": "#45a29e"},
    "icon": {"color": "red", "font-size": "18px"}, 
    "nav-link": {"font-size": "14px", "text-align": "left", "margin":"0px", "--hover-color": "#3b4e64"},
    "nav-link-selected": {"background-color": "#1f2833"},}
)



# ---- HOME PAGE ----
logo = Image.open(r'C:\Streamlit\stenv\img\jae.jpg')
profile = Image.open(r'C:\Streamlit\stenv\img\jae.jpg')
if choose == "Home":
    col1, col2 = st.columns( [0.8, 0.2])
    with col1:               # To display the header text using css style
        st.markdown(""" <style> .font {
        font-size:35px ; font-family: 'Cooper Black'; color: #66FCF1;} 
        </style> """, unsafe_allow_html=True)
        st.markdown('<p class="font">Hi! Welcome to Our Project!</p>', unsafe_allow_html=True)    
    with col2:               # To display brand log
        st.image(logo, width=130 )
    
    st.write("Jaemin.....\n\nTo read jaemin  posts, please visit her Medium blog at:")    
    st.image(profile, width=700 )
    
    
# ---- PROJECT ----
elif choose == "Project":
    col1, col2 = st.columns( [0.8, 0.2])
    with col1:               # To display the header text using css style
        st.markdown(""" <style> .font {
        font-size:35px ; font-family: 'Cooper Black'; color: #66FCF1;} 
        </style> """, unsafe_allow_html=True)
        st.markdown('<p class="font">Upload your photo here...</p>', unsafe_allow_html=True)
        
    with col2:               # To display brand logo
        st.image(logo,  width=150)
    #Add file uploader to allow users to upload photos
    uploaded_file = st.file_uploader("", type=['jpg','png','jpeg'])
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        
        col1, col2 = st.columns( [0.5, 0.5])
        with col1:
            st.markdown('<p style="text-align: center;">Before</p>',unsafe_allow_html=True)
            st.image(image,width=300)  

        with col2:
            st.markdown('<p style="text-align: center;">After</p>',unsafe_allow_html=True)

            converted_img = np.array(image.convert('RGB')) 
            gray_scale = cv2.cvtColor(converted_img, cv2.COLOR_RGB2GRAY)
            inv_gray = 255 - gray_scale
            blur_image = cv2.GaussianBlur(inv_gray, (125,125), 0, 0)
            sketch = cv2.divide(gray_scale, 255 - blur_image, scale=256)
            st.image(sketch, width=300)



# ---- PLANNING PAGE ----            
elif choose == "Planning":
#Add a file uploader to allow users to upload their project plan file
    st.markdown(""" <style> .font {
    font-size:35px ; font-family: 'Cooper Black'; color: #66FCF1;} 
    </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font">Upload your project plan</p>', unsafe_allow_html=True)

    uploaded_file = st.file_uploader("Fill out the project plan template and upload your file here. After you upload the file, you can edit your project plan within the app.", type=['csv'], key="2")
    if uploaded_file is not None:
        Tasks=pd.read_csv(uploaded_file)
        Tasks['Start'] = Tasks['Start'].astype('datetime64')
        Tasks['Finish'] = Tasks['Finish'].astype('datetime64')
        
        grid_response = AgGrid(
            Tasks,
            editable=True, 
            height=300, 
            width='100%',
            )

        updated = grid_response['data']
        df = pd.DataFrame(updated) 
        
        if st.button('Generate Gantt Chart'): 
            fig = px.timeline(
                            df, 
                            x_start="Start", 
                            x_end="Finish", 
                            y="Task",
                            color='Completion Pct',
                            hover_name="Task Description"
                            )

            fig.update_yaxes(autorange="reversed")          #if not specified as 'reversed', the tasks will be listed from bottom up       
            
            fig.update_layout(
                            title='Project Plan Gantt Chart',
                            hoverlabel_bgcolor='#DAEEED',   #Change the hover tooltip background color to a universal light blue color. If not specified, the background color will vary by team or completion pct, depending on what view the user chooses
                            bargap=0.2,
                            height=600,              
                            xaxis_title="", 
                            yaxis_title="",                   
                            title_x=0.5,                    #Make title centered                     
                            xaxis=dict(
                                    tickfont_size=15,
                                    tickangle = 0,
                                    rangeslider_visible=True,
                                    side ="top",            #Place the tick labels on the top of the chart
                                    showgrid = True,
                                    zeroline = True,
                                    showline = True,
                                    showticklabels = True,
                                    tickformat="%x\n",      #Display the tick labels in certain format. To learn more about different formats, visit: https://github.com/d3/d3-format/blob/main/README.md#locale_format
                                    )
                        )
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.write('---') 
            

# ---- ABOUT US ----
elif choose == "About Us":
    st.markdown(""" <style> .font {
    font-size:35px ; font-family: 'Cooper Black'; color: #66FCF1; text-align: center;} 
    </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font">Lebih lanjut mengenai kami:</p>', unsafe_allow_html=True)

    with st.container():
        col1, col2, col3 = st.columns(3)

        with col1:
            st.image("./img/Ira.png")
            st.write("<h4 style='text-align: center; color: white;'>Ira Naintin Sepnanda</h4>", unsafe_allow_html=True)
            st.write("Seorang wanita")
            st.caption("Instagram: [@irasepnanda](https://instagram.com/irasepnanda/)")
            st.caption("LinkedIn: [linkedin.com/in/ira-naintin-sepnanda-17951718b](linkedin.com/in/ira-naintin-sepnanda-17951718b/)")
            

        with col2:
            st.image("./img/vita1.png")
            st.write("<h4 style='text-align: center; color: white;'>Vita Tri Utami</h4>", unsafe_allow_html=True)
            st.write("Seorang wanita")
            st.caption("Instagram: [@heyvita__tr](https://instagram.com/heyvita__tr/)")
            st.caption("LinkedIn: [linkedin.com/in/ira-naintin-sepnanda-17951718b](linkedin.com/in/ira-naintin-sepnanda-17951718b/)")
            

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
