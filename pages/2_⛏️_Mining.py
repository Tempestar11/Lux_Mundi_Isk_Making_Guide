import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Mining guide",
    page_icon="⛏️",
)

st.title("⛏️ Wormhole Mining guide")
st.write("If you think this is just some nice AFK isk, dont. You're better off huffing")

st.divider()
st.subheader("Why should I mine ores?")
st.write("Mining in EVE was never a great way to make isk, espeically trying to plex your account. It is more of a side activity to supplement your industry production chain, building up margins to your product. **BUT** remember, just because mined it doesn't mean its free.")
st.subheader("What ores and minerals can I mine?")
st.write(
    """
    Being in a wormhole, you have access to a large variety of **rare minerals** not available in highsec.
    In addition, through our static connections, you can mine highsec ores as well.

    The **only minerals you cannot obtain** are:
    - Lowsec/Nullsec mineral: `Noxcium`
    - Nullsec mineral: `Morphite`
    """
)
st.write("""
        In addition to the ore belts, we also have a moon drill setup in our home system, which allows us to mine **R4** moons every friday. R4 moons are the least valuable in EVE, but they still yield a good amount of minerals and are a great way to get them when no ore belts are available.
         """)

st.success("We regularly do boosted mining fleets, please look out for announcements or ask in our internal chat channel **The Explorers Club** or on Discord.")
st.info("If you would like to get started in manufacturing but don't know where to start, please ask in chat or discord for some BPCs from your fellow corpmates, we have a large library of blueprints available.")

st.divider()

belt_choice = st.selectbox("Select an ore belt",("Ordinary Perimeter Deposit", "Common Perimeter Deposit", "Unexceptional Frontier Deposit", "Uncommon Core Deposit", "Average Frontier Deposit"))

if belt_choice == "Ordinary Perimeter Deposit":
    ore_data = {
        "Ore Type": ["Arkonor", "Bistot", "Gneiss", "Kernite", "Omber", "Pyroxeres"],
        "Quantity (m3)": ["160,000", "320,000", "100,000", "240,000", "120,000", "486,000"],
        "Units" : ["10,000", "20,000", "20,000", "200,000", "200,000", "1,620,000"],
        # "Jita Price (ISK/m3)": ["5,428", "5,528", "3,165", "850", "376", "43"],
    }

    df = pd.DataFrame(ore_data)

    st.subheader("Ordinary Perimeter Deposit Ore Table")
    st.dataframe(df, hide_index=True)

if belt_choice == "Common Perimeter Deposit":
    ore_data = {
        "Ore Type": ["Arkonor", "Bistot", "Gneiss", "Kernite", "Omber", "Pyroxeres"],
        "Quantity (m3)": ["320,000", "480,000", "220,000", "360,000", "180,000", "156,000"],
        "Units" : ["20,000", "30,000", "40,000", "300,000", "300,000", "520,000"],
        # "Jita Price (ISK/m3)": ["5,428", "5,528", "3,165", "850", "376", "43"],
    }

    df = pd.DataFrame(ore_data)

    st.subheader("Common Perimeter Deposit Ore Table")
    st.dataframe(df, hide_index=True)

if belt_choice == "Unexceptional Frontier Deposit":
    ore_data = {
        "Ore Type": ["Arkonor", "Bistot", "Gneiss", "Kernite", "Omber"],
        "Quantity (m3)": ["480,000", "800,000", "300,000", "480,000", "240,000"],
        "Units" : ["30,000", "50,000", "60,000", "400,000", "400,000"],
        # "Jita Price (ISK/m3)": ["5,428", "5,528", "3,165", "850", "376"],
    }

    df = pd.DataFrame(ore_data)

    st.subheader("Unexceptional Frontier Deposit Ore Table")
    st.dataframe(df, hide_index=True)

if belt_choice == "Uncommon Core Deposit":
    ore_data = {
        "Ore Type": ["Arkonor", "Bistot", "Gneiss", "Kernite", "Omber", "Pyroxeres"],
        "Quantity (m3)": ["640,000", "960,000", "350,000", "708,000", "360,000", "150,000"],
        "Units" : ["40,000", "60,000", "70,000", "590,000", "600,000", "500,000"],
        # "Jita Price (ISK/m3)": ["5,428", "5,528", "3,165", "850", "376"],
    }

    df = pd.DataFrame(ore_data)

    st.subheader("Uncommon Core Deposit Ore Table")
    st.dataframe(df, hide_index=True)

if belt_choice == "Average Frontier Deposit":
    ore_data = {
        "Ore Type": ["Arkonor", "Bistot", "Gneiss", "Kernite", "Omber", "Pyroxeres"],
        "Quantity (m3)": ["480,000", "640,000", "2,250,000", "360,000", "180,000", "210,000"],
        "Units" : ["30,000", "40,000", "450,000", "300,000", "300,000", "700,000"],
        # "Jita Price (ISK/m3)": ["5,428", "5,528", "3,165", "850", "376"],
    }

    df = pd.DataFrame(ore_data)

    st.subheader("Average Frontier Deposit Ore Table")
    st.dataframe(df, hide_index=True)