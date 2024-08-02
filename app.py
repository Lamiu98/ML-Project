import streamlit as st
import pandas as pd
import numpy as np
import time



st.title("Excel File Reader, Hoang Lam")
st.header("Test")
st.subheader("_Prototype v0.4.sad1_sad")
st.markdown("_Prototype v0.4.sad1_sad")
st.code("import streamlit: 2+1=3")

st.button("Submit",type="primary")
st.button("Clear",type="secondary")
a="1"
ten=st.text_input("Nhap ten cua ban")

st.write(ten+" " + a)

file=st.file_uploader("Upload file")
if file is None:
    st.write("Upload your file")
else:
    st.write(file.size)
    st.write(file.name)
    st.download_button("Download file",data=file,file_name=file.name)
    df = pd.read_excel(file)
    columns= df.columns.tolist()
    st.dataframe(df)
    header=st.selectbox("Select column",columns)

    st.dataframe(df[header])

    if pd.api.types.is_numeric_dtype(df[header]):
        sumcol=df[header].sum()
        st.write(sumcol)
    else:
        st.write('Can not sum')
slide=st.slider("Select",1,200)  
st.progress(value=slide)

st.sidebar.title("Menu")
sidebar_selectbox = st.sidebar.selectbox(
    "Chọn một tùy chọn",
    ("Tùy chọn 1", "Tùy chọn 2", "Tùy chọn 3")
)

st.info("Information")

st.markdown("[Nhấn vào đây để mở URL](https://onedrive.live.com/?cid=7A5A68FA60C27F21&id=7A5A68FA60C27F21%2126387&parId=7A5A68FA60C27F21%2126233&o=OneUp)")