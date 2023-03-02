#import libraries
import os
import openai
import streamlit as st

#set key
openai.api_key=st.secrets["api_key"]
#secrets.toml

#input text
st.header("laymanizer using openai and streamlit")
article_text= st.text_area("enter text to laymanize")

#get text
if len(article_text)>100 :
  if st.button("generate summary"):
    #gpt stuff
    response=openai.Completion.create(
    engine="text-davinci-003",
    prompt="Explain the sentence below as if they had basic knowledge of the field, please  change any scientific or confusing terms to high school terms:"+ article_text,
    max_tokens=516,
    temperature=0.1,
    )

#print summary
    res=response["choices"]["0"]["text"]
    st.info(res)

#check if there are enough words in the text that was read
else:
    st.warning("make sure your sentence is at least 100 characters!")

#if enough,show
