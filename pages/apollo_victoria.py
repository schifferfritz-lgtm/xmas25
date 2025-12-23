import streamlit as st
from pathlib import Path

st.markdown("# Apollo Victoria")
st.sidebar.header("Apollo Victoria")
progress_bar = st.sidebar.progress(0)
status_text = st.sidebar.empty()

path = Path(__file__).parent / "../data"
Venue_Images =  [f'{path}/apollo_victoria_indoor.jpg',
                 f'{path}/apollo_victoria_outdoor.jpg',
                 f'{path}/apollo_victoria_map.png']


st.image(Venue_Images[1], caption='Building', clamp=True)
