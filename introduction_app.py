import streamlit as st
import datetime as dt

#creating the title of the app 
st.header("INTRODUCTION APP")
st.markdown("CREATED BY SIDDHARTH CHILLAPWAR")
st.markdown("----")


#TAKING NAME FROM THE USER 
name = st.text_input("**ENTER YOUR NAME**")
if name:
    st.markdown(f"**HELLO {name.upper()} , NICE TO MEET YOU! :)**")

else:
    pass

#ASKING USER FOR SELF INTRODUCTION 
detail = st.text_area(f"TELL ME SOMETHING ABOUT YOUR SELF {name.upper()}")

if detail:
    st.subheader(f" IT WAS NICE KNOWING YOU {name.upper()}!!")
    st.image("leaving image.jpg")
    

else:
    pass

#asking the user for review

radio_btn = st.radio("**NEED YOUR HONEST OPINIOIN- HOW WAS THE APP**",options = ("NO OPINIONS","GOOD","MODERATE","BAD"))

if radio_btn=="GOOD":
    st.image("thank.jpg")
elif radio_btn=="MODERATE":
    st.image("moderate choice.jpg")
elif radio_btn=="BAD":
    st.image("shocked reaction.jpg")
else:
    pass


#adding the handels of the creator
st.markdown("[INSTAGRAM HANDLE](https://www.instagram.com/_siddharth2006_/)")
st.markdown("MAKE SURE TO FOLLOW!")

