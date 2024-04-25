import streamlit as st


col1,col2=st.columns([5,1])
with col2:
    Codigo=st.number_input('Codigo de acceso',1,step=1)

with col1:
    if Codigo==2049:
        st.subheader('Ejercicio de aprendizaje 1')
        with st.expander('Ejercicio 1'):
            st.markdown('Su origen viene de los esfuerzos para sistematizar el conocimiento y se remonta a los tiempos prehistóricos, civilizaciones del neolítico. El objetivo primario de la ciencia es (siempre ha sido y será) mejorar la calidad de vida de los humanos, y también ayuda a resolver las preguntas cotidianas')
            st.radio('Elige la opción más apropiada',['a','b'],horizontal=True)
            st.markdown('____')
    else:
        st.error('El ejercicio Ia está bloqueado')