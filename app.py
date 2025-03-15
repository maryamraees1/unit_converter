import streamlit as st
import random #for random emoji in result
st.title("UNIT CONVERTER   o(≧▽≦)o ")
# category select box
unit_category=st.selectbox("# Select Unit",["Length","Time","Weight"])

#  function to convert 
def convert_values(unit_category,value,unit):
    if unit_category=="Length":
        if unit=="meters to inches":  
            return value *39.37,"inches"
        elif unit=="inches to meters":
            return value / 39.37 , "meters" , "You can divide the value by 39.37"

    elif unit_category=="Time":
        if unit=="hours to mins": 
            return value * 60 , "mins"
        elif unit=="mins to hours":
            return value / 60 , "hours"

    elif unit_category=="Weight":
        if unit=="kg to pounds": 
            return value *  2.20462 ,"pounds"
        elif unit=="pounds to kg":
            return value /  2.20462 , "kg"

    return "Invalid Conversion"

    #unit slect box---parametr
if unit_category=="Length":
    unit=st.selectbox("📐 Select Unit" ,["meters to inches","inches to meters"])
elif unit_category=="Time":
    unit=st.selectbox("⌚ Select Unit" ,["hours to mins","mins to hours"])
elif unit_category=="Weight":
    unit=st.selectbox("⚖️ Select Unit" ,["kg to pounds","pounds to kg"])

#value--parameter
value=st.number_input("Enter value :")
# emoji list
emojis=["😒","🤷‍♂️","🙄","😶‍🌫️","🫠","🙃","🫤","😕","😔","😭","🥴","😵‍💫","🤡","🥸","🧐","👽","😺","🦒","🫎","🐳","🐟","🦈","🪸","🐦‍🔥","🐌","🧞","🤺","🧗‍♂️","🚵","🎀","🪡","🔐"]
# cpnvert button
if st.button("Convert"):
    result ,units = convert_values(unit_category,value,unit)
    random_emoji = random.choice(emojis)
    st.success(f"it's {result} {units} {random_emoji}. ")

