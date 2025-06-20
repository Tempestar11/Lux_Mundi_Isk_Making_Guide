import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="PvE guide",
    page_icon="💥",
    layout="wide",
)

st.title("💥 Wormhole PvE guide")
st.write("You want to go pew pew? This is the place to start!")

st.divider()
st.subheader("What is PvE in Wormholes?")
st.write("This is some of the best money in the game. You are essentially completing waves of NPCs for dropped loot, which goes into building T3Cs or sold to NPC stations for a fixed price. DP is a C2 wormhole, with HS and C3 static connections. We will be focusing on C2 and C3 combat sites as they are more accessible while maintaining a good income.")
st.subheader("Ship progression")
st.write("Fits are ordered by clear time(isk/hr). The more SP you have, the more expensive your ship can be, and the more damage you can do. The fits are designed to be used in C2 and C3 sites, with some being Omega only due to skill requirements.")
st.write("""The recommended progression for a fresh character is as follows: \n
        Drake(C2) -> Gila(C2/C3) -> Praxis(C3) -> Tengu(C3) -> Maurader(C3+)
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
    with st.expander("C3 Vagabond"):
        st.caption("C3 Vagabond")
        st.code("""
            [Vagabond, Vagabond C3 PVE]
            Assault Damage Control II
            Gyrostabilizer II
            Gyrostabilizer II
            Capacitor Flux Coil II
            Reactor Control Unit II

            Dread Guristas Large Shield Booster
            Republic Fleet Large Cap Battery
            Multispectrum Shield Hardener II
            10MN Afterburner II

            425mm AutoCannon II
            425mm AutoCannon II
            425mm AutoCannon II
            425mm AutoCannon II
            425mm AutoCannon II
            Core Probe Launcher II

            Medium Core Defense Operational Solidifier II
            Medium Semiconductor Memory Cell II
                
            Hobgoblin II x5

            Barrage M x3500
            Hail M x5100
            Sisters Core Scanner Probe x8
        """, language="markdown")

st.divider()
st.header("Site layout and spawns")

class_option = st.pills(
    "Select fit type to display:",
    ("C2", "C3", "C4", "C5"),
    label_visibility="collapsed")

if class_option == "C2":
    st.caption("Combat sites")
    with st.expander("Perimeter Checkpoint"):
        st.image('combat_sites/C2/1_perimeter_checkpoint.png', caption="Perimeter Checkpoint")
    with st.expander("Perimeter Hangar"):
        st.image('combat_sites/C2/2_perimeter_hangar.png', caption="Perimeter Hangar")
    with st.expander("Sleeper Data Signature Sanctuary"):
        st.image('combat_sites/C2/3_sleeper_data_signature_sanctuary.png', caption="Sleeper Data Signature Sanctuary")
    with st.expander("The Ruins of Enclave Cohort 27"):
        st.image('combat_sites/C2/4_the_ruins_of_enclave_cohort_27.png', caption="The Ruins of Enclave Cohort 27")
    st.caption("Relic sites")
    with st.expander("Forgotten Perimeter Gateway"):
        st.image('combat_sites/C2/5_forgotten_perimeter_gateway.png', caption="Forgotten Perimeter Gateway")
    with st.expander("Forgotten Perimeter Habitation Coils"):
        st.image('combat_sites/C2/6_forgotten_perimeter_habitation_coils.png', caption="Forgotten Perimeter Habitation Coils")
    st.caption("Data sites")
    with st.expander("Unsecured Perimeter Comms Relay"):
        st.image('combat_sites/C2/7_unsecured_perimeter_comms_relay.png', caption="Unsecured Perimeter Comms Relay")
    with st.expander("Unsecured Perimeter Transponder Farm"):
        st.image('combat_sites/C2/8_unsecured_perimeter_transponder_farm.png', caption="Unsecured Perimeter Transponder Farm")

elif class_option == "C3":
    st.caption("Combat sites")
    with st.expander("Fortification Frontier Stronghold"):
        st.image('combat_sites/C3/1_fortification_frontier_stronghold.png', caption="Fortification Frontier Stronghold")
    with st.expander("Outpost Frontier Stronghold"):
        st.image('combat_sites/C3/2_outpost_frontier_stronghold_2.png', caption="Outpost Frontier Stronghold")
    with st.expander("Solar Cell"):
        st.image('combat_sites/C3/3_solar_cell.png', caption="Solar Cell")
    with st.expander("The Oruze Construct"):
        st.image('combat_sites/C3/4_the_oruze_construct.png', caption="The Oruze Construct")
    st.caption("Relic sites")
    with st.expander("Forgotten Frontier Quarantine Outpost"):
        st.image('combat_sites/C3/5_forgotten_frontier_quarantine_outpost.png', caption="Forgotten Frontier Quarantine Outpost")  
    with st.expander("Forgotten Frontier Recursive Depot"):
        st.image('combat_sites/C3/6_forgotten_frontier_recursive_depot.png', caption="Forgotten Frontier Recursive Depot")
    st.caption("Data sites")
    with st.expander("Unsecured Frontier Database"):
        st.image('combat_sites/C3/7_unsecured_frontier_database.png', caption="Unsecured Frontier Database")
    with st.expander("Unsecured Frontier Reciever"):
        st.image('combat_sites/C3/8_unsecured_frontier_receiver.png', caption="Unsecured Frontier Receiver")

elif class_option == "C4":
    st.caption("Combat sites")
    with st.expander("Frontier Barracks"):
        st.image('combat_sites/C4/1_frontier_barracks.png', caption="Frontier Barracks")
    with st.expander("Frontier Command Post"):
        st.image('combat_sites/C4/2_frontier_command_post.png', caption="Frontier Command Post")
    with st.expander("Integrated Terminus"):
        st.image('combat_sites/C4/3_integrated_terminus.png', caption="Integrated Terminus")
    with st.expander("Sleeper Information Sanctum"):
        st.image('combat_sites/C4/4_sleeper_information_sanctum.png', caption="Sleeper Information Sanctum")
    st.caption("Relic sites")
    with st.expander("Forgotten Frontier Conversion Module"):
        st.image('combat_sites/C4/5_forgotten_frontier_conversion_module.png', caption="Forgotten Frontier Conversion Module")
    with st.expander("Forgotten Frontier Evacuation Center"):
        st.image('combat_sites/C4/6_forgotten_frontier_evacuation_center.png', caption="Forgotten Frontier Evacuation Center")
    st.caption("Data sites")
    with st.expander("Unsecured Frontier Digital Nexus"):
        st.image('combat_sites/C4/7_unsecured_frontier_digital_nexus.png', caption="Unsecured Frontier Digital Nexus")
    with st.expander("Unsecured Frontier Trinary Hub"):
        st.image('combat_sites/C4/8_unsecured_frontier_trinary_hub.png', caption="Unsecured Frontier Trinary Hub")

elif class_option == "C5":
    st.caption("Combat sites")
    with st.expander("Core Garrison"):
        st.image("combat_sites/C5/1_core_garrison.png", caption="Core Garrison")
    with st.expander("Core Stronghold"):
        st.image("combat_sites/C5/2_core_stronghold.png", caption="Core Stronghold")
    with st.expander("Oruze Osobnyk"):
        st.image("combat_sites/C5/3_oruze_osobnyk.png", caption="Oruze Osobnyk")
    with st.expander("Quarantine Area"):
        st.image("combat_sites/C5/4_quarantine_area.png", caption="Quarantine Area")
    st.caption("Relic sites")
    with st.expander("Forgotten Core Data Field"):
        st.image("combat_sites/C5/5_forgotten_core_data_field.png", caption="Forgotten Core Data Field")
    with st.expander("Forgotten Core Information Pen"):
        st.image("combat_sites/C5/6_forgotten_core_information_pen.png", caption="Forgotten Core Information Pen")
    st.caption("Data sites")
    with st.expander("Unsecured Frontier Enclave Relay"):
        st.image("combat_sites/C5/7_unsecured_frontier_enclave_relay.png", caption="Unsecured Frontier Enclave Relay")
    with st.expander("Unsecured Frontier Server Bank"):
        st.image("combat_sites/C5/8_unsecured_frontier_server_bank.png", caption="Unsecured Frontier Server Bank")