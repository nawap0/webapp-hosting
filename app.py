
import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")
st.subheader("Welcome, This is Pawan G Ramteke :wave:")
st.write("B.Tech Environmental Engineering ")
st.write("Diploma in Industrial Safety, Health, and Environment")
st.write("My journey till this point instilled in me a deep passion for environmental sustainability")

# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

#load asset

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_code_url = load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_yhTMvfGz0n.json")
lottie_code_url2 = load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_wZfLZTnsGl.json")

# my work
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("My Work")
        st.write("##")
        st.write("Project 1")
        st.write("""
    I published my final year dissertation on “Treatment of dairy waste water using PVA GEL as MBBR” in the International Journal of Engineering Research and Review. """)
    st.write("Executive Summary:")
    st.write("""Dairy is one of the industries producing wastewater characterized by high Chemical Oxygen Demand (COD), Biological Oxygen Demand (BOD). Dairy wastewaters are generally treated using biological methods such as Activated Sludge Process, Aerated lagoons, Trickling Filters, Sequencing Batch Reactor (SBR), Anaerobic Filters where all bio-reactors beds are fixed structurally, thus restricting the contact of decomposer micro-organisms and waste water with all average detention time for treatment of 24 hrs. For the first time we proposed and applied the use of PVA (Polyvinyl alcohol gel) as MBBR (Moving bed biofilm reactor). MBBR is a floating/suspended reactor which moves in the treatment tank with aerators allowing access to cover entire tank volume, thus increasing the rate of reaction. This study effectively increased speed of organic matter degradation and resulted in cutback of detention period by 12 hrs of traditional wastewater treatment with improved wastewater quality. This study was performed on a pilot scale at milk cooperative ltd (Gokul dudh) in Kolhapur. Further research proposal was presented by me to amplify the biomass attached growth on MBBR and reduce the pre-treatment timeframe.

    """)
    with right_column:
        st_lottie(lottie_code_url, height=300, key="coding")

    #st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.write("##")
        st.write("Project 2")
        st.write("Abstract: Identification of potential fishing habitat zone using satellite imagery")
        st.write("Executive Summary:")
        st.write("""Fishes are found in such areas where phytoplankton (Primary producers in ocean doing photosynthesis)
         up well as a result of mixing of warm and cold currents. Ideal conditions for fish aggregation. The study uses 
         satellite data on Chlorophyll and Sea Surface temperature from Ocean and Land Color Instrument (OLCI), Sea and 
         Land Surface Temperature Radiometer (SLSTR) instrument onboard Sentinel 3 satellite from ESA.

Chlorophyll-A band from OLCI and Sea Surface Temperature from SLSTR in raster images at 300 m resolution were used in a 
case study for detecting Sardine fishing zones in Mediterranean Sea. Their migration pattern in Mediterranean Sea is in 
July where the ocean water having Chlorophyll A concentration range of 0.2-20 Rf and SST range of 22.5-28.5 oC demarcate
 the habitat for Sardine fishes.

I am in the process of replicating the case study and workflow to process satellite imagery in ESA SNAP software 
Intersecting pixels where Chl-A and SST ranges intersect, giving ideal sardine fishing zones in Indian ocean regions.
""")
    with right_column:
        st_lottie(lottie_code_url2, height=300)

# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

# Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
contact_form = """
    <form action="https://formsubmit.co/pawanramteke363@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
left_column, right_column = st.columns(2)
with left_column:
    st.markdown(contact_form, unsafe_allow_html=True)
with right_column:
    st.empty()