
import streamlit as st
from pathlib import Path

st.markdown("# Victoria Palace Theatre")

path = Path(__file__).parent / "../data"
Venue_Images =  [f'{path}/victoria_palace_indoor.jpg',
                 f'{path}/victoria_palace_outdoor.jpg',
                 f'{path}/victoria_palace_map.png']


col1, col2 = st.columns([1,1])
col1.image(Venue_Images[0], caption='Interior', clamp=True)
col2.image(Venue_Images[1], caption='Building', clamp=True)

st.write('## How to get here:')
st.write(':performing_arts: Adress: 126 Victoria St, London SW1E 5LA')
st.write(':round_pushpin: Tube Station: Victoria Station')
st.write(':railway_car: from AirB&B  via lines: Jubilee & Victoria (20 min)')
st.write(':walking: 0.1 km, about 3 min')


st.write('#### Find it on maps:')
st.image(Venue_Images[2], caption='Location', clamp=True)
