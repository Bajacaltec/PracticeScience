import streamlit as st
import streamlit as st
from streamlit_timeline import timeline

st.title('Historía de la investigación')

# load data
with open('example.json', "r") as f:
    data = f.read()

# render timeline
timeline(data, height=800)