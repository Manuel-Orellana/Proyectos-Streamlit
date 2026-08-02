#librerias
import numpy as np
import altair as alt
import pandas as pd
import streamlit as st

#Cabecera de la aplicación
st.header("Cabecera de la aplicación")

#Excribiendo texto con estructura de markdawn
st.write("Hello, *World!* :sunglasses:")

#Escribiendo números
st.write(1234)

#Escribiendo dataframe de pandas
estructura_df = {"Base": [1, 2, 3, 4, 5],
                 "Elevado al cuadrado": [1, 4, 9, 16, 25]}
df = pd.DataFrame(data= estructura_df)

st.write(df)

#Escribiendo texto -> dataframe -> texto
st.write("Números y su potencia:", df, "Muchas gracias por su atención")

#Haciendo gráfico con altair
grafico = (
    alt.Chart(df)
    .mark_line(point=True)
    .encode(
        x="Base",
        y="Elevado al cuadrado"
    )
)

st.write(grafico)


