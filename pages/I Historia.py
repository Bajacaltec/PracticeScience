import streamlit as st

from streamlit_timeline import timeline


# use full page width

# load data
with open('example.json', "r") as f:
    data = f.read()

# render timeline
timeline(data, height=800)
st.title('Historía de la investigación')
