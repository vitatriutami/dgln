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

# SIDEBAR    
st.sidebar.markdown("<h1 style='text-align: center; color: red;'>Homepage</h1>", unsafe_allow_html=True)                       

st.text_input("Your name:", key = "name")
st.write(":sunglasses: :sunglasses: Hello,", st.session_state.name)
st.title('\n')



