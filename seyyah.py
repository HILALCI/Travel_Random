import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import folium
from streamlit_folium import st_folium
from folium.plugins import Draw
import folium.plugins
from streamlit_folium import folium_static
import time

veri = pd.read_csv("./kordinat2.csv")

flag = False

def show_map(go):
    m = folium.Map(location=go.iloc[:,2:].values[0], zoom_start=10)
    folium.Marker(
        go.iloc[:,2:].values[0], popup=go.iloc[:,1:2].values[0][0]
    ).add_to(m)
    st_folium(m, width=725, returned_objects=[])


if st.sidebar.button("Let's Go"):
    flag = True
    rastgele = np.random.randint(1,81, size=(1,))[0]
    secilen = veri[veri["il_plaka"] == rastgele]
    show_map(secilen)

if flag:
    with st.sidebar:
            with st.spinner("Loading..."):
                time.sleep(1)
                st.write("Rastgele Secilen il = ",secilen.iloc[:,1:2].values[0][0])