import streamlit as st

st.text('Prueba')
history_slider=st.select_slider('Historía de la ciencia',('historia','prehistoria'))
if history_slider=='historia':
    st.text('Prueba')
    st.number_input('Prueba')
