import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
df=pd.read_csv('data/Iris.csv')
st.set_page_config(
    page_title="IRIS FLOWER DASHBOARD",
    page_icon="✅",
    layout="wide",
)
st.title("IRIS FLOWER DASHBOARD")
with st.sidebar:
     st.header('Description')
     st.caption('Iris is a flowering plant genus of 310 accepted species with showy flowers. As well as being the scientific name, iris is also widely used as a common name for all Iris species, as well as some belonging to other closely related genera. A common name for some species is flags, while the plants of the subgenus Scorpiris are widely known as junos, particularly in horticulture. It is a popular garden flower.')
st.divider()
col1,col2=st.columns(2)
with col1:
     sp_distribution=df['Species'].value_counts(normalize=True)*100
     fig_SPE_pie = px.pie(
          values=sp_distribution,
          names=sp_distribution.index,
          title="pie Chart of Species",
          lables={}
     )
     





