#streamlit
import streamlit as st

st.set_page_config(page_title = "growth mindset project",project_icon="★")
st.title("Growth Mindset Challeng: Web App with Streamlit")

st.header(" Welcome To Your Growth Journey!")
st.write("Embrace challenges, learn from mistake, and unlolck your full lpotential. This AI-powered app help you build a growth mindset with reflection,challenges,and achievements!")

#quote section
st.header("Today's Growth Mindset Quote")
st.write("Success is not final, failure is not fatalL: it is courage to continue that count.-Winston Churchill")

st.header("What's Your Challenge Today?")
user_input = st.text_input ("Describe a challeng you're facing:")

#condition
if user_input:
    st.success(f"You re facing: {user_input}. Keep pushing forward towords your goal! ")
else:
    st.write("Tell us about your challenge to get started!")

#reflexing
st.header ("Reflect on Your Learning here:")
reflection = st.text_area("Write your reflection here: ")

if reflection:
    st.success(f"Great Insight! Your reflection :{reflection}")
else:
    st.ifo("Reflectig on past experience help you difficulties")


    #acheivements
    st.header("Celebrate Your Wins!")
    acyheivment =st. text_input("Share somethig you've recently accomplished:")

    if acyheivment:
        st.success(f"Amazing! You achieved:{acyheivment}")
    else:
        st.info("Big or small , every achievement count! Share one now")

        #footer
        st.write("- - -")
        st.write(" Keep believing in yourself. Growth is a journey, not a destination!" )
        st.write("**Created by Sanam Adeel**")