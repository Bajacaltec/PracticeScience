import streamlit as st
import time

Activar=False

st.title('Historia')
st.markdown('___')

contra = st.sidebar.text_input('Contraseña', type='password')
falcho=False
ingresar=st.sidebar.toggle('Ingresar',disabled=Activar)

st.sidebar.caption('El conteo de 10 minutos inicia al hacer click en ingresar')
usuarios = ('123', '234')

if ingresar ==True and contra in usuarios:
    st.info(f'Bienvenido {contra}, tu examen ha iniciado')
    with st.form ('Examen 1'):
        st.text_input('Pregunta 1')
        st.form_submit_button('Enviar respuestas')

else:
    st.sidebar.error('La contraseña es incorrecta. Por favor, inténtalo de nuevo.')


