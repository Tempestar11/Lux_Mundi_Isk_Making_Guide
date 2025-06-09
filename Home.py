import streamlit as st

st.set_page_config(
    page_title="LUX Homepage",
    page_icon="👋",
    layout="wide",
)

st.title("Welcome to LUX Mundi Exploration Company! 👋")
st.write("Your NEW home! What next?")
st.caption("This document is written and updated for the current activiies of all corp members, so that you may join in on the fun and know what to expect. If you have any questions, please ask in our internal chat channel **The Explorers Club** or on Discord.")

st.divider()

st.header("📞 Communications")
col1, col2 = st.columns(2)
col1.markdown("""
**Ingame**
""")
col2.markdown("""
**Discord**
""")

col3, col4 = st.columns(2)
col3.success("""We use an internal chat channel **The Explorers Club** for every day in-game communication, please join this via corp MOTD.""")
col4.success("""We have a Discord server for out-of-game communication, please join via the link below:
[Join our Discord](https://discord.gg/your-discord-link)""")

st.divider()
st.header("📦 Moving-in")

col5, col6 = st.columns(2)
col5.markdown("""
**Bookmarks**
""")
col6.markdown("""
**Pathfinder**
""")

col7, col8 = st.columns(2)
col7.info("""To find our wormhole HQ you need access to our corporation bookmarks folder via corp MOTD:""")
col8.info("""We use the tool **Pathfinder** to map our way around J-space. If you are unsure how to use Pathfinder, please ask and we will be happy to help (there are also guides in Discord).  
          
Pathfinder will show you our current connections to High sec and where you can enter our home (The Dog Pound AKA J231837).
[Open Pathfinder](http://map.battlestar.space/map/MjM0Mw%3D%3D#)""")

st.caption("Once you reached the current HS system, Look for '0 DP' for the entrance bookmark. This is easiest if you scroll to the top of your locations window and expand the 'Location in system' folder")

st.divider()

st.header("🚀 Ship Naming Convention")

st.markdown("""
When naming your ship, please add the delta symbol at the beginning of your ship name, this is for ease of identifying friendlies on D-Scan""")

st.code("Δ   << Copy paste me", language="markdown")

st.divider()

st.header("🧳 Moving in and what to bring")

st.markdown("""
The most important ship to bring is a **scanning frigate**, followed by something to make ISK with (e.g., gas huffing, sleeper ratting, or exploration).
""")

col9, col10, col11, col12, col13 = st.columns(5)

col9.markdown("""
<br>
<a href="PvE" target="_self">
    <button style="
        background-color: #ffcc00;
        color: #222;
        padding: 1em 2em;
        font-size: 1em;
        font-weight: bold;
        border: none;
        border-radius: 12px;
        cursor: pointer;
        transition: background 0.3s;
    " onmouseover="this.style.backgroundColor='#ffe066';" onmouseout="this.style.backgroundColor='#ffcc00';">
        💥 PvE Guide
    </button>
</a>
""", unsafe_allow_html=True)

col10.markdown("""
<br>
<a href="Mining" target="_self">
    <button style="
        background-color: #ffcc00;
        color: #222;
        padding: 1em 2em;
        font-size: 1em;
        font-weight: bold;
        border: none;
        border-radius: 12px;
        cursor: pointer;
        transition: background 0.3s;
    " onmouseover="this.style.backgroundColor='#ffe066';" onmouseout="this.style.backgroundColor='#ffcc00';">
        ⛏️ Mining Guide
    </button>
</a>
""", unsafe_allow_html=True)

col11.markdown("""
<br>
<a href="Gas_Huffing" target="_self">
    <button style="
        background-color: #ffcc00;
        color: #222;
        padding: 1em 2em;
        font-size: 1em;
        font-weight: bold;
        border: none;
        border-radius: 12px;
        cursor: pointer;
        transition: background 0.3s;
    " onmouseover="this.style.backgroundColor='#ffe066';" onmouseout="this.style.backgroundColor='#ffcc00';">
        💨 Huffing Guide
    </button>
</a>
""", unsafe_allow_html=True)

col12.markdown("""
<br>
<a href="Exploration" target="_self">
    <button style="
        background-color: #ffcc00;
        color: #222;
        padding: 1em 2em;
        font-size: 1em;
        font-weight: bold;
        border: none;
        border-radius: 12px;
        cursor: pointer;
        transition: background 0.3s;
    " onmouseover="this.style.backgroundColor='#ffe066';" onmouseout="this.style.backgroundColor='#ffcc00';">
        🗝️ Exploration Guide
    </button>
</a>
""", unsafe_allow_html=True)

col13.markdown("""
<br>
<div style="margin-left: 1.5em;">
<a href="PvP" target="_self">
    <button style="
        background-color: #ffcc00;
        color: #222;
        padding: 1em 2em;
        font-size: 1em;
        font-weight: bold;
        border: none;
        border-radius: 12px;
        cursor: pointer;
        transition: background 0.3s;
    " onmouseover="this.style.backgroundColor='#ffe066';" onmouseout="this.style.backgroundColor='#ffcc00';">
        ☠️ PvP Guide
    </button>
</a>
</div>
""", unsafe_allow_html=True)

st.divider()

st.header("💰Buy Back Program")
st.subheader("""Lux offers a buyback program for any items at **90% Jita Buy**.""")
st.markdown("""Janice is used as our selected appraisal tool, please include a link to the Janice appraisal in your buyback request.""")
st.caption("More information can be found in the **rules-and-guides** channel on Discord.")
st.markdown("""[rules-and-guides](https://discord.com/channels/691295139162882079/1131422099999830208)""")
st.markdown("""[Janice Appraisal Tool](https://janice.app)""")