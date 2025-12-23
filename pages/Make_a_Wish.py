import datetime
import streamlit as st
from streamlit_image_select import image_select

musicals = {
  "Wicked": {
    'Venue' : "Apollo Victoria Theatre",
    'Dates' : [datetime.datetime(2026, 2, 13, 19, 30),datetime.datetime(2026, 2, 14, 14, 30),datetime.datetime(2026, 2, 14, 19, 30),datetime.datetime(2026, 2, 15, 14, 30),],
    'Run Time' : "2hr 45min.",
    'images' : ["data/Wicked.webp","data/apollo_victoria_map.png"],
    'colour' : "green",
    'description' : "Wicked tells the untold story of Elphaba, the Wicked Witch of the West, and Glinda the Good Witch in one unforgettable show.\
                     Prepare to be amazed by the technical wizardry, dazzling costumes, show-stopping songs, and witty nods to L. Frank Baum’s The Wizard of Oz.\
                     Even though it's one of the longest-running London musicals, Wicked continues redefining modern musical theatre for an entire generation, challenging our preconceptions of good and evil.",
  },
  "Moulin Rouge": {
    'Venue' : "Piccadilly Theatre",
    'Dates' : [datetime.datetime(2026, 2, 13, 19, 30),datetime.datetime(2026, 2, 14, 14, 30),datetime.datetime(2026, 2, 14, 19, 30),datetime.datetime(2026, 2, 15, 14, 30),],
    'Run Time' : "2hr 45min.",
    'images' : ["data/MoulinRouge.webp",'data/picadilly_map.png'],
    'colour' : "red",
    'description' : "Set in the Montmartre Quarter in Paris, Moulin Rouge! The Musical is a luxurious, indulgent musical.\
                     As a lovesick writer named Christian takes his seat inside the Moulin Rouge, he's greeted by Satine.\
                     With a dazzling smile and an inviting manner, their lives epically collide as they grow closer together in an extravagant world where anything goes."
  },
  "Hamilton": {
    'Venue' : "Victoria Palace Theatre",
    'Dates' : [datetime.datetime(2026, 2, 13, 19, 30),datetime.datetime(2026, 2, 14, 14, 30),datetime.datetime(2026, 2, 14, 19, 30),],
    'Run Time' : "2hr 45min.",
    'images' : ["data/Hamilton.webp",'data/victoria_palace_map.png'],
    'colour' : "gold",
    'description' : "Orphaned at a young age, Hamilton moved to New York in the hope of a better life.\
                     While there, there he impressed those around him with his hunger for revolution and reform.\
                     The story sees Hamilton become George Washington's right-hand man, fall in love, and go on to become the first Secretary of the Treasury of the United States.",
  },
  "Mousetrap": {
    'Venue' : "St. Martin’s Theatre",
    'Dates' : [datetime.datetime(2026, 2, 13, 19, 30),datetime.datetime(2026, 2, 14, 15, 00),datetime.datetime(2026, 2, 14, 19, 30),],
    'Run Time' : "2hr 00min.",
    'images' : ["data/mousetrap.webp",'data/st_martin_map.png'],
    'colour' : "blue",
    'description' : "The Mousetrap play follows a group of people gathered in a remote part of the countryside as they discover, to their horror, that there is a murderer in their midst.\
                     Who can it be? One by one, suspicious characters reveal their sordid pasts until, at the last nerve-shredding moment, the play finally unveils the identity and the motive.\
                     An irresistible treat for amateur sleuths everywhere!",
  },
}

st.markdown("# Merry X-mas 2025!")

if 'selected_musical' not in st.session_state:
    st.session_state["selected_musical"] = 'Wicked'
if 'previous_example_index' not in st.session_state:
    st.session_state["previous_example_index"] = 0

info_expander = st.expander("How to make a wish?")

index_selected = image_select(
    "",
    images=[musical['images'][0] for musical in musicals.values()],
    captions=list(musicals.keys()),
    index=0,
    return_value="index",
    use_container_width=False,
)
if index_selected != st.session_state["previous_example_index"]:
    st.session_state["previous_example_index"] = index_selected
    st.session_state["selected_musical"] = list(musicals.keys())[index_selected]

selection = f"""
<style>
.badge {{ display:inline-block; border-radius:12px; color:#fff; padding:6px 10px; margin-right:8px; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial; }}
.badge-sel {{ font-size:24px; width:670px; height: 50px; font-weight:700}}
.green {{ background: #2c715d; }}
.red {{ background: #5d001e; }}
.gold {{ background: #c48a04; }}
.blue {{ background: #4c5b6a; }}
</style>
<div>
    <span class="badge badge-sel {musicals[st.session_state['selected_musical']]['colour']}"> {st.session_state['selected_musical']} </span>
</div>
"""
st.markdown(selection, unsafe_allow_html=True)

html_description = f"""
<style>
.badge {{ display:inline-block; border-radius:12px; color:#fff; padding:6px 10px; margin-right:8px; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial; }}
.badge-des {{ font-size:12px; width:670px; height: 120px; font-weight:400}}
.green {{ background: #2c715d; }}
.red {{ background: #5d001e; }}
.gold {{ background: #c48a04; }}
.blue {{ background: #4c5b6a; }}
</style>
<div>
    <span class="badge badge-des {musicals[st.session_state['selected_musical']]['colour']}"> {musicals[st.session_state['selected_musical']]['description']}</span>
</div>
"""
st.write('')
st.markdown(html_description, unsafe_allow_html=True)
st.write('')
st.metric(":round_pushpin: Venue", musicals[st.session_state['selected_musical']]['Venue'])

col1, col2 = st.columns([1,1])
col1.image(musicals[st.session_state['selected_musical']]['images'][1], caption='Location', clamp=True)
event_date = col2.date_input(
    "Schedule your event",
    musicals[st.session_state['selected_musical']]['Dates'][0],
    min_value=musicals[st.session_state['selected_musical']]['Dates'][0],
    max_value=musicals[st.session_state['selected_musical']]['Dates'][-1]
)
event_time = col2.selectbox(
    "Time",
    options=["%s:%s" % (dates.hour, str(dates.minute).zfill(2)) for dates in musicals[st.session_state['selected_musical']]['Dates'] if dates.date() == event_date],
    index=None,
    placeholder='select time',
    #on_change=event_date,
)

expander = st.expander('view your selection')
col1, col2 = st.columns([1,1])
col1.badge(f"Selected Show: {st.session_state['selected_musical']}", icon=":material/star:", color=musicals[st.session_state['selected_musical']]['colour'])
col2.badge(f"Runtime: {musicals[st.session_state['selected_musical']]['Run Time']}", icon=":material/hourglass:", color=musicals[st.session_state['selected_musical']]['colour'])
col1.badge(f"Selected Date: {event_date}", icon=":material/calender_check:", color=musicals[st.session_state['selected_musical']]['colour'])
col2.badge(f"Selected Time: {event_time}", icon=":material/alarm_on:", color=musicals[st.session_state['selected_musical']]['colour'])
expander.write(f'Please confirm your choices and make a wish.')
