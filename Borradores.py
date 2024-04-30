from streamlit_timeline import timeline
import streamlit as st



# use full page width

# load data
with open('example.json', "r") as f:
    data = f.read()

# render timeline
timeline(data, height=800)
st.title('Historía de la investigación')

st.subheader('Participación 1')
st.info('Cual consideras que es el inicio de la ciencia')
col1,col2=st.columns(2)
with col1:
    st.number_input('Primer participación',0)
    st.number_input('Segunda participación',0)
with col2:
    st.number_input('3er participación',0)
    st.number_input('4ta participación',0)






#
import streamlit as st
import psycopg2

st.subheader('Examen 1')
st.caption('La historia de la ciencia, 4000 años')

clave=st.sidebar.number_input('Introduce la clave del examen',step=1)


if clave==123:

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
    nombre = st.text_input("Nombre:")
    edad = st.number_input("Edad:")
    if st.button("Guardar"):
        if nombre and edad:
            insert_data(nombre, edad)
        else:
            st.warning("Por favor ingresa el nombre y la edad.")
else:
    st.error('El examen se encuentra cerrado')


import streamlit.components.v1 as components

components.iframe("https://docs.google.com/presentation/d/e/2PACX-1vSe3Fg2NFEl6VES9qmoS4vnmgEp7GTjCYrSH22k9m1afpOcgF2hWv6LKe25I8vQYZq6aRQP3xkQMnSP/embed?start=true&loop=false&delayms=5000",height=540)

#iframe
    # load data
    with open('example.json', "r") as f:
        data = f.read()

    # render timeline
    timeline(data, height=800)

#st.markdown cambiar texto:
st.markdown('''
    :red[Streamlit] :orange[can] :''')
    texto=texto_html = """
<div style='color: red; font-size: 32px; font-family: Arial,font-weight: bold, sans-serif; text-align: right; transition: transform 0.3s ease-in-out;'>
    Hover over me!
</div>
"""