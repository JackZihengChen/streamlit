import streamlit as st
import pandas as pd
import numpy as np

for i in range(5):
  st.write("Here's our first attempt at using data to create a table:")

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)
