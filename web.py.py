from PIL import Image

import requests

import streamlit as st


from streamlit_lottie import st_lottie

st.set_page_config(page_title="HIBA'S WEBSITE NO.1", page_icon="👽",layout="wide")
def load_lottieurl(url):
    r=requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()
lottie_coding = load_lottieurl ("https://lottie.host/bcc365f1-f2ed-47ba-89ea-c05e011eccaf/BlnV6Nucng.json")
img_contact_form=Image.open("C:\PythonProject/photo_2025-03-27_22-53-39.jpg")
photo_2025=Image.open("C:\PythonProject/photo_2025-03-27_22-53-39.jpg")
with st.container():
    st.subheader("Ahlan ahlan 👋.")
    st.title(" Tajruba raqam  1️⃣  ️to program a website. ")
    st.write(" Inshallah bash esh daka.")
with st.container():
    st.write("---")
    l_column, r_column = st.columns(2)
    with l_column:
        st.header("How did i programmed this website?")
        st.write("##")
        st.write("I used python, with youtube to learn and i strongly recommend it ... its fun 😸. ")
        st.write("[For example this >](https://youtu.be/VqgUkExPvLY?si=g1gpehIRFBgNCCR7)")
with r_column:
    st_lottie(lottie_coding, height=300, key="coding")
with st.container():
    st.write("---")
    st.header("Is learning programming worth it?")
    st.write("#")
    st.write("Yeah, for sure Programming is everywhere now, and learning it can get you good jobs and help you really understand how tech works instead of just using it and walla its fun.")
    st.write("#")
    image_column, text_column= st.columns((1,2))
    with image_column:
        st.image(photo_2025)
    with text_column:
        st.subheader("Most famous programming languages:")
        st.write("Ofc there are hundreds but i chose the most used one.")
        st.markdown("[Watch this>](https://youtu.be/EFmxPMdBqmU?si=clAc79XptDdxeLY-)")
with st.container():
    st.write("Bo zanyari zyatr tkaya maw3id 7jz bkan😐")
    st.write("just kidding u can use youtube, google, ai, books and textbooks, courses or just ask someone who knows.")

