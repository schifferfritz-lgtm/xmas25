import streamlit as st
from pathlib import Path

st.markdown("# Apollo Victoria")
st.sidebar.header("Apollo Victoria")

path = Path(__file__).parent / "../data"
Venue_Images =  [f'{path}/apollo_victoria_indoor.jpg',
                 f'{path}/apollo_victoria_outdoor.jpg',
                 f'{path}/apollo_victoria_map.png']


st.image(Venue_Images[1], caption='Building', clamp=True)
