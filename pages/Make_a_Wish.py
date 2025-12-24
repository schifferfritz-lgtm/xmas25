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
    'colour' : "yellow",
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
if 'selected_musical_final' not in st.session_state:
    st.session_state["selected_musical_final"] = None
if 'selected_date' not in st.session_state:
    st.session_state["selected_date"] = None
if 'selected_time' not in st.session_state:
    st.session_state["selected_time"] = None
if 'previous_example_index' not in st.session_state:
    st.session_state["previous_example_index"] = 0
if 'wish_used' not in st.session_state:
    st.session_state["wish_used"] = False

info_expander = st.expander("How to make a wish?")
explanation = f"""
<style>
.badge {{ display:inline-block; border-radius:12px; color:#fff; padding:6px 10px; margin-right:8px; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial; }}
.badge-hello {{ font-size:11px; width:670px; height: 100px; font-weight:600}}
.green {{ background: #2c715d; }}
.red {{ background: #5d001e; }}
.yellow {{ background: #c48a04; }}
.blue {{ background: #4c5b6a; }}
</style>
<div>
    <span class="badge badge-hello gray"> Buon Natale, mio piccolo pesciolino!\
    <br />Even if I don`t see you today here is your present, perfectly on time.\
    <br />You already guessed what I wanted to give you, but I hope this is still a surprise.\
    <br />Just click on an image and select a day and time and then click on "Make a Wish".\
    <br />Ti amo. </span> 
</div>
"""
info_expander.markdown(explanation, unsafe_allow_html=True)
info_expander.write('')

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
.badge-sel {{ font-size:24px; width:670px; height: 50px; font-weight:700}}
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
.yellow {{ background: #c48a04; }}
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


made_a_wish = st.form(key="form_settings")
expander = made_a_wish.expander('view your selection')
col1, col2, col3, col4 = expander.columns([1,1,1,1])
selected_show = f"""
<style>
.badge-view {{ font-size:12px; width:150px; height: 90px; font-weight:400}}
</style>
<div>
    <span class="badge badge-view {musicals[st.session_state['selected_musical']]['colour']}"> 🔖 Selected Show: <br />{st.session_state['selected_musical']} </span>
</div>
"""
col1.markdown(selected_show, unsafe_allow_html=True)
col1.write('')
runtime = f"""
<div>
    <span class="badge badge-view {musicals[st.session_state['selected_musical']]['colour']}"> ⌛ Run Time: <br />{musicals[st.session_state['selected_musical']]['Run Time']} </span>
</div>
"""
col2.markdown(runtime, unsafe_allow_html=True)
col2.write('')
sel_date = f"""
<div>
    <span class="badge badge-view {musicals[st.session_state['selected_musical']]['colour']}"> 📅 Selected Date: <br />{event_date} </span>
</div>
"""
col3.markdown(sel_date, unsafe_allow_html=True)
col3.write('')
sel_date = f"""
<div>
    <span class="badge badge-view {musicals[st.session_state['selected_musical']]['colour']}"> ⏰ Selected Time: <br />{event_time} </span>
</div>
"""
col4.markdown(sel_date, unsafe_allow_html=True)
col4.write('')
made_a_wish.write('')
made_a_wish.write(f'Please confirm your choices and make a wish.')
confirm = made_a_wish.checkbox("confirm choices")
selected_show = f"""
<style>
.gray {{ background: #6b7280; }}
.badge-confirm {{ font-size:9px; width:600px; height: 30px; font-weight:400}}
</style>
<div>
    <span class="badge badge-confirm gray"> *by selecting "confirm choices" I also confirm that I do <b>not</b> belong to the naughty list and am eligable for a christmas gift.  </span>
</div>
"""
made_a_wish.markdown(selected_show, unsafe_allow_html=True)
st.write('')
security = made_a_wish.text_input("Security Check", "What is the name of the person or animal you love the most?")
st.write('')
message = made_a_wish.text_input("Your message to Santa Clause", "Enter here an optional message...")
made_a_wish.write('')

wished = made_a_wish.form_submit_button(label="Make a Wish", disabled=st.session_state["wish_used"])

if wished:
  if not st.session_state["wish_used"]:
    if not confirm:
      st.write('   Please confirm your choices by checking the box.')
    else:
      if event_time is None:
        st.write('   Please select a time.')
      elif security.lower() == 'joshua':
        st.write('... nice try, but I know it is not me.')
      elif security.lower() == 'shelley':
        st.session_state["wish_used"] = True
        st.session_state["selected_musical_final"] = st.session_state["selected_musical"]
        st.session_state["selected_date"] = event_date
        st.session_state["selected_time"] = event_time
        st.write('   Merry Christmas!')
      else:
         st.write('   Security question was not answered correctly.')

if st.session_state["wish_used"]:
  selected_show = f"""
  <style>
  .badge-wish {{ font-size:11px; width:670px; height: 100px; font-weight:600}}
  </style>
  <div>
      <span class="badge badge-wish {musicals[st.session_state['selected_musical_final']]['colour']}"> Santa recieved your wish already. <br />
                                            Mark the {st.session_state["selected_date"]} at {st.session_state["selected_time"]} as busy in your calander. <br />
                                            We are going to {st.session_state["selected_musical_final"]}! <br />
                                            Merry Christmas!
                                            </span>
  </div>
  """
  st.markdown(selected_show, unsafe_allow_html=True)
