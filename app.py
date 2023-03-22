import streamlit as st
import folium
import pandas as pd
import requests
import geopandas 
import shapely.geometry
from streamlit_folium import st_folium

st.write("Live Map Komy")


geodf = geopandas.read_file('testgeo.geojson')
st.write(geodf)
columns_view=['Περιφερειακή Ενότητα','Πληθυσμός', 'ΚΟΜΥ', 'Νοσηλευτές και λοιποί επαγγελματίες υγείας',
       'Νοσηλευτές και λοιποί επαγγελματίες υγείας που εμβολιάζουν',
       'Λοιποί επαγγελματίες υγείας που δεν εμβολιάζουν', 'Ιατροί/Βιολόγοι που πραγματοποιούν μοριακά τεστ',
       'Νοσηλευτές που πραγματοποιούν μοριακά τεστ',
       'Επαγγελματίες υγείας που πραγματοποιούν μοριακά τεστ και εμβολιάζουν','Οδηγοί']
m = geodf.explore(
     location=[40,23],
     zoom_start=6,
     tiles=None,
     column="Πληθυσμός",  # make choropleth based on "BoroName" column
     scheme="naturalbreaks",  # use mapclassify's natural breaks scheme
     tooltip=columns_view,
     popup=columns_view,
     cmap="Greens",
     legend=True, # show legend
     k=10, # use 10 bins
     legend_kwds=dict(colorbar=False), # do not use colorbar
    name="periferiakes enotites", # name of the layer in the map
    show=False
)

st_map=st_folium(m)