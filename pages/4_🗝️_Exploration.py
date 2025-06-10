import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Exploration Guide",
    page_icon="🗝️",
)

st.title("🗝️ Exploration Guide")
st.write("Stealing loot from the rich... or is it?")

st.divider()
st.header("What is Exploration?")
st.markdown("""
Exploration in EVE is a relatively safe activity that involves scanning down cosmic signatures, finding data and relic sites.. It is a great way to make ISK, however very luck dependent.""")

st.subheader("What do I need to explore and stay safe?")
st.markdown("""All you need is a scanning ship fitted with data/relic analyser. T1, T2 and Faction exploration frigates are recommended. When scanning, cloaks are your best friend, allowing you to scan from safety, hidden from prying eyes. If you cannot fit a cloak, make sure to have a safe BM in space""")

st.error("**Note:** Just because you haven't seen anyone doesn't mean you are safe while hacking. Pay attention to your overview, you have less than 6 seconds to react to a hostile player entering the site")

st.divider()

fit_option = st.radio(
    "Select fit type to display:",
    ("Alpha", "Omega", "Alpha & Omega"),
    horizontal=True
)

if fit_option == "Alpha" or fit_option == "Alpha & Omega":
    with st.expander("Hacking Heron (Alpha)"):
        st.write("As an alpha pilot, you can either fly the T1 exploration frigates or the Astero. This Heron fit will suit any caldari alpha pilots")
        st.caption("Alpha Hacking Heron - 12M ISK")
        st.code("""
            [Heron, Δ Hacking Heron]
            Type-D Restrained Inertial Stabilizers
            Warp Core Stabilizer I

            5MN Y-T8 Compact Microwarpdrive
            Data Analyzer I
            Relic Analyzer I
            Scan Rangefinding Array I
            Scan Rangefinding Array I

            Core Probe Launcher I

            Small Memetic Algorithm Bank II
            Small Signal Focusing Kit I

            Sisters Core Scanner Probe x8
        """, language="markdown")
    with st.expander("Imicus (Alpha)"):
        st.write("As an alpha pilot, you can either fly the T1 exploration frigates or the Astero. This Imicus fit will suit any Gallente alpha pilots")
        st.caption("Alpha Hacking Imicus - 12M ISK")
        st.code("""
                [Imicus, Δ Hacking Imicus]
                Inertial Stabilizers II
                Inertial Stabilizers II
                Warp Core Stabilizer I

                5MN Quad LiF Restrained Microwarpdrive
                Scan Rangefinding Array I
                Data Analyzer I
                Relic Analyzer I

                [Empty High slot]
                Core Probe Launcher I

                Small Gravity Capacitor Upgrade I
                Small Gravity Capacitor Upgrade I
            """, language="markdown")
    with st.expander("Magnate (Alpha)"):
        st.write("As an alpha pilot, you can either fly the T1 exploration frigates or the Astero. This Magnate fit will suit any Amarr alpha pilots")
        st.caption("Alpha Hacking Magnate - 12M ISK")
        st.code("""
                [Magnate, Δ Hacking Magnate]
                Type-D Restrained Inertial Stabilizers
                Type-D Restrained Inertial Stabilizers
                Type-D Restrained Nanofiber Structure
                Warp Core Stabilizer I

                5MN Quad LiF Restrained Microwarpdrive
                Relic Analyzer I
                Data Analyzer I

                Core Probe Launcher I

                Small Gravity Capacitor Upgrade I
                Small Gravity Capacitor Upgrade I

                Sisters Core Scanner Probe x8
            """, language="markdown")
    with st.expander("Probe (Alpha)"):
        st.write("As an alpha pilot, you can either fly the T1 exploration frigates or the Astero. This Probe fit will suit any Amarr alpha pilots")
        st.caption("Alpha Hacking Probe - 12M ISK")
        st.code("""
                [Probe, Δ Hacking Probe]
                Type-D Restrained Inertial Stabilizers
                Type-D Restrained Inertial Stabilizers
                Warp Core Stabilizer I

                5MN Quad LiF Restrained Microwarpdrive
                Data Analyzer I
                Relic Analyzer I
                Scan Rangefinding Array I

                [Empty High slot]
                Core Probe Launcher I

                Small Gravity Capacitor Upgrade I
                Small Gravity Capacitor Upgrade I

                Sisters Core Scanner Probe x8
            """, language="markdown")
    with st.expander("Astero (Alpha)"):
        st.write("As an alpha pilot, you can either fly the T1 exploration frigates or the Astero. This Astero fit will suit any alpha pilots who want to use a faction ship")
        st.caption("Alpha Hacking Astero - 120M ISK")
        st.code("""
            [Astero, Δ Hacking Astero]
            Damage Control II
            Warp Core Stabilizer I
            Inertial Stabilizers II
            Inertial Stabilizers II

            1MN Monopropellant Enduring Afterburner
            Data Analyzer I
            Relic Analyzer I
            Scan Rangefinding Array I

            [Empty High slot]
            Core Probe Launcher I

            Small Gravity Capacitor Upgrade I
            Small Explosive Armor Reinforcer I
            Small Trimark Armor Pump I

            Sisters Core Scanner Probe x8
        """, language="markdown")
