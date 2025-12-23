import datetime
import streamlit as st
from streamlit_image_select import image_select

st.set_page_config(
    page_title="xmas2025", page_icon="🖼️",layout='centered'
)

make_a_wish = st.Page("pages/Make_a_Wish.py", title="Make a Wish", icon=":material/dashboard:",default=True)
apollo_victoria = st.Page("pages/apollo_victoria.py", title="Apollo Victoria", icon=":performing_arts:")
picadilly_theatre = st.Page("pages/Picadilly_Theatre.py", title="Picadilly Theatre", icon=":performing_arts:")
st_martins = st.Page("pages/st_martins.py", title="St. Martin’s Theatre", icon=":performing_arts:")
pg = st.navigation(
    {
        "Your Present" : [make_a_wish],
        "Venues": [apollo_victoria,picadilly_theatre,st_martins],
    }
)
pg.run()
