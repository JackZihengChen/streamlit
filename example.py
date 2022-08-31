import streamlit as st
import pandas as pd
import numpy as np
import time

for i in range(5):
  st.write("Here's our first attempt at using data to create a table:")

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)

'Starting a long computation...'

# Add a placeholder
my_bar = st.progress(0)
percent_complete =  0

while True:
     time.sleep(0.1)
     my_bar.progress((percent_complete + 1) % 100)
'Does this get printed??'
