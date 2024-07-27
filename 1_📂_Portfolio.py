import json
import streamlit as st
import requests
from streamlit_lottie import st_lottie
import pandas as pd
from streamlit_option_menu import option_menu


# page settings
st.set_page_config(
    page_title=('Hello'),
    page_icon=(':wave:')
)


# animation
# def load_lottieurl(url: str):
#     r = requests.get(url)
#     if r.status_code != 200:
#         return None
#     return r.json()
# lottie_url_1 =load_lottieurl('https://lottie.host/fd453450-40e6-40c4-97a0-bb4492ee394d/HHSs1WBYaK.json')
# st_lottie(lottie_url_1, key=None)


# some title
#st.title(':blue[Welcome to my portfolio !] :sparkles:' )

#html for title
st.html("<p>" 
        "<span style='text-decoration: underline violet;text-underline-offset: 12px;text-decoration-thickness: 10px; font-size: 350%;font-weight: bold; color:#2de2e6;'"
        ">Welcome to my portfolio !<"
        "/span</p>")

# st.sidebar.success('Enjoy')

# create logo
st.logo('assets/miami.png')
# change size of logo
st.html("""
  <style>
    [alt=Logo] {
      height: 7rem;
    }
  </style>
        """)
# create text on side
st.sidebar.text('[Made with 💙 by Jacob]')


# background image
def add_bg_from_local():
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("https://preview.redd.it/car-in-miami-retro-wave-style-1600-900-v0-s2gfu8clrcma1.png?width=1080&crop=smart&auto=webp&s=4ce084275f1b88a754a266926951f59f5ee9c09f");
            background-size: cover;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
add_bg_from_local()
