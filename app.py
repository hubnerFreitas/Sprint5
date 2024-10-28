import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles.csv')

st.header('Dashboard de veículos  Sprint 5')

hist_button = st.button('Criar Histograma')
if hist_button:
    st.write('Criando  histograma para o conjuto de dados')

    fig = px.histogram(car_data, x="odometer")

    st.plotly_chart(fig, use_container_width=True)

disp_button = st.button('Criar gráfico de dispersão')
if disp_button:
    st.write('Criando gráfico para o conjuto de dados.')

    fig = px.scatter(car_data, x="odometer", y="price")

    st.plotly_chart(fig, use_container_width=True)
