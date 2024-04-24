import streamlit as st 
import pandas as pd 
import psycopg2

#from streamlit_lottie import st_lottie


#st_lottie("https://lottie.host/7821495d-4a43-4f88-8eaf-b7b3f1a97a6e/RRYQvDBKOw.json")


st.title('Metodología de la investigación 1') 
st.subheader('Docente responsable')

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

import psycopg2

# Parámetros de conexión a la base de datos
dbname = 'bajacaltec_ciencia'
user = 'bajacaltec_ciencia_user'
password = 'QnVGnpcQGxEr7q9W3YDiPS4ABxSTkAVn'
host = 'dpg-cokdc7gl5elc73c3klp0-a.oregon-postgres.render.com'

# Definir la sentencia SQL para crear la tabla
create_table_query = '''
CREATE TABLE db (
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
