import streamlit as st 
import pandas as pd 
from streamlit_lottie import st_lottie


st_lottie("https://lottie.host/7821495d-4a43-4f88-8eaf-b7b3f1a97a6e/RRYQvDBKOw.json")


st.set_page_config('Learnscience',layout='wide')
st.title('Metodología de la investigación 1') 
st.subheader('Docentes responsables')

col1, col2=st.columns(2)
with col1:
    st.image('Imagenes/fernandopic.PNG','Cirujano General egresado del Hospital siglo XXI, México, Maestro en ciencias de la vida por parte del CICESE y aspirante a Dr. med por la universidad de Oldenburg, Alemanía',200)
with col2:
    st.image('Imagenes/fernandopic.PNG','Dr. Edgar Santos Marcial, Neurocirujano por la universidad de Heidelberg, Maestría en ciencias por, Dr. Med',200)


st. subheader('Forma de trabajo y calificación')
st.markdown('La dinámica será basada en la presentación de clase y tema visto en capsulas de 25 minutos, con descansos de 5 minutos.')
st.error('Al inicio de la clase se realizará un miniexamen con preguntas aleatorizadas de todos los temas vistos en clases, estos son acumulables por lo que se recomienda repasar todo el material antes de empezar las clases')

with st.expander('Datos en los que se basa la forma de trabajo'):
    st.text('En que se basa esta metodología')