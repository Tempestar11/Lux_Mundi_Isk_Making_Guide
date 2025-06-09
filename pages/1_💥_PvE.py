import streamlit as st

st.set_page_config(
    page_title="PvE guide",
    page_icon="💥",
)

st.title("💥 Wormhole PvE guide")
st.write("You want to go pew pew? This is the place to start!")

st.divider()
st.subheader("What is PvE in Wormholes?")
st.write("This is some of the best money in the game. You are essentially completing waves of NPCs for dropped loot, which goes into building T3Cs or sold to NPC stations for a fixed price. DP is a C2 wormhole, with HS and C3 static connections. We will be focusing on C2 and C3 combat sites as they are more accessible while maintaining a good income.")
st.subheader("Ship progression")
st.write("Fits are ordered by skill points and investment required to fly them. The more SP you have, the more expensive your ship can be, and the more damage you can do. The fits are designed to be used in C2 and C3 sites, with some being Omega only due to skill requirements.")
st.write("""The recommended progression for a fresh character is as follows: \n
        Drake -> Gila -> Praxis -> Tengu -> Maurader
         """)
fit_option = st.radio(
    "Select fit type to display:",
    ("Alpha", "Omega", "Alpha & Omega"),
    horizontal=True
)

if fit_option == "Alpha" or fit_option == "Alpha & Omega":
    with st.expander("C2 Passive Tanked Drake"):
        st.write("This is the first ship you will be able to fly, it is a passive tanked Drake with light missiles. The passive tank allows you to run the site without needing to manage your capacitor or worry about neut pressure, and the light missiles are a good choice for the DPS you can output.")
        st.caption("Alpha C2 Passive Drake - 150M ISK")
        st.code("""
            [Drake, C2 Passive Drake]
            Imperial Navy Drone Damage Amplifier
            Imperial Navy Drone Damage Amplifier
            Imperial Navy Drone Damage Amplifier
            Imperial Navy Drone Damage Amplifier
            Large Shield Extender II
            Large Shield Extender II
            Large Shield Extender II
            Large Shield Extender II
            Rapid Light Missile Launcher II
            Rapid Light Missile Launcher II
            Rapid Light Missile Launcher II
            Rapid Light Missile Launcher II
            Medium EM Shield Reinforcer II
            Medium Capacitor Control Circuit II
            Medium Capacitor Control Circuit II
            Hornet EC-300 x3
            Inferno Fury Light Missile x1000
            Nova Fury Light Missile x1000
            Scourge Fury Light Missile x1000
        """, language="markdown")
    
    with st.expander("C2 Active Tanked Drake"):
        st.caption("C2 Active Drake")
        st.code("""
            [Drake, C2 Active Drake]
            Imperial Navy Drone Damage Amplifier
            Imperial Navy Drone Damage Amplifier
            Imperial Navy Drone Damage Amplifier
            Large Shield Extender II
            Large Shield Extender II
            Large Shield Extender II
            Large Shield Extender II
            Rapid Light Missile Launcher II
            Rapid Light Missile Launcher II
            Rapid Light Missile Launcher II
            Rapid Light Missile Launcher II
            Medium EM Shield Reinforcer II
            Medium Capacitor Control Circuit II
            Medium Capacitor Control Circuit II
            Hornet EC-300 x3
            Inferno Fury Light Missile x1000
            Nova Fury Light Missile x1000
            Scourge Fury Light Missile x1000
        """, language="markdown")

if fit_option == "Omega" or fit_option == "Alpha & Omega":
    # Add code to display Omega fits here
    with st.expander("C2 Passive Tanked Drake (Omega)"):
        st.caption("C2 Passive Drake (Omega)")
        st.code("""
            [Drake, C2 Passive Drake (Omega)]
            Imperial Navy Drone Damage Amplifier
            Imperial Navy Drone Damage Amplifier
            Imperial Navy Drone Damage Amplifier
            Large Shield Extender II
            Large Shield Extender II
            Large Shield Extender II
            Large Shield Extender II
            Rapid Light Missile Launcher II
            Rapid Light Missile Launcher II
            Rapid Light Missile Launcher II
            Rapid Light Missile Launcher II
            Medium EM Shield Reinforcer II
            Medium Capacitor Control Circuit II
            Medium Capacitor Control Circuit II
            Hornet EC-300 x3
            Inferno Fury Light Missile x1000
            Nova Fury Light Missile x1000
            Scourge Fury Light Missile x1000
        """, language="markdown")
    with st.expander("C3 Tengu"):
        st.caption("C3 Tengu")
        st.code("""
            [Tengu, C3 Tengu]
            Imperial Navy Drone Damage Amplifier
            Imperial Navy Drone Damage Amplifier
            Imperial Navy Drone Damage Amplifier
            Large Shield Extender II
            Large Shield Extender II
            Large Shield Extender II
            Large Shield Extender II
            Rapid Light Missile Launcher II
            Rapid Light Missile Launcher II
            Rapid Light Missile Launcher II
            Rapid Light Missile Launcher II
            Medium EM Shield Reinforcer II
            Medium Capacitor Control Circuit II
            Medium Capacitor Control Circuit II
            Hornet EC-300 x3
            Inferno Fury Light Missile x1000
            Nova Fury Light Missile x1000
            Scourge Fury Light Missile x1000
        """, language="markdown")