#import libraries
import os
import openai
import streamlit as st

#set key
openai.api_key=st.secrets["api_key"]
#secrets.toml

#input text
st.header("Laymanizer using OpenAI and Streamlit")
article_text= st.text_area("Enter text to Laymanize")

#get text
if len(article_text)>100 :
  if st.button("Generate summary"):
    #gpt stuff
    response=openai.Completion.create(
    engine="text-davinci-002",
    prompt="Explain the sentence below to someone who has a high school level knowledge of the field,change any scientific or confusing terms simpler terms:"+ article_text,
    max_tokens=516,
    temperature=0.1,
    )
    

#print summary
    res = response["choices"][0]["text"].strip()
    st.success(res)

#check if there are enough words in the text that was read
else:
    st.warning("Make sure your sentence is at least 100 characters!")

#if enough,show
