import streamlit as st
import pandas as pd 
import numpy as np
from PIL import Image
import pydeck as pdk
from urllib.error import URLError
import altair as alt
from collections import Counter 
import datetime
from datetime import date
import joblib
import pandas as pd
import numpy as np
from sklearn.model_selection import cross_val_score, GridSearchCV
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import MinMaxScaler
import logging
import threading
from copy import copy
import scipy
from math import radians, cos, sin, asin, sqrt, atan2
from streamlit_folium import folium_static
import folium
import random
import plotly.graph_objects as go
from plotly import tools
import plotly.offline as py
import plotly.express as px
import plotly.graph_objs as go
import networkx as nx

st.set_page_config(layout='wide')
#Header
# primaryColor="#d33682"
# backgroundColor = '#273346'

st.image('images/logo.png')

##########################################################################
####### Analysis 
### text
original_title = '<p style="font-family:Montserrat; color:#1A212E; font-size: 46px;">Mapping: Journey of a kit</p>'
st.markdown(original_title, unsafe_allow_html=True)
st.image('images/hackathon_full.png', width=1500)

# all_paths
original_title = '<p style="font-family:Montserrat; color:#1A212E; font-size: 46px;">Path Of A Shipment</p>'
st.markdown(original_title, unsafe_allow_html=True)
if __name__ == '__main__':
    input = st.empty()
    x = st.number_input("Enter Shipment id/node number to get its path")

    if x:
        G = nx.DiGraph([(1, 2), (1, 3), (2, 4), (2, 5), (3, 5),(4,6),(5, 7)])
        roots = (v for v, d in G.in_degree() if d == 0)
        leaves = (v for v, d in G.out_degree() if d == 0)
        all_paths = []
        for root in roots:
            for leaf in leaves:
                paths = nx.all_simple_paths(G, root, leaf)
                all_paths.extend(paths)

        path_list= []
        for i in all_paths:
            if x in i:
                path_list.append(i)
        # path_list       
        dic = {1: "1(PX_1228)", 2:"2(PX_1241)", 3:"3(PX_1241)", 4:"4(PX_1253)", 5:"5(PX_1254)", 6:"6(Clinical Site)", 7:"7(Customer Location)"}    
        for i in path_list:
            i_new=[dic.get(n, n) for n in i]
            st.write(i_new)


# option = st.multiselect('1 (PX_1228)',('2 (PX_1241)', '3 (PX_1241)', '4 (PX_1253)','5 (PX_1254)','6 (Clinical Site)','7 (Customer Location)'))
# st.write('You selected:', option)

    



# path = st.radio("Select Node to get mapping ",('1 (PX_1228)','2 (PX_1236)','3 (PX_1241)','4 (PX_1253)','5 (PX_1254)','6 (Clinical Site)','7 (Customer Location)'))
# if path == '1 (PX_1228)':
#     st.subheader('Mapping for 1 (PX_1228)')


# elif path == '2 (PX_1236)':
#     st.subheader('Mapping  for 2 (PX_1236)')

# elif path == '3 (PX_1241)':
#     st.subheader('Mapping  for 3 (PX_1241)')

# elif path == '4 (PX_1253)':
#     st.subheader('Mapping  for 4 (PX_1253)')

# elif path == '5 (PX_1254)':
#     st.subheader('Mapping for 5 (PX_1254)')


# elif path == '6 (Clinical Site)':
#     st.subheader('Mapping  for 6 (Clinical Site)')

# elif path == '7 (Customer Location)':
#     st.subheader('Mapping  for 7 (Customer Location)')




b_title = '<p style="font-family:Montserrat; color:Black; font-size: 46px;">Status/ RSB</p>'
st.markdown(b_title, unsafe_allow_html=True)

Lane = st.radio("Select Shipment: Status Result ",('1 (PX_1228)','2 (PX_1236)','3 (PX_1241)','4 (PX_1253)','5 (PX_1254)'))
if Lane == '1 (PX_1228)':
    st.subheader('Status for 1 (PX_1228)')
    st.write("Spent less than 13 days in range 1 to 15: Approve/OK to use")
    st.write("Spent less than 5 days in range 15 to 20: Assess")
    st.write("Spent less than 2 days in range above 20: Assess")
    st.subheader('RSB for 1 (PX_1228): 86.70%')

elif Lane == '2 (PX_1236)':
    st.subheader('Status for 2 (PX_1236)')
    st.write("Spent less than 2 days in range -4 to 1:Assess")
    st.write("Spent less than 13 days in range 1 to 15:Approve/OK to use")
    st.subheader('RSB for 2 (PX_1236): 99.15%')

elif Lane == '3 (PX_1241)':
    st.subheader('Status for 3 (PX_1241)')
    st.write("Spent less than 13 days in range 1 to 15: Approve/OK to use")
    st.write("Spent less than 5 days in range 15 to 20: Access")
    st.write("Spent less than 2 days in range above 20: Access")
    st.subheader('RSB for 3 (PX_1241): 97.46%')

elif Lane == '4 (PX_1253)':
    st.subheader('Status for 4 (PX_1253)')
    st.write("Spent less than 13 days in range 1 to 15:Approve/OK to use")
    st.write("Spent less than 5 days in range 15 to 20: Assess")
    st.subheader('RSB for 4 (PX_1253): 99.06%')

elif Lane == '5 (PX_1254)':
    st.subheader('Status for 5 (PX_1254)')
    st.write("Spent less than 2 days in range -4 to 1: Assess")
    st.write("Spent less than 13 days in range 1 to 15: Approve/OK to use")
    st.subheader('RSB for 5 (PX_1254): 97.48%')

# elif Lane == '6 (Clinical Site)':
#     st.subheader('Status for 6 (Clinical Site)')
#     st.write("Approve/OK to use")
#     st.subheader('RSB for 6 (Clinical Site)')

# elif Lane == '7 (Customer Location)':
#     st.subheader('Status for 7 (Customer Location)')
#     st.write("Assess")
#     st.subheader('RSB for 7 (Customer Location)')

b_title = '<p style="font-family:Montserrat; color:Black; font-size: 46px;">Kit Level Cummulative RSB</p>'
st.markdown(b_title, unsafe_allow_html=True)

kit = st.radio("Select Shipment: Status Result ",('Kit 1','Kit 2','Kit 3'))
if kit == 'Kit 1':
    st.subheader('RSB for Kit 1: 84.92 %')

elif kit== 'Kit 2':
    st.subheader('RSB for Kit 2: 83.34%')

elif kit == 'Kit 3':
    st.subheader('RSB for Kit 3: 81.65%')
#### 

elif Lane_fork_day == 'Shreveport':
    st.image(image= Image.open('images/Shreveport.png'),width=370)
    st.write('Shreveport does not have any fork, So we are considering the start day for the analysis.')
    result2=pd.read_csv('data/fork/time_S_day.csv')
    chart= alt.Chart(result2).mark_bar( color='orange', size = 30).encode(
        x = alt.X('weekday',axis=alt.Axis(labelAngle=0),sort=alt.EncodingSortField(field="weekday", op="count", order='ascending')),
        y=alt.Y('Count'),
        tooltip=["Count",'weekday']
    ).properties (title='Start Day of Shipments (Shreveport lane)',width = 400)
    st.subheader('Chart 2.2.D: Start Day of Shipments (Shreveport lane)')
    chart
    ### Weekday




###################################################################################################
###################################################################################################
###################################################################################################