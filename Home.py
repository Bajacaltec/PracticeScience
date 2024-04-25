import streamlit as st 
import pandas as pd 
import psycopg2
import openpyxl
st.set_page_config(page_title="Timeline Example", layout="wide")




#from streamlit_lottie import st_lottie


#st_lottie("https://lottie.host/7821495d-4a43-4f88-8eaf-b7b3f1a97a6e/RRYQvDBKOw.json")

col1, col3=st.columns([5,1])

with col1:
    st.title('Metodología de la investigación I') 

with col3:
    st.image('Imagenes/fernandopic.PNG',width=100)
    st.markdown('Dr. Fernando A. Núñez Moreno')
    st.caption('M.D. MSc y especialista en cirugía general')
    st.markdown('------')
    
with col1:
    st.subheader('Medicina general')
    st.caption('Graduación por examen profresional')
    st.caption('CEUX, Tijuana Baja California, México')
    st.subheader('Especialidad en cirugía general')
    st.caption('Tesis publicada: Acute Cholecystitis Complicating Cardiac Disease: A Cohort Study From a Tertiary Care Center in Mexico City, Mexico')
    st.markdown('https://pubmed.ncbi.nlm.nih.gov/38465030/')
    st.caption('Centro Médico Nacional Siglo XXI, Ciudad de México')
    st.subheader('Maestría en ciencias de la vida con terminal en microbiología')
    st.caption('Análisis funcional de la miosina de clase II en la organización apical en el hongo filamentoso Neurospora crassa')
    st.markdown('http://cicese.repositorioinstitucional.mx/jspui/handle/1007/662')
    st.caption('CICESE, Ensenada, Baja California, México')
    st.subheader('Candidato a Dr. Med')
    st.caption('Tesis en curso, nombre provisional: Aplicación del analisis de imagenes multiespectrales en cirugía de columna de lo experimental a la clínica')
    st.caption('Oldenburg Universität, Alemania')

st.markdown('____')
with st.expander('Calificación'):

    st. subheader('Forma de trabajo y calificación')
    

    calif_df=pd.read_excel('/Users/alonso/Desktop/Metodología/Calificación df.xlsx')
    st.dataframe(calif_df)

with st.expander('Temario'):
    st.subheader('Temario')
    df_temario=pd.read_excel('/Users/alonso/Desktop/Metodología/Temario.xlsx')
    st.table(df_temario)
with st.expander('Miniexamenes'):
    st.subheader('Miniexamenes')
    st.caption('Seran realizados al inicio de todas las clases con excepción del 1er tema, las preguntas serán acumulables tomando en cuenta cualquier tema que ya se considere visto')
    st.info('Examenes de 10 preguntas con opción múltiple')
    st.caption('Con 10 minutos de tiempo para contestar')
    st.caption('Ejemplo')
    sol1,sol2=st.columns(2)
    with sol1:
        st.write('Cual es la razón por la cual se cree sucede el sesgo de confirmación')
        st.radio('Respuesta',['A','B','C'])
        st.button('Enviar respuestas')

with st.expander('Ensayo'):
    st.subheader('Pregunta abierta tipo ensayo')
    st.write('Estas se considerarán dentro de los productos de aprendizaje y se realizarán como parte del cierre de cada tema')
    st.text_area('Escribe cual crees que es la razón por la cual el desarrollo de la astronomía pudo desarrollarse de manera paralela en areas aisladas geograficamente')
    st.button('Enviar')
    