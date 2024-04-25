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
