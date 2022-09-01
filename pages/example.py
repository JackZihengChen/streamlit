import streamlit as st
import pandas as pd
import numpy as np
import time
from datetime import datetime


"### Data frame highlight max"
dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))

st.dataframe(dataframe.style.highlight_max(axis=0))


"### Data frame"
dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))
st.table(dataframe)


"### Line chart"
chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])
st.line_chart(chart_data)


"### Map"
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])
st.map(map_data)


"### Slider"
x = st.slider('x')  # 👈 this is a widget
st.write(x, 'squared is', x * x)


"### Input field and access"
st.text_input("Your name", key="name")
st.session_state.name


"### Checkbox and showing data"
if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])
    chart_data


"### Drop down selection and access" 
df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
    })
option = st.selectbox(
    'Which number do you like best?',
     df['first column'])
'You selected: ', option


st.sidebar.write("#### Add a selectbox to the sidebar:")
add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)


st.sidebar.write("#### Add a slider to the sidebar:")
add_slider = st.sidebar.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0)
)


"### Adding columns"
left_column, mid_column, right_column = st.columns(3)
# You can use a column just like st.sidebar:
left_column.write("#### Left column")
left_column.button('Press me!')

# Or even better, call Streamlit functions inside a "with" block:
right_column.write("#### Right column")
with right_column:
    chosen = st.radio(
        'Sorting hat',
        ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
    st.write(f"You are in {chosen} house!")






"### Messing with auto update"

my_bar = st.progress(0)

st.button('*UPDATE*')

while True:
     day_of_week = datetime.today().weekday()
     now = datetime.now()

     if day_of_week == 3:
          start_time = datetime(now.year,now.month,now.day,13,00)
          end_time = datetime(now.year,now.month,now.day,17,00)
     elif day_of_week == 1 or day_of_week == 2:
          start_time = datetime(now.year,now.month,now.day,8,00)
          end_time = datetime(now.year,now.month,now.day,16,00)
     duration = (now - start_time).total_seconds()
     total = (end_time - start_time).total_seconds()

     start_time = None
     end_time = None
     # st.write("Current Time is ", now.strftime("%H:%M:%S"))

     time.sleep(0.1)
     
     percent_complete =  (duration/total)*100
     my_bar.progress(int(percent_complete) % 100)

# while True:
#      now = datetime.now()
#      current_time = now.strftime("%H:%M:%S")
#      st.write("Current Time =", current_time)

# chart_data = pd.DataFrame(
#      np.random.randn(20, 3),
#      columns=['a', 'b', 'c'])

# st.line_chart(chart_data)

# 'Starting a long computation...'

# # Add a placeholder
# my_bar = st.progress(0)
# percent_complete =  0

# while True:
#      time.sleep(0.1)
#      percent_complete += 1
#      my_bar.progress((percent_complete + 1) % 100)
# 'Does this get printed??'