elif fit_option == "Omega" or fit_option == "Alpha & Omega":
    with st.expander("Buzzard (Omega)"):
        st.write("As an omega pilot, you can fly the T2 exploration frigates.")
        st.caption("Omega Hacking Buzzard - 90M ISK")
        st.code("""
            [Buzzard, Δ Hacking Buzzard]
            Inertial Stabilizers II
            Inertial Stabilizers II
            Warp Core Stabilizer II

            Relic Analyzer I
            Cargo Scanner I
            Data Analyzer I
            Sensor Booster II
            5MN Y-T8 Compact Microwarpdrive

            Sisters Core Probe Launcher
            Interdiction Nullifier II
            Covert Ops Cloaking Device II

            Small Ancillary Current Router II
            Small Ancillary Current Router I

            Sisters Core Scanner Probe x16
            Targeting Range Script x1
            Scan Resolution Script x1
        """, language="markdown")
    with st.expander("Anathema (Omega)"):
        st.write("As an omega pilot, you can fly the T2 exploration frigates.")
        st.caption("Omega Hacking Anathema - 90M ISK")
        st.code("""
            [Anathema,  Δ Hacking Anathema]
            Inertial Stabilizers II
            Inertial Stabilizers II
            Warp Core Stabilizer II
            Inertial Stabilizers II

            Data Analyzer I
            Relic Analyzer I
            Cargo Scanner I
            5MN Microwarpdrive I

            Sisters Core Probe Launcher
            Covert Ops Cloaking Device II
            Interdiction Nullifier II

            Small Gravity Capacitor Upgrade I
            Small Gravity Capacitor Upgrade I

            Sisters Core Scanner Probe x16
        """, language="markdown")
    with st.expander("Helios (Omega)"):
        st.write("As an omega pilot, you can fly the T2 exploration frigates.")
        st.caption("Omega Hacking Helios - 90M ISK")
        st.code("""
            [Helios,  Δ Hacking Helios]
            Inertial Stabilizers II
            Inertial Stabilizers II
            Warp Core Stabilizer II

            Data Analyzer I
            Relic Analyzer I
            Cargo Scanner I
            5MN Microwarpdrive I
            Sensor Booster II

            Interdiction Nullifier II
            Covert Ops Cloaking Device II
            Sisters Core Probe Launcher

            Small Gravity Capacitor Upgrade I
            Small Gravity Capacitor Upgrade I

            Sisters Core Scanner Probe x16
            Targeting Range Script x1
            Scan Resolution Script x1
        """, language="markdown")
    with st.expander("Cheetah (Omega)"):
        st.write("As an omega pilot, you can fly the T2 exploration frigates.")
        st.caption("Omega Hacking Cheetah - 90M ISK")
        st.code("""
            [Cheetah, Δ Hacking Cheetah]
            Warp Core Stabilizer II
            Inertial Stabilizers II
            Inertial Stabilizers II
            Inertial Stabilizers II

            Data Analyzer I
            Relic Analyzer I
            5MN Y-T8 Compact Microwarpdrive
            Cargo Scanner I

            Interdiction Nullifier II
            Sisters Core Probe Launcher
            Covert Ops Cloaking Device II

            Small Gravity Capacitor Upgrade I
            Small Ancillary Current Router II

            Sisters Core Scanner Probe x16
        """, language="markdown")
    with st.expander("Astero (Omega)"):
        st.write("As an omega pilot, you can fly the T2 exploration frigates. This Astero fit will suit any omega pilots who want to use a faction ship")
        st.caption("Omega Hacking Astero - 160M ISK")
        st.code("""
            [Astero, Δ Hacking Astero]
            Warp Core Stabilizer II
            Inertial Stabilizers II
            Inertial Stabilizers II
            Inertial Stabilizers II

            5MN Microwarpdrive I
            Data Analyzer I
            Relic Analyzer I
            Scan Rangefinding Array I

            Covert Ops Cloaking Device II
            Sisters Core Probe Launcher

            Small Hyperspatial Velocity Optimizer II
            Small Hyperspatial Velocity Optimizer II
            Small Hyperspatial Velocity Optimizer II

            Sisters Core Scanner Probe x16
        """, language="markdown")
