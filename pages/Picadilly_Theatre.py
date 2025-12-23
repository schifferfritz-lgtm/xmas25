import streamlit as st
from pathlib import Path

st.set_page_config(page_title="Apollo Victoria", page_icon="🌍")

st.markdown("# Picadilly Theatre")
st.sidebar.header("Picadilly Theatre")

path = Path(__file__).parent / "../data"
Venue_Images =  [f'{path}/picadilly_indoor.jpg',
                 f'{path}/picadilly_outdoor.jpg',
                 f'{path}/picadilly_map.png']


st.image(Venue_Images[1], caption='Building', clamp=True)
