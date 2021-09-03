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
original_title = '<p style="font-family:Montserrat; color:Black; font-size: 46px;">Mapping</p>'
st.markdown(original_title, unsafe_allow_html=True)
st.image('images/hackathon_full.png', width=1200)

G = nx.DiGraph([(1, 2), (1, 3), (2, 4), (2, 5), (3, 5),(4,6),(5, 7)])
roots = (v for v, d in G.in_degree() if d == 0)
leaves = (v for v, d in G.out_degree() if d == 0)
all_paths = []
for root in roots:
    for leaf in leaves:
        paths = nx.all_simple_paths(G, root, leaf)
        all_paths.extend(paths)
all_paths
hash_list= 1, 2, 3, 4, 5, 6, 7
x = st.text_input("Enter your answer here",key=id_generator())

# for i in all_paths:
#     if x in i:
#       st.write(i)

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

Lane = st.radio("Select Shipment: Status Result ",('1 (PX_1228)','2 (PX_1236)','3 (PX_1241)','4 (PX_1253)','5 (PX_1254)','6 (Clinical Site)','7 (Customer Location)'))
if Lane == '1 (PX_1228)':
    st.subheader('Status for 1 (PX_1228)')
    st.write("Approve/OK to use")
    st.subheader('RSB for 1 (PX_1228)')

elif Lane == '2 (PX_1236)':
    st.subheader('Status for 2 (PX_1236)')
    st.write("Approve/OK to use")
    st.subheader('RSB for 2 (PX_1236)')

elif Lane == '3 (PX_1241)':
    st.subheader('Status for 3 (PX_1241)')
    st.write("Reject/Do not use")
    st.subheader('RSB for 3 (PX_1241)')

elif Lane == '4 (PX_1253)':
    st.subheader('Status for 4 (PX_1253)')
    st.write("Approve/OK to use")
    st.subheader('RSB for 4 (PX_1253)')

elif Lane == '5 (PX_1254)':
    st.subheader('Status for 5 (PX_1254)')
    st.write("Approve/OK to use")
    st.subheader('RSB for 5 (PX_1254)')

elif Lane == '6 (Clinical Site)':
    st.subheader('Status for 6 (Clinical Site)')
    st.write("Approve/OK to use")
    st.subheader('RSB for 6 (Clinical Site)')

elif Lane == '7 (Customer Location)':
    st.subheader('Status for 7 (Customer Location)')
    st.write("Assess")
    st.subheader('RSB for 7 (Customer Location)')


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