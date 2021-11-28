import streamlit as st
import pandas as pd

data = {'Series 1': [1, 3, 4, 5, 7],
        'Series 2': [10, 30, 40, 100, 250]}

df  = pd.DataFrame(data)
st.title("Our First Streamlit App")
st.subheader("Introducing Strimlit in Automate Everything With Python")
st.write("This is our first web app. Enjoy!!")
st.write(df)
st.line_chart(df)
st.area_chart(df)