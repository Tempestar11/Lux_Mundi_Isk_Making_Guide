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
with st.expander("T1 Scoop Venture"):
    st.write("Cheap gas huffing venture with T1 scoops, slowest but cheapest option, about 1 hour of huffing to fill up hold")
    st.caption("T1 Venture - 10M ISK")
    st.code("""
        [Venture, T1 Venture]
        Mining Laser Upgrade I
        Mining Laser Upgrade I
        Mining Laser Upgrade I
        Gas Cloud Harvester I
        Gas Cloud Harvester I
        Gas Cloud Harvester I
        Medium EM Shield Reinforcer I
        Medium Capacitor Control Circuit I
        Medium Capacitor Control Circuit I
    """, language="markdown")
with st.expander("Faction Scoop Venture"):
    st.write("This is a very expensive ship with paper thin tank, but it has a faster gas cloud scoop and a higher yield. It is recommended for long-term use and for players who want to make the most out of gas huffing.")
    st.caption("Faction Venture - 50M ISK")
    st.code("""
        [Venture, Faction Venture]
        Mining Laser Upgrade II
        Mining Laser Upgrade II
        Mining Laser Upgrade II
        Syndicate Gas Cloud Harvester
        Syndicate Gas Cloud Harvester
        Syndicate Gas Cloud Harvester
        Medium EM Shield Reinforcer II
        Medium Capacitor Control Circuit II
        Medium Capacitor Control Circuit II
    """, language="markdown")
with st.expander("T2 Scoop Prospect"):
    st.write("This is the best ship for gas huffing, it has a T2 gas cloud scoop and a high yield. .")
    st.caption("T2 Prospect - 100M ISK")
    st.code("""
        [Prospect, T2 Prospect]
        Mining Laser Upgrade II
        Mining Laser Upgrade II
        Mining Laser Upgrade II
        Gas Cloud Harvester II
        Gas Cloud Harvester II
        Gas Cloud Harvester II
        Medium EM Shield Reinforcer II
        Medium Capacitor Control Circuit II
        Medium Capacitor Control Circuit II
    """, language="markdown")
with st.expander("Faction Scoop Prospect"):
    st.write("This is the best ship for gas huffing, it has a Faction gas cloud scoop and a high yield. It is recommended for players who want to make the most out of gas huffing and have the skills to fly it.")
    st.caption("Faction Prospect - 150M ISK")
    st.code("""
        [Prospect, Faction Prospect]
        Mining Laser Upgrade II
        Mining Laser Upgrade II
        Mining Laser Upgrade II
        Syndicate Gas Cloud Harvester
        Syndicate Gas Cloud Harvester
        Syndicate Gas Cloud Harvester
        Medium EM Shield Reinforcer II
        Medium Capacitor Control Circuit II
        Medium Capacitor Control Circuit II
    """, language="markdown")

st.divider()
st.header("Gas sites")
st.subheader("There are 9 types of gas sites available in wormholes")
st.write("The gas sites you need to look out for are Ordinary Perimeter Reservoir, they contain turrets that will kill any frigate in one shot. Other gas sites are not as dangerous, with rats spawning around 15 seconds after initial warpin.")