import streamlit as st
import pandas as pd
import numpy as np

st.title("My First Streamlit App")  
#st.write("This is a simple Streamlit app to demonstrate its features.")
#

st.write("Hello Saransh.")
st.text("Let's learn Streamlit together!")

name=st.text_input("Enter your name:")
if st.button("SUBMIT!"):
    st.success(f"Hello, {name}! Welcome to Streamlit!")

#Creating Charts using Pandas & Numpy
df=pd.DataFrame(np.random.randn(10,2),columns=['Column 1','Column 2'])

st.line_chart(df)
st.bar_chart(df)

#SideBar ,  Image and Video
st.sidebar.title("Navigation")
st.image("https://www.digitaltrends.com/tachyon/2024/08/samsung-galaxy-buds-3-pro-review-00018.jpeg?fit=2500%2C1667")
st.video("https://www.youtube.com/watch?v=rfscVS0vtbw")


upload_csv=st.file_uploader("Upload a csv file",type='csv')

if upload_csv:
    df=pd.read_csv(upload_csv)
    st.dataframe(df)

st.header("This is a Headder")
st.subheader("This is a subheader")
st.markdown("**Bold**, *Italic*, 'Code' [Link](http://streamlit.io)")
st.code("for i in range(5): print(i)", language="python")

st.text_input("What's your nanme?")
st.text_area("Write something....")
st.number_input("pick a number",min_value=0,max_value=1000)
st.slider("Choose arange",0,100)
st.selectbox("select a fruit",["Apple","Banana","Mango"])
st.multiselect("Choose toppings",["Cheese","Tomato","Olives"])
st.radio("Pick one", ["Option A","Option B"])
st.checkbox("I agree the items.")

import matplotlib.pyplot as plt
fig, ax=plt.subplots()
ax.plot([1,2,3],[1,4,9])
st.pyplot(fig)