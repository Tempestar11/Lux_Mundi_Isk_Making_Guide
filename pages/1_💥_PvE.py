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
    with st.expander("C2 Passive Drake (Starter)"):
        st.write("This is the first ship you will be able to fly, it is a passive tanked Drake with light missiles. The passive tank allows you to run the site without needing to manage your capacitor or worry about neut pressure, and the light missiles are a good choice for the DPS you can output.")
        st.caption("Alpha C2 Passive Drake - 70M ISK")
        st.code("""
            [Drake, C2 Passive Drake]
            Shield Power Relay II
            Power Diagnostic System I
            Ballistic Control System II
            Ballistic Control System II

            Large Shield Extender II
            Large Shield Extender II
            Multispectrum Shield Hardener II
            10MN Monopropellant Enduring Afterburner
            EM Shield Amplifier II
            Large Shield Extender II

            Upgraded 'Malkuth' Heavy Assault Missile Launcher I
            Upgraded 'Malkuth' Heavy Assault Missile Launcher I
            Upgraded 'Malkuth' Heavy Assault Missile Launcher I
            Upgraded 'Malkuth' Heavy Assault Missile Launcher I
            Upgraded 'Malkuth' Heavy Assault Missile Launcher I
            Upgraded 'Malkuth' Heavy Assault Missile Launcher I
            Core Probe Launcher I

            Medium Core Defense Field Purger II
            Medium Core Defense Field Purger II
            Medium Core Defense Field Purger II

            Hobgoblin I x5

            Caldari Navy Scourge Heavy Assault Missile x936
        """, language="markdown")
    
    with st.expander("C2 Active Tanked Gnosis (Starter)"):
        st.caption("C2 Active Tanked Gnosis")
        st.code("""
            [Gnosis, C2 Gnosis]
            Ballistic Control System II
            Capacitor Power Relay II
            Capacitor Power Relay II
            Capacitor Power Relay II
            Capacitor Power Relay II
            IFFA Compact Damage Control

            10MN Monopropellant Enduring Afterburner
            Multispectrum Shield Hardener II
            Compact Multispectrum Shield Hardener
            Large Compact Pb-Acid Cap Battery
            Copasetic Compact Shield Boost Amplifier
            X-Large C5-L Compact Shield Booster

            Shield Command Burst I
            Prototype 'Arbalest' Heavy Assault Missile Launcher I
            Prototype 'Arbalest' Heavy Assault Missile Launcher I
            Prototype 'Arbalest' Heavy Assault Missile Launcher I
            Prototype 'Arbalest' Heavy Assault Missile Launcher I
            Prototype 'Arbalest' Heavy Assault Missile Launcher I

            Medium Core Defense Capacitor Safeguard I
            Medium Processor Overclocking Unit I
            Medium Processor Overclocking Unit I

            Hobgoblin I x5
            Hammerhead I x5

            Caldari Navy Mjolnir Heavy Assault Missile x300
            Shield Harmonizing Charge x300
        """, language="markdown")
    
    with st.expander("C3 Praxis"):
        st.caption("C3 Praxis - 415M ISK")
        st.code("""
            [Praxis, C3 Praxis]
            Drone Damage Amplifier II
            Co-Processor I
            Ballistic Control System II
            Capacitor Flux Coil II
            Capacitor Flux Coil II
            Capacitor Flux Coil II
            Capacitor Flux Coil II

            Dread Guristas X-Large Shield Booster
            Compact Multispectrum Shield Hardener
            Compact Multispectrum Shield Hardener
            Compact Multispectrum Shield Hardener
            Copasetic Compact Shield Boost Amplifier
            Copasetic Compact Shield Boost Amplifier
            Copasetic Compact Shield Boost Amplifier

            Rapid Heavy Missile Launcher II
            Rapid Heavy Missile Launcher II
            Rapid Heavy Missile Launcher II
            Rapid Heavy Missile Launcher II
            Rapid Heavy Missile Launcher II
            Rapid Heavy Missile Launcher II
            Drone Link Augmentor I

            Large Capacitor Control Circuit II
            Large Capacitor Control Circuit II
            Large Capacitor Control Circuit I

            Caldari Navy Hornet x10
            Caldari Navy Vespa x10

            Inferno Precision Heavy Missile x600
            Inferno Fury Heavy Missile x750
        """, language="markdown")

