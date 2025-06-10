import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Gas Huffing Guide",
    page_icon="💨",
)

st.title("💨 Gas Huffing Guide")
st.markdown("""The most addictive drug in J-Space.""")

st.divider()
st.header("What is Gas Huffing?")
st.markdown("""Similar to ore mining, gas huffing is a method of extracting resources from gas clouds in wormholes. It is a VERY lucrative activity, with up to 200 million ISK per hour, depending on optimisations and skills.""")
st.subheader("What do I need to gas huff?")
st.markdown("""To gas huff, you need a mining frigate, we DO NOT recommend using any barges as that makes you an easy target. New players or alpha pilots are recommended to use a Venture, while Omega pilots can use a Prospect. You will also need a gas cloud scoop, which can be fitted to the ship.
            There are three types of scoops available: T1, T2 and Faction scoops (Synidcate Gas Cloud Scoop).""")
st.info("**Note:** We do not recommend fitting a T1 scoop if avoidable due to it being too slow at harvesting.")
st.markdown("""
            T2 scoops are the cheaper option out of the fast scoops, however they have a significant residue chance. Meanwhile faction scoops are the fastest with 0 residue but they are also the most expensive option.
            The choice of scoop depends on your budget and the amount of gas you plan to harvest. If you see yourself doing gas huffing sparingly and more, Faction scoops are your go to. Few good hauls of gas will pay for the scoop. 
""")

st.info("**Note:** New gas huffers should find an experienced corpmate to huff together as rat spawn times can be unpredictable and you may need help with the rats.")

st.divider()

st.info("**Note:** T1 and Faction scoops need minimal skill investment where as T2 scoops require level 4 Gas Harvesting skills.")
with st.expander("T1 Scoop Venture (Alpha)"):
    st.write("Cheap gas huffing venture with T1 scoops, slowest but cheapest option, about 1 hour of huffing to fill up hold")
    st.caption("T1 Venture - 15M ISK")
    st.code("""
        [Venture, Δ Gas Huffer T1]
        Type-D Restrained Inertial Stabilizers

        Medium Shield Extender I
        Compact EM Shield Amplifier
        5MN Y-T8 Compact Microwarpdrive

        Gas Cloud Scoop I
        Gas Cloud Scoop I
        Core Probe Launcher I

        Small Low Friction Nozzle Joints I
        Small Low Friction Nozzle Joints I
        Small Core Defense Field Extender I

        Sisters Core Scanner Probe x8

    """, language="markdown")
with st.expander("Faction Scoop Venture (Alpha)"):
    st.write("This is a very expensive ship with paper thin tank, but it has a faster gas cloud scoop and a higher yield. It is recommended for long-term use and for players who want to make the most out of gas huffing.")
    st.caption("Faction Venture - 250M ISK")
    st.code("""
        [Venture, Δ Gas Huffer Faction]
        Warp Core Stabilizer II

        Medium Shield Extender II
        EM Shield Amplifier II
        5MN Quad LiF Restrained Microwarpdrive

        Syndicate Gas Cloud Scoop
        Syndicate Gas Cloud Scoop
        Core Probe Launcher I

        Small Low Friction Nozzle Joints I
        Small Low Friction Nozzle Joints II
        Small Core Defense Field Extender I
            
        Sisters Core Scanner Probe x8

    """, language="markdown")
with st.expander("T2 Scoop Prospect (Omega)"):
    st.write("This gives you the best bang for your buck. Slightly slower, but a lot cheaper to lose.")
    st.caption("T2 Prospect - 70M ISK")
    st.code("""
        [Prospect, Δ Gas Huffer T2]
        Warp Core Stabilizer II
        Inertial Stabilizers II
        Inertial Stabilizers II
        Inertial Stabilizers II

        Medium Shield Extender I
        ML-3 Scoped Survey Scanner
        5MN Y-T8 Compact Microwarpdrive

        Gas Cloud Scoop II
        Gas Cloud Scoop II
        Covert Ops Cloaking Device II

        Small Core Defense Field Extender II
        Small Core Defense Field Extender II
            
        Core Scanner Probe I x8
        Core Probe Launcher I x1
        Mobile Depot x1

    """, language="markdown")
with st.expander("Faction Scoop Prospect (Omega)"):
    st.write("This is the best ship for gas huffing, it has a Faction gas cloud scoop and a high yield. It is recommended for players who want to make the most out of gas huffing and have the skills to fly it. You'll earn this fit back in 2-3 hours of huffing.")
    st.caption("Faction Prospect - 300M ISK")
    st.code("""
        [Prospect, Δ Gas Huffer Faction]
        Warp Core Stabilizer II
        Inertial Stabilizers II
        Inertial Stabilizers II
        Inertial Stabilizers II

        Medium Shield Extender II
        Survey Scanner I
        5MN Y-T8 Compact Microwarpdrive

        Syndicate Gas Cloud Scoop
        Syndicate Gas Cloud Scoop
        Covert Ops Cloaking Device II

        Small Core Defense Field Extender II
        Small Core Defense Field Extender II

        Core Scanner Probe I x8
        Core Probe Launcher I x1
        Mobile Depot x1

    """, language="markdown")

st.divider()
st.header("Gas sites")
st.subheader("There are 9 types of gas sites available in wormholes")
st.write("The gas sites you need to look out for are **Ordinary Perimeter Reservoir**, they contain turrets that will kill any frigate in one shot. Other gas sites are not as dangerous, with rats spawning around 15 minutes after initial warpin.")

site_choice = st.selectbox("Select a gas site", (
    "Barren Perimeter Reservoir",
    "Token Perimeter Reservoir",
    "Minor Perimeter Reservoir",
    "Ordinary Perimeter Reservoir",
    "Sizeable Perimeter Reservoir",
    "Bountiful Frontier Reservoir",
    "Vast Frontier Reservoir",
    "Vital Core Reservoir",
    "Instrumental Core Reservoir"
))

if site_choice == "Barren Perimeter Reservoir":
    st.caption("Barren Perimeter Reservoir - 1.5 Prospect loads")
    gas_data = {
        "Gas Type": ["C50", "C60"],
        "Quantity (m3)": ["12,000", "6,000"],
        "Units": ["12,000", "6,000"],
    }
    
    df = pd.DataFrame(gas_data)
    st.dataframe(df, hide_index=True)
elif site_choice == "Token Perimeter Reservoir":
        st.caption("Token Perimeter Reservoir - 1.5 Prospect loads")
        gas_data = {
            "Gas Type": ["C60", "C70"],
            "Quantity (m3)": ["12,000", "6,000"],
            "Units": ["12,000", "6,000"],
        }
        df = pd.DataFrame(gas_data)
        st.dataframe(df, hide_index=True)
elif site_choice == "Minor Perimeter Reservoir":
        st.caption("Minor Perimeter Reservoir - 1.5 Prospect loads")
        gas_data = {
            "Gas Type": ["C70", "C72"],
            "Quantity (m3)": ["12,000", "6,000"],
            "Units": ["12,000", "6,000"],
        }
        df = pd.DataFrame(gas_data)
        st.dataframe(df, hide_index=True)   
elif site_choice == "Ordinary Perimeter Reservoir":
        st.error("DO NOT warp if you are not sure the site is clear of turrets")
        st.caption("Ordinary Perimeter Reservoir - 1.5 Prospect loads")
        gas_data = {
            "Gas Type": ["C72", "C84"],
            "Quantity (m3)": ["12,000", "6,000"],
            "Units": ["12,000", "6,000"],
        }
        df = pd.DataFrame(gas_data)
        st.dataframe(df, hide_index=True)
elif site_choice == "Sizeable Perimeter Reservoir":
        st.caption("Sizeable Perimeter Reservoir - 3.5 Prospect loads")
        gas_data = {
            "Gas Type": ["C50", "C84"],
            "Quantity (m3)": ["6,000", "24,000"],
            "Units": ["6,000", "12,000"],
        }
        df = pd.DataFrame(gas_data)
        st.dataframe(df, hide_index=True)
elif site_choice == "Bountiful Perimeter Reservoir":
        st.caption("Sizeable Perimeter Reservoir - 5 Prospect loads")
        gas_data = {
            "Gas Type": ["C28", "C32"],
            "Quantity (m3)": ["40,000", "20,000"],
            "Units": ["20,000", "4,000"],
        }
        df = pd.DataFrame(gas_data)
        st.dataframe(df, hide_index=True)
elif site_choice == "Vast Perimeter Reservoir":
        st.caption("Sizeable Perimeter Reservoir - 9 Prospect loads")
        gas_data = {
            "Gas Type": ["C28", "C32"],
            "Quantity (m3)": ["8,000", "100,000"],
            "Units": ["4,000", "20,000"],
        }
        df = pd.DataFrame(gas_data)
        st.dataframe(df, hide_index=True)
elif site_choice == "Vital Core Reservoir":
        st.error("Found in C5 and above wormholes, these sites contain rats that are very dangerous. Make sure to have someone expereiced to huff with.")
        st.caption("Vital Core Reservoir - 20.8 Prospect loads")
        gas_data = {
            "Gas Type": ["C320", "C540"],
            "Quantity (m3)": ["10,000", "240,000"],
            "Units": ["2,000", "24,000"],
        }
        df = pd.DataFrame(gas_data)
        st.dataframe(df, hide_index=True)
elif site_choice == "Instrumental Core Reservoir":
        st.error("Found in C5 and above wormholes, these sites contain rats that are very dangerous. Make sure to have someone expereiced to huff with.")
        st.caption("Instrumental Core Reservoir - 20.8 Prospect loads")
        gas_data = {
            "Gas Type": ["C320", "C540"],
            "Quantity (m3)": ["120,000", "20,000"],
            "Units": ["24,000", "2,000"],
        }
        df = pd.DataFrame(gas_data)
        st.dataframe(df, hide_index=True)