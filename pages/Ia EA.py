import streamlit as st
import time
st.sidebar.caption('By Baja Caltec')

Desactivar=False

col1,col2=st.columns(2)
with col1:
    st.title('Historia')
st.markdown('___')

contra = st.sidebar.text_input('Contraseña', type='password')
falcho=False
ingresar=st.sidebar.toggle('Ingresar',disabled=Desactivar)

st.sidebar.caption('El conteo de 10 minutos inicia al hacer click en ingresar')
usuarios = ('2089', '234')

if ingresar ==True and contra in usuarios:
    with col2:
        st.info(f'Bienvenido {contra}, tu examen ha iniciado')
    st.subheader('EL origen de la ciencia')
    with st.form ('Evidencia de aprendizaje'):
        st.markdown('1.¿Que tipo de conocimiento crees que se pueda obtener de un razonamiento puro como el propuesto por platon, y que diferencia ves con la ciencia actual?')
        Ia=st.text_area('Pregunta 1',height=200)
        Ib=st.text_area('Pregunta 2. ¿Qué opinas de la idea de platón respecto a la inexactitud de las experiencias obtenidas por nuestros sentidos, que ejemplos conoces en los que nuestros sentidos pueden dar información erronea ante un fenomeno real? ')

    

        st.form_submit_button('Enviar respuestas')
    st.info('Reconstruye esta linea de tiempo, recuerda que cada vez que falles en un intento deberás reiniciar tu ejercicios')
    st.text('Fue el primer filosofo en cuestionar los fenomenos como naturales y no debido al deseo de los dioses')
    opciones=['Tales de mileto','Platon','Aristoteles']
    IIIa=st.radio('Opciones',opciones,horizontal=True)
    if IIIa=='Tales de mileto':
        IIIaa=st.radio('Opciones IA',opciones)
        if IIIaa=='Platon':
            IIIaaaa=st.radio('Opciones IA',opciones,key=123)
            if IIIaaaa=='Aristoteles':
                IIIaaaaa=st.radio('Opciones IA',opciones,key=1123)


        else:
            st.error('Vuelve a intentar')

    else:
        st.error('Vuelve a intentar')
            

elif ingresar==True and contra not in usuarios:
    st.sidebar.error('Contraseña incorrecta')


