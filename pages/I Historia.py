import streamlit as st
from streamlit_lottie import st_lottie
import streamlit.components.v1 as components

st.set_page_config(page_title="Timeline Example", layout="wide")

st.title('Historia de la ciencia')
st.subheader('Como llegamos al método científico')
components.iframe("https://docs.google.com/presentation/d/e/2PACX-1vSe3Fg2NFEl6VES9qmoS4vnmgEp7GTjCYrSH22k9m1afpOcgF2hWv6LKe25I8vQYZq6aRQP3xkQMnSP/embed?start=true&loop=false&delayms=5000",height=540)


from streamlit_timeline import timeline


with st.expander('Historia'):

    col1,col2,col3=st.columns([3,1,1])
    with col1:
        st.write('El origen de la ciencia es dificil de precisar ya que la evidencia de pensamientos precientíficos como las matemáticasse encuentran en diversos lugares.')
        st.info('Esto se puede considerar como evidencia para la captura de datos como transacciones, pero la importancia radica en la capacidad de guardar información')
        st.caption('January 2026')
        st.image('Imagenes/huesos.png','Marcas en un hueso de mandril encontrados en  Uganda, catalogados con una antiguedad de 20,000-18,000 años antes de cristo',width=400)
    with col3:
        st_lottie("https://lottie.host/aa4838ad-01bf-4b1d-9856-274ed8a8a77e/quNHC4nr3V.json")

 

# load data
with open('example.json', "r") as f:
    data = f.read()

# render timeline
timeline(data, height=800)
st.title('Historía de la investigación')


col1,col2=st.columns([3,1])
with col1:
    st.subheader('Babilonios')