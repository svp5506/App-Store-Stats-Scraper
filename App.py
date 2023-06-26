import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title='App Ratings')

tab1, tab2, tab3 = st.tabs(["📊 Combined Ratings", "📱 iOS Ratings", "📱 Android Ratings"])

iOS_file = 'iOSratings.xlsx'
Android_file = 'AndroidRatings.xlsx'
sheet_name = 'Sheet1'

dfiOS = pd.read_excel(iOS_file,
                   sheet_name='Sheet1',
                   usecols='B:F',
                   header=0
                   )
dfiOS = dfiOS.sort_values(by=['App Rating'],ascending=False)
dfiOS = dfiOS.reset_index(drop=True)
# styler = dfiOS.style.hide_index()
# st.write(styler.to_html(), unsafe_allow_html=True)

dfAndroid = pd.read_excel(Android_file,
                   sheet_name='Sheet1',
                   usecols='B:J',
                   header=0
                   )
dfAndroid = dfAndroid.sort_values(by=['Star Rating'],ascending=False)
dfAndroid = dfAndroid.reset_index(drop=True)

with tab1:
    st.header('App Store Ratings')

with tab2:
    st.header('App Ratings iOS Store')
    st.dataframe(dfiOS, use_container_width=True)
    pie_chart = px.pie(dfiOS,
                    title='Total Reviews by App',
                    values='Review Count',
                    names='App Name')
    st.plotly_chart(pie_chart, use_container_width=True)

with tab3:
    st.header('App Ratings Android Store')
    st.dataframe(dfAndroid, use_container_width=True)
    pie_chart = px.pie(dfAndroid,
                    title='Total Reviews by App',
                    values='Total Reviews',
                    names='App Name'
                    )
    st.plotly_chart(pie_chart, use_container_width=True)