st.divider()
st.header("What sites are safe?")
st.markdown("""The only safe data and relic sites are available in Class 1, 2, 3 wormholes. Sites containing faction names are safe to hack, while <Unsecured> and <Forgotten> sites are not.""")

st.subheader("Data sites")
data_sites = [
    {
        "Data site name": "Central <Faction> Sparking Transmitter",
        "Safe": "Yes",
        "Scanning Difficulty": "I",
        "Comm Tower": "1",
        "Mainframe": "3",
        "Databank": "1"
    },
    {
        "Data site name": "Central <Faction> Survey Site",
        "Safe": "Yes",
        "Scanning Difficulty": "I",
        "Comm Tower": "2",
        "Mainframe": "2",
        "Databank": "2"
    },
    {
        "Data site name": "Central <Faction> Command Center",
        "Safe": "Yes",
        "Scanning Difficulty": "III",
        "Comm Tower": "1",
        "Mainframe": "2",
        "Databank": "3"
    },
    {
        "Data site name": "Central <Faction> Data Mining Site",
        "Safe": "Yes",
        "Scanning Difficulty": "III / IV",
        "Comm Tower": "1",
        "Mainframe": "2",
        "Databank": "4"
    }
]

df = pd.DataFrame(data_sites)
st.dataframe(df, hide_index=True)

st.subheader("Relic sites")
relic_sites = [
    {
        "Relic site name": "Ruined (Faction) Monument Site",
        "Safe": "Yes",
        "Scanning Difficulty": "I",
        "Rubble": "2",
        "Remains": "3",
        "Ruins": "1"
    },
    {
        "Relic site name": "Ruined (Faction) Temple Site",
        "Safe": "Yes",
        "Scanning Difficulty": "II",
        "Rubble": "1",
        "Remains": "3",
        "Ruins": "2"
    },
    {
        "Relic site name": "Ruined (Faction) Science Outpost",
        "Safe": "Yes",
        "Scanning Difficulty": "III",
        "Rubble": "-",
        "Remains": "4",
        "Ruins": "2"
    },
    {
        "Relic site name": "Ruined (Faction) Crystal Quarry",
        "Safe": "Yes",
        "Scanning Difficulty": "III / IV",
        "Rubble": "1",
        "Remains": "3",
        "Ruins": "3"
    }
]

df_relic = pd.DataFrame(relic_sites)
st.dataframe(df_relic, hide_index=True)

st.info("**Note:** You will come across ghost sites with the names <Superior>. Newer players are not recommended to tackle these sites as they are on a timer and will kill all frigates.")

st.divider()
st.header("How do I hack the cans?")
st.markdown("""Hacking is a mini-game that is similar to mine-sweeper. You have to navigate through the grid, avoiding virus nodes to find the system core.""")
st.subheader("Nodes are:")
st.markdown("-- Orange: Explored node")
st.markdown("-- Green: Adjacent to Explored node")
st.markdown("-- Grey: Unexplored node")
st.info(""" Clicking on a node will reveal its contents, if it is empty, it will turn orange and display a number briefly between 1 and 5, indicating the distance to the nearest node with a virus, utility or data cache.""")
st.image("hacking.png", caption="Hacking example", use_container_width=True)

st.subheader("System Core")
st.write("Finding and disabling the system core is the goal of hacking. Each system core, virus and you have Coherence(Health) and Strength(Attack power). You fail a hack if your coherence reaches 0, or closing the hacking window for reasons such as moving too far away.")
st.info("You can fail two hacks before the can explodes, however dealing no damage.")
st.image("system_cores.png", caption="System cores table", use_container_width=True)

st.subheader("Defensive Subsystems")
st.write("Defensive subsystems prevent you from exploring adjacent nodes until they are disabled.")
st.image("defensive_subsystems.png", caption="Defensive subsystems table", use_container_width=True)

st.subheader("Utility Subsystems")
st.write("Utility subsystems provide you with buffs, such as increasing your coherence or block incoming attack.")
st.image("utility_subsystems.png", caption="Utility subsystems table", use_container_width=True)