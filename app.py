# import streamlit as st
# import folium
# import pandas as pd
# import requests
# import geopandas 
# import shapely.geometry
# from streamlit_folium import st_folium

# # st.write("Live Map Komy")


# # @st.experimental_memo
# # def get_data(geojson):
    
# #     geodf=geopandas.read_file(geojson)
# #     return geodf

# # geodata =get_data('testgeo.geojson')

# # geodf = geopandas.read_file('testgeo.geojson')

# # m = geodata.explore(
# #      location=[40,23],
# #      zoom_start=6,
# #      tiles=None,
# #      column="Πληθυσμός",  # make choropleth based on "BoroName" column
# #      scheme="naturalbreaks",  # use mapclassify's natural breaks scheme
# #      tooltip=columns_view,
# #      popup=columns_view,
# #      cmap="Greens",
# #      legend=True, # show legend
# #      k=10, # use 10 bins
# #      legend_kwds=dict(colorbar=False), # do not use colorbar
# #     name="periferiakes enotites", # name of the layer in the map
# #     show=False
# # )

# # st_map=st_folium(m)






# # import streamlit as st
# # import pandas as pd
# # import folium
# # from streamlit_folium import st_folium

# APP_TITLE = 'Fraud and Identity Theft Report'
# APP_SUB_TITLE = 'Source: Federal Trade Commission'

# # def display_time_filters(df):
# #     year_list = list(df['Year'].unique())
# #     year_list.sort()
# #     year = st.sidebar.selectbox('Year', year_list, len(year_list)-1)
# #     quarter = st.sidebar.radio('Quarter', [1, 2, 3, 4])
# #     st.header(f'{year} Q{quarter}')
# #     return year, quarter

# # def display_state_filter(df, state_name):
# #     state_list = [''] + list(df['State Name'].unique())
# #     state_list.sort()
# #     state_index = state_list.index(state_name) if state_name and state_name in state_list else 0
# #     return st.sidebar.selectbox('State', state_list, state_index)

# # def display_report_type_filter():
# #     return st.sidebar.radio('Report Type', ['Fraud', 'Other'])

# def display_map(df):
#     st.write("inside display map")
#     map = folium.Map(location=[38, -96.5], zoom_start=4, scrollWheelZoom=False, tiles='CartoDB positron')
    
#     choropleth = folium.Choropleth(
#         geo_data='testgeo.geojson',
#         data=df,
#         columns=('Πληθυσμός'),
#         # key_on='feature.properties.per_enotita',
#         line_opacity=0.8,
#         highlight=True
#     )
#     choropleth.geojson.add_to(map)

#     # df_indexed = df.set_index('State Name')

#     # for feature in choropleth.geojson.data['features']:
#     #     state_name = feature['properties']['name']
#     #     feature['properties']['population'] = 'Population: ' + '{:,}'.format(df_indexed.loc[state_name, 'State Pop'][0]) if state_name in list(df_indexed.index) else ''
#     #     feature['properties']['per_100k'] = 'Reports/100K Population: ' + str(round(df_indexed.loc[state_name, 'Reports per 100K-F&O together'][0])) if state_name in list(df_indexed.index) else ''

#     # choropleth.geojson.add_child(
#     #     folium.features.GeoJsonTooltip(['name', 'population', 'per_100k'], labels=False)
#     # )
    
#     st_map = st_folium(map, width=700, height=450)

#     # state_name = ''
#     # if st_map['last_active_drawing']:
#     #     state_name = st_map['last_active_drawing']['properties']['name']
#     # return state_name

# # def display_fraud_facts(df, year, quarter, report_type, state_name, field, title, string_format='${:,}', is_median=False):
# #     df = df[(df['Year'] == year) & (df['Quarter'] == quarter)]
# #     df = df[df['Report Type'] == report_type]
# #     if state_name:
# #         df = df[df['State Name'] == state_name]
# #     df.drop_duplicates(inplace=True)
# #     if is_median:
# #         total = df[field].sum() / len(df[field]) if len(df) else 0
# #     else:
# #         total = df[field].sum()
# #     st.metric(title, string_format.format(round(total)))

# def main():
#     st.set_page_config(APP_TITLE)
#     st.title(APP_TITLE)
#     st.caption(APP_SUB_TITLE)

#     #Load Data
#     geodf=geopandas.read_file('testgeo.geojson')
#     st.write(geodf)
#     columns_view=['Περιφερειακή Ενότητα','Πληθυσμός', 'ΚΟΜΥ', 'Νοσηλευτές και λοιποί επαγγελματίες υγείας',
#         'Νοσηλευτές και λοιποί επαγγελματίες υγείας που εμβολιάζουν',
#         'Λοιποί επαγγελματίες υγείας που δεν εμβολιάζουν', 'Ιατροί/Βιολόγοι που πραγματοποιούν μοριακά τεστ',
#         'Νοσηλευτές που πραγματοποιούν μοριακά τεστ',
#         'Επαγγελματίες υγείας που πραγματοποιούν μοριακά τεστ και εμβολιάζουν','Οδηγοί']
#     # df_continental = pd.read_csv('data/AxS-Continental_Full Data_data.csv')
#     # df_fraud = pd.read_csv('data/AxS-Fraud Box_Full Data_data.csv')
#     # df_median = pd.read_csv('data/AxS-Median Box_Full Data_data.csv')
#     # df_loss = pd.read_csv('data/AxS-Losses Box_Full Data_data.csv')

#     #Display Filters and Map
#     # year, quarter = display_time_filters(df_continental)
#     state_name = display_map(geodf)
#     # state_name = display_state_filter(df_continental, state_name)
#     # report_type = display_report_type_filter()

#     #Display Metrics
#     # st.subheader(f'{state_name} {report_type} Facts')

#     # col1, col2, col3 = st.columns(3)
#     # with col1:
#     #     display_fraud_facts(df_fraud, year, quarter, report_type, state_name, 'State Fraud/Other Count', f'# of {report_type} Reports', string_format='{:,}')
#     # with col2:
#     #     display_fraud_facts(df_median, year, quarter, report_type, state_name, 'Overall Median Losses Qtr', 'Median $ Loss', is_median=True)
#     # with col3:
#     #     display_fraud_facts(df_loss, year, quarter, report_type, state_name, 'Total Losses', 'Total $ Loss')        


# if __name__ == "__main__":
#     main()



import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
import geopandas 


APP_TITLE = 'Fraud and Identity Theft Report'
APP_SUB_TITLE = 'Source: Federal Trade Commission'



def display_map(geodf):
    st.write(geodf)
    map = folium.Map(location=[38, -96.5], zoom_start=4, scrollWheelZoom=False, tiles='CartoDB positron')
    
    choropleth = folium.Choropleth(
        geo_data=geodf,
        data=geodf,
        columns=('per_enotita','Πληθυσμός'),
        key_on='properties.LEKTIKO',
        line_opacity=0.8,
        highlight=True
    )
    choropleth.add_to(map)

   
    
    st_map = st_folium(map, width=700, height=450)

    # st_map2=st_folium(st_map)
    state_name = ''
    if st_map['last_active_drawing']:
        state_name = st_map['last_active_drawing']['properties']['LEKTIKO']
    return state_name



def main():
    st.set_page_config(APP_TITLE)
    st.title(APP_TITLE)
    st.caption(APP_SUB_TITLE)

    #Load Data
    # df_continental = pd.read_csv('AxS-Continental_Full Data_data.csv')
    # geodf=geopandas.read_file('testgeo.geojson')
    # geojson_url="https://raw.githubusercontent.com/michalis-raptakis/greece-region-units-geojson/master/greece-region-units-geojson.json"
    geodf = geopandas.read_file('testgeo.geojson')

    # map_data3= pd.read_excel('komgeodata.xlsx',dtype={'KALCODE':str})

    #Display Filters and Map
    # year, quarter = display_time_filters(df_continental)
    state_name = display_map(geodf)


    #Display Metrics
    st.subheader(f'{state_name} Facts')

    # col1, col2, col3 = st.columns(3)
    # with col1:
    #     display_fraud_facts(df_fraud, year, quarter, report_type, state_name, 'State Fraud/Other Count', f'# of {report_type} Reports', string_format='{:,}')
    # with col2:
    #     display_fraud_facts(df_median, year, quarter, report_type, state_name, 'Overall Median Losses Qtr', 'Median $ Loss', is_median=True)
    # with col3:
    #     display_fraud_facts(df_loss, year, quarter, report_type, state_name, 'Total Losses', 'Total $ Loss')        


if __name__ == "__main__":
    main()
