import streamlit as st 
import pandas as pd 
import psycopg2
import openpyxl

#from streamlit_lottie import st_lottie


#st_lottie("https://lottie.host/7821495d-4a43-4f88-8eaf-b7b3f1a97a6e/RRYQvDBKOw.json")

col1, col2,col3=st.columns([3,1,3])

with col1:
    st.title('Metodología de la investigación 1') 

with col3:
    st.image('Imagenes/fernandopic.PNG',width=120)
    st.markdown('Dr. Fernando A. Núñez Moreno')
    st.caption('Docente responsable')
    st.image('/Users/alonso/Documents/projects-code/PracticeScience/Imagenes/paper.png')
    st.markdown('------')
    st.video('https://www.youtube.com/watch?v=DfDImABW3is')
    
with col1:
    st.subheader('Médico general')
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
st. subheader('Forma de trabajo y calificación')
st.markdown('La dinámica será basada en la presentación de clase y tema visto en capsulas de 25 minutos, con descansos de 5 minutos.')
st.error('Al inicio de la clase se realizará un miniexamen con preguntas aleatorizadas de todos los temas vistos en clases, estos son acumulables por lo que se recomienda repasar todo el material antes de empezar las clases')

with st.expander('Datos en los que se basa la forma de trabajo'):
    st.text('En que se basa esta metodología')

calif_df=pd.DataFrame({'col1':[1],'col3':[4]},index=['Nombre'])
df_excel=pd.read_excel('Calificación df.xlsx')
st.dataframe(df_excel)
st.table(calif_df)
st.toggle('sfd')


# Parámetros de conexión a la base de datos
dbname = 'bajacaltec_ciencia'
user = 'bajacaltec_ciencia_user'
password = 'QnVGnpcQGxEr7q9W3YDiPS4ABxSTkAVn'
host = 'dpg-cokdc7gl5elc73c3klp0-a.oregon-postgres.render.com'

# Definir la sentencia SQL para crear la tabla
create_table_query = '''
CREATE TABLE IF NOT EXISTS db (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100),
    edad INT
);
'''

# Conexión a la base de datos y creación de la tabla
try:
    conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)
    cursor = conn.cursor()
    cursor.execute(create_table_query)
    conn.commit()
    print("La tabla 'db' ha sido creada correctamente.")
except psycopg2.Error as e:
    print("Error al crear la tabla:", e)
finally:
    if conn:
        cursor.close()
        conn.close()

def insert_data(nombre, edad):
    try:
        conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)
        cursor = conn.cursor()
        insert_query = "INSERT INTO db (nombre, edad) VALUES (%s, %s)"
        cursor.execute(insert_query, (nombre, edad))
        conn.commit()
        st.success("Datos insertados correctamente en la tabla.")
    except psycopg2.Error as e:
        st.error(f"Error al insertar datos en la tabla: {e}")
    finally:
        if conn:
            cursor.close()
            conn.close()

# Crear un formulario para ingresar datos
st.title("Formulario para ingresar datos")
nombre = st.text_input("Nombre:")
edad = st.number_input("Edad:")
if st.button("Guardar"):
    if nombre and edad:
        insert_data(nombre, edad)
    else:
        st.warning("Por favor ingresa el nombre y la edad.")