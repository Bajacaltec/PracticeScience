import streamlit as st
from streamlit_lottie import st_lottie
import psycopg2
import datetime
import streamlit.components.v1 as components

st.set_page_config(page_title="Timeline Example", layout="wide")

st.sidebar.caption('By Baja Caltec')

Desactivar=False
contra = st.sidebar.text_input('Contraseña', type='password')

ingresar=st.sidebar.toggle('Ingresar',disabled=Desactivar)

usuarios = ('2089')

if ingresar ==True and contra in usuarios:

    st.sidebar.caption('Haz iniciado sesión')
    #Base  de datos
    # Parámetros de conexión a la base de datos
    dbname = 'bajacaltec_ciencia'
    user = 'bajacaltec_ciencia_user'
    password = 'QnVGnpcQGxEr7q9W3YDiPS4ABxSTkAVn'
    host = 'dpg-cokdc7gl5elc73c3klp0-a.oregon-postgres.render.com'

    #Crear tabla de participación
    create_table_query = '''
    CREATE TABLE IF NOT EXISTS Participaciones (
        id SERIAL PRIMARY KEY,
        nombre VARCHAR(100),
        fecha TIMESTAMP
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

    def insert_data(nombre, fecha):
        try:
            conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)
            cursor = conn.cursor()
            insert_query = "INSERT INTO Participaciones (nombre, fecha) VALUES (%s, %s)"
            cursor.execute(insert_query, (nombre, fecha))
            conn.commit()
            st.success("Datos insertados correctamente en la tabla.")
        except psycopg2.Error as e:
            st.error(f"Error al insertar datos en la tabla: {e}")
        finally:
            if conn:
                cursor.close()
                conn.close()

    st.title('Historia de la ciencia')
    st.subheader('Como llegamos al método científico')
    
    components.iframe("https://docs.google.com/presentation/d/e/2PACX-1vSe3Fg2NFEl6VES9qmoS4vnmgEp7GTjCYrSH22k9m1afpOcgF2hWv6LKe25I8vQYZq6aRQP3xkQMnSP/embed?start=true&loop=false&delayms=5000",height=540)




    #Codigo para participaciones con nombre y fecha
    st.warning('Punto de participaión')
    nombre=st.text_input('Nombre del participante')
    fecha=datetime.datetime.now()
    fecha_formateada = fecha.strftime("%Y-%m-%d %H:%M:%S")
    enviar_part=st.button('Guardar')
    if enviar_part==True:
        insert_data(nombre,fecha_formateada)

elif ingresar== True and contra not in usuarios:
    st.sidebar.error('Contraseña incorrecta')
    #Término de codigo para participaciones


