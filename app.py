import pandas as pd
import plotly.express as px
import streamlit as st
import numpy as np

car_data = pd.read_csv('vehicles_us.csv') # leer los datos

st.header('Proyecto Sprint 4: Software Development Tools')
st.write('Prueba')

# Agregar un párrafo debajo del encabezado
st.write("Este es un análisis de datos de vehículos. Puedes seleccionar dos tipos de visualizaciones a continuación.")

# Crear casillas de verificación para seleccionar el tipo de gráfico
hist_checkbox = st.checkbox('Histograma de millaje de vehículos', key='hist_checkbox')
scatter_checkbox = st.checkbox('Diagrama de dispersión de precio vs millaje', key='scatter_checkbox')

# Verificar qué casilla de verificación está seleccionada
if hist_checkbox: 
    # crear un histograma
    fig = px.histogram(car_data, x="odometer", title='Histograma de millaje de vehículos')        
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
    # escribir un mensaje
    st.write('A continuación algunos estadísticos descriptivos sobre la variable de millaje de los vehículos:')            
    # calcular y mostrar la media, mediana y desviación estándar
    st.write(f"Media: {car_data['odometer'].mean():,.0f}, "
             f"Mediana: {car_data['odometer'].median():,.0f}, "
             f"Desviación Estándar: {car_data['odometer'].std():,.0f}")

if scatter_checkbox:     
    # crear el gráfico de dispersión con Plotly Express
    fig2 = px.scatter(car_data, x='odometer', y='price', title='Diagrama de dispersión de precio vs millaje')
    # costrar el gráfico usando st.plotly_chart()
    st.plotly_chart(fig2, use_container_width=True)
    # escribir un mensaje
    st.write('Precio y millaje se encuentran inversamente correlacionados.')
    # calcular el coeficiente de correlación y mostrarlo con tres decimales
    correlation = car_data['odometer'].corr(car_data['price'])
    st.write(f"Coeficiente de correlación: {correlation:.3f}")


