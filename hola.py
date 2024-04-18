
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Creamos el título de la App
st.title('Titanic App')
st.header('Titanic Graphs - App')
st.write("GRAPHICS OF THE TITANIC DATASET")

titanic_link = 'Titanic.csv'
titanic_data = pd.read_csv(titanic_link)
st.dataframe(titanic_data.sample(10))

# muestran a continuación:
fig, ax = plt.subplots()
ax.hist(titanic_data['Fare'], bins=30, color='r', alpha=0.5)
st.header("Histograma del Titanic")
st.pyplot(fig)