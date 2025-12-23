import streamlit as st
from pathlib import Path

st.markdown("# Picadilly Theatre")
st.sidebar.header("Picadilly Theatre")

path = Path(__file__).parent / "../data"
Venue_Images =  [f'{path}/picadilly_indoor.jpg',
                 f'{path}/picadilly_outdoor.jpeg',
                 f'{path}/picadilly_map.png']

col1, col2 = st.columns([1,1])
col1.image(Venue_Images[0], caption='Interior', clamp=True)
col2.image(Venue_Images[1], caption='Building', clamp=True)

st.write('## How to get here:')
st.write(':round_pushpin: Adress: 16 Denman St, London W1D 7DY')
st.write(':round_pushpin::railway_car: Tube Station: Piccadilly Circus Underground Station')
st.write(':railway_car: Tube Lines: Piccadilly Circus Underground Station')
st.write(':walking: Walking Distance: 0.2 km, about 3 min')


st.write('#### Find it on maps:')
st.image(Venue_Images[2], caption='Location', clamp=True)