if fit_option == "Omega" or fit_option == "Alpha & Omega":
    with st.expander("C3 Tengu (Fort only)"):
        st.caption("C3 Tengu (Fort only) - 550M ISK")
        st.code("""
            [Tengu, C3 Tengu (Fort only)]
            Ballistic Control System II
            Ballistic Control System II
            Ballistic Control System II

            Republic Fleet Large Cap Battery
            Multispectrum Shield Hardener II
            Copasetic Compact Shield Boost Amplifier
            Dread Guristas EM Shield Hardener
            10MN Afterburner I
            Dread Guristas Large Shield Booster
            Target Painter II

            Heavy Assault Missile Launcher II
            Heavy Assault Missile Launcher II
            Heavy Assault Missile Launcher II
            Heavy Assault Missile Launcher II
            Heavy Assault Missile Launcher II
            Heavy Assault Missile Launcher II

            Medium Ancillary Current Router I
            Medium EM Shield Reinforcer II
            Medium Capacitor Control Circuit II

            Tengu Core - Augmented Graviton Reactor
            Tengu Defensive - Amplification Node
            Tengu Offensive - Accelerated Ejection Bay
            Tengu Propulsion - Fuel Catalyst
                
            Nanite Repair Paste x200
            Scourge Javelin Heavy Assault Missile x396
            Scourge Rage Heavy Assault Missile x792
        """, language="plaintext")

    with st.expander("C3 Gila"):
        st.caption("C3 Gila - 420M ISK")
        st.code("""
            [Gila, C3 Gila]
            Shield Power Relay II
            Shield Power Relay II
            Drone Damage Amplifier II

            Large Shield Extender II
            Large Shield Extender II
            Caldari Navy Large Shield Extender
            Caldari Navy Large Shield Extender
            Pithum C-Type EM Shield Amplifier
            Pithum C-Type Thermal Shield Amplifier

            Rapid Light Missile Launcher II
            Rapid Light Missile Launcher II
            Rapid Light Missile Launcher II
            Rapid Light Missile Launcher II
            Drone Link Augmentor I

            Medium Core Defense Field Purger II
            Medium Core Defense Field Purger II
            Medium Core Defense Field Purger II

            Caldari Navy Hornet x4
            Imperial Navy Infiltrator x2
            Caldari Navy Vespa x2
            Federation Navy Hammerhead x2
            Republic Fleet Valkyrie x2

            Caldari Navy Scourge Light Missile x480
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
        st.image('combat_sites/C2/1_Perimeter_Checkpoint_Layout.jpg')
        st.image('combat_sites/C2/1_perimeter_checkpoint.png', caption="Perimeter Checkpoint")
    with st.expander("Perimeter Hangar"):
        st.image('combat_sites/C2/2_Perimeter_Hangar_Layout.jpg')
        st.image('combat_sites/C2/2_perimeter_hangar.png', caption="Perimeter Hangar")
    with st.expander("Sleeper Data Signature Sanctuary"):
        st.image('combat_sites/C2/3_Sleeper_Data_Signature_Sanctuary_Layout.jpg')
        st.image('combat_sites/C2/3_sleeper_data_signature_sanctuary.png', caption="Sleeper Data Signature Sanctuary")
    with st.expander("The Ruins of Enclave Cohort 27"):
        st.image('combat_sites/C2/4_The_Ruins_Of_Enclave_Cohort_27_Layout.jpg')
        st.image('combat_sites/C2/4_the_ruins_of_enclave_cohort_27.png', caption="The Ruins of Enclave Cohort 27")
    st.caption("Relic sites")
    with st.expander("Forgotten Perimeter Gateway"):
        st.image('combat_sites/C2/5_Forgotten_Perimeter_Gateway_Layout.jpg')
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