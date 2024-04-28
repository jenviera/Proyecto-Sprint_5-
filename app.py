import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv') # leer los datos
build_histogram = st.checkbox('Construir un histograma')

if build_histogram: # si la casilla de verificación está seleccionada
    st.write('Construir un histograma para la columna odómetro')

    # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            
    # crear un histograma
    fig = px.histogram(car_data, x="odometer")
        
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
        

st.header('Proyecto Sprint 4: Software Development Tools')

# Agregar un párrafo debajo del encabezado
st.write("Este es un análisis de datos de vehículos. Puedes seleccionar dos tipos de visualizaciones a continuación.")


