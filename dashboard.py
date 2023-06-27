import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title='App Ratings')

tab1, tab2, tab3 = st.tabs(["📊 Combined Ratings", "📱 iOS Ratings", "📱 Android Ratings"])

iOS_file = 'iOSratings.xlsx'
Android_file = 'AndroidRatings.xlsx'
Combined_file = 'combinedRatings.xlsx'
sheet_name = 'Sheet1'

dfCombined = pd.read_excel(Combined_file,
                   sheet_name,
                   usecols='A:I',
                   header=0
                   )
dfCombined = dfCombined.sort_values(by=['Overall App Rating'],ascending=False)
dfCombined = dfCombined.reset_index(drop=True)

dfiOS = pd.read_excel(iOS_file,
                   sheet_name,
                   usecols='A:E',
                   header=0
                   )
dfiOS = dfiOS.sort_values(by=['iOS App Rating'],ascending=False)
dfiOS = dfiOS.reset_index(drop=True)
# styler = dfiOS.style.hide_index()
# st.write(styler.to_html(), unsafe_allow_html=True)

dfAndroid = pd.read_excel(Android_file,
                   sheet_name,
                   usecols='A:I',
                   header=0
                   )
dfAndroid = dfAndroid.sort_values(by=['Android App Rating'],ascending=False)
dfAndroid = dfAndroid.reset_index(drop=True)

with tab1:
    st.header('App Store Ratings')
    st.dataframe(dfCombined, use_container_width=True)
    pie_chart = px.pie(dfCombined,
        title='Total Reviews by App',
        values='Total Reviews',
        names='App Name')
    st.plotly_chart(pie_chart, use_container_width=True)

with tab2:
    st.header('iOS Store App Rating')
    st.dataframe(dfiOS, use_container_width=True)
    pie_chart = px.pie(dfiOS,
                    title='Total Reviews by App',
                    values='iOS Total Reviews',
                    names='App Name')
    st.plotly_chart(pie_chart, use_container_width=True)

with tab3:
    st.header('Android Store App Ratings')
    st.dataframe(dfAndroid, use_container_width=True)
    pie_chart = px.pie(dfAndroid,
                    title='Total Reviews by App',
                    values='Android Total Reviews',
                    names='App Name'
                    )
    st.plotly_chart(pie_chart, use_container_width=True)
