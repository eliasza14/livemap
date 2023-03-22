import streamlit as st
import folium
import pandas as pd
import requests
import geopandas 
import shapely.geometry

st.write("Live Map Komy")


geodf = geopandas.read_file('testgeo.geojson')
st.write(geodf)