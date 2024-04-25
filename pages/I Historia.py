import streamlit as st
st.set_page_config(page_title="Timeline Example", layout="wide")

st.title('Historia de la ciencia')
st.subheader('Como llegamos al método científico')

from streamlit_timeline import timeline
import streamlit as st

col1,col2=st.columns([3,1])
with col1:
    st.write('El origen de la ciencia es dificil de precisar ya que la evidencia de pensamientos precientíficos como las matemáticasse encuentran en diversos lugares.')
    st.info('Esto se puede considerar como evidencia para la captura de datos como transacciones, pero la importancia radica en la capacidad de guardar información')

with col2:
    st.image('Imagenes/huesos.png','Marcas en un hueso de mandril encontrados en  Uganda, catalogados con una antiguedad de 20,000-18,000 años antes de cristo',width=150)


# load data
with open('example.json', "r") as f:
    data = f.read()

# render timeline
timeline(data, height=800)
st.title('Historía de la investigación')


col1,col2=st.columns([3,1])
with col1:
    st.subheader('Babilonios')