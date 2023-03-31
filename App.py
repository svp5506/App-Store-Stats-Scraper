import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image

st.set_page_config(page_title='App Ratings')
st.header('App Ratings iOS Store')

excel_file = 'reviews2.xlsx'
sheet_name = 'Sheet1'

df = pd.read_excel(excel_file,
                   sheet_name='Sheet1',
                   usecols='B:D',
                   header=0
                   )

st.dataframe(df, use_container_width=True)

pie_chart = px.pie(df,
                   title='Total Reviews by App',
                   values='Review Count',
                   names='App Name')
st.plotly_chart(pie_chart)

image = Image.open('images/iOS_App_Store_logo.png')

st.image(image,
         width=100)
