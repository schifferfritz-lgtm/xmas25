import streamlit as st
from pathlib import Path

st.markdown("# St. Martin’s Theatre")

path = Path(__file__).parent / "../data"
Venue_Images =  [f'{path}/st_martin_indoor.jpg',
                 f'{path}/st_martin_outdoor.jpg',
                 f'{path}/st_martin_map.png']


col1, col2 = st.columns([1,1])
col1.image(Venue_Images[0], caption='Interior', clamp=True)
col2.image(Venue_Images[1], caption='Building', clamp=True)

st.write('## How to get here:')
st.write(':performing_arts: Adress: West St, London WC2H 9NZ')
st.write(':round_pushpin: Tube Station: Leicester Square')
st.write(':railway_car: from AirB&B  via lines: Jubilee & Picadilly (23 min) or Jubilee & Central (26 min)')
st.write(':walking: 0.2 km, about 4 min')


st.write('#### Find it on maps:')
st.image(Venue_Images[2], caption='Location', clamp=True)
