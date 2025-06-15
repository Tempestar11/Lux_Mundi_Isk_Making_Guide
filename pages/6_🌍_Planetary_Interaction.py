import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Planetary Interaction Guide",
    page_icon="🌍",
)

st.title("🌍 Planetary Interaction Guide")
st.markdown("""It's a love-hate relationship honestly.""")

st.divider()
st.header("Planetary Interaction Overview")
st.markdown("""
Planetary Interaction (PI) is a feature in EVE Online that allows players to establish colonies on planets and extract resources. It involves setting up structures, managing resources, and optimizing production chains. PI can be a lucrative activity, especially for players who invest time in understanding the mechanics and optimizing their operations.""")
st.write("There is too much to cover in this guide, so we will be linking a good playlist that covers everything you need to know about PI. Additionally, this page will store PI templates specifically for LUX and PI calculations")

st.video("https://www.youtube.com/watch?v=9lC-Cp8ymOY&list=PLXllDeIzDzd5t13rVjcTRpLxWEgzGVBmU")

st.divider()
st.header("PI Templates")

st.write('Even if you know nothing about PI, it is still worth setting up a basic extractor, this will provide you a steady passive income.')

st.info("These templates are made using command center level 4, as not everyone have command center level 5 ")

planet_choice = st.selectbox("Select a planet type to view templates:", ("Gas", "Ice", "Lava", "Oceanic"), index=None)

if planet_choice == "Gas":
    selection = st.pills("Gas Planet Templates", ["Water", "Reactive Metals", "Electrolytes", "Oxygen", "Oxidising Compound"])
    if selection == "Water":
        with st.expander("Water P0 extractor"):
            st.code("""[PH]""", language="plaintext")
            st.download_button(
                label="Download P0 Extractor",
                data="https://example.com/micro_organism_p0_extractor.pi",
                file_name="micro_organism_p0_extractor.pi",
                mime="application/octet-stream"
            )
        with st.expander("Water P1 Factory"):
            st.caption("Bacteria P1 Factory")
            st.code("""[PH]""", language="plaintext")
            st.download_button(
                label="Download P1 Factory",
                data="https://example.com/bacteria_p1_factory.pi",
                file_name="bacteria_p1_factory.pi",
                mime="application/octet-stream"
            )
        with st.expander("Water P1 Extractor + Factory"):
            st.caption("Bacteria P1 Extractor + Factory")
            st.code("""[PH]""", language="plaintext")
            st.download_button(
                label="Download P1 Extractor + Factory",
                data="https://example.com/bacteria_p1_factory.pi",
                file_name="bacteria_p1_factory.pi",
                mime="application/octet-stream"
            )
    elif selection == "Reactive Metals":
        with st.expander("Reactive Metals P0 extractor"):
            st.code("""[PH]""", language="plaintext")
            st.download_button(
                label="Download P0 Extractor",
                data="https://example.com/reactive_metals_p0_extractor.pi",
                file_name="reactive_metals_p0_extractor.pi",
                mime="application/octet-stream"
            )
        with st.expander("Reactive Metals P1 Factory"):
            st.caption("Reactive Metals P1 Factory")
            st.code("""[PH]""", language="plaintext")
            st.download_button(
                label="Download P1 Factory",
                data="https://example.com/reactive_metals_p1_factory.pi",
                file_name="reactive_metals_p1_factory.pi",
                mime="application/octet-stream"
            )
        with st.expander("Reactive Metals P1 Extractor + Factory"):
            st.caption("Reactive Metals P1 Extractor + Factory")
            st.code("""[PH]""", language="plaintext")
            st.download_button(
                label="Download P1 Extractor + Factory",
                data="https://example.com/reactive_metals_p1_factory.pi",
                file_name="reactive_metals_p1_factory.pi",
                mime="application/octet-stream"
            )
    elif selection == "Electrolytes":
        with st.expander("Electrolytes P0 extractor"):
            st.code("""[PH]""", language="plaintext")
            st.download_button(
                label="Download P0 Extractor",
                data="https://example.com/electrolytes_p0_extractor.pi",
                file_name="electrolytes_p0_extractor.pi",
                mime="application/octet-stream"
            )
        with st.expander("Electrolytes P1 Factory"):
            st.caption("Electrolytes P1 Factory")
            st.code("""[PH]""", language="plaintext")
            st.download_button(
                label="Download P1 Factory",
                data="https://example.com/electrolytes_p1_factory.pi",
                file_name="electrolytes_p1_factory.pi",
                mime="application/octet-stream"
            )
        with st.expander("Electrolytes P1 Extractor + Factory"):
            st.caption("Electrolytes P1 Extractor + Factory")
            st.code("""[PH]""", language="plaintext")
            st.download_button(
                label="Download P1 Extractor + Factory",
                data="https://example.com/electrolytes_p1_factory.pi",
                file_name="electrolytes_p1_factory.pi",
                mime="application/octet-stream"
            )
    elif selection == "Oxygen":
        with st.expander("Oxygen P0 extractor"):
            st.code("""[PH]""", language="plaintext")
            st.download_button(
                label="Download P0 Extractor",
                data="https://example.com/oxygen_p0_extractor.pi",
                file_name="oxygen_p0_extractor.pi",
                mime="application/octet-stream"
            )
        with st.expander("Oxygen P1 Factory"):
            st.caption("Oxygen P1 Factory")
            st.code("""[PH]""", language="plaintext")
            st.download_button(
                label="Download P1 Factory",
                data="https://example.com/oxygen_p1_factory.pi",
                file_name="oxygen_p1_factory.pi",
                mime="application/octet-stream"
            )
        with st.expander("Oxygen P1 Extractor + Factory"):
            st.caption("Oxygen P1 Extractor + Factory")
            st.code("""[PH]""", language="plaintext")
            st.download_button(
                label="Download P1 Extractor + Factory",
                data="https://example.com/oxygen_p1_factory.pi",
                file_name="oxygen_p1_factory.pi",
                mime="application/octet-stream"
            )
    elif selection == "Oxidising Compound":
        with st.expander("Oxidising Compound P0 extractor"):
            st.code("""[PH]""", language="plaintext")
            st.download_button(
                label="Download P0 Extractor",
                data="https://example.com/oxidising_compound_p0_extractor.pi",
                file_name="oxidising_compound_p0_extractor.pi",
                mime="application/octet-stream"
            )
        with st.expander("Oxidising Compound P1 Factory"):
            st.caption("Oxidising Compound P1 Factory")
            st.code("""[PH]""", language="plaintext")
            st.download_button(
                label="Download P1 Factory",
                data="https://example.com/oxidising_compound_p1_factory.pi",
                file_name="oxidising_compound_p1_factory.pi",
                mime="application/octet-stream"
            )
        with st.expander("Oxidising Compound P1 Extractor + Factory"):
            st.caption("Oxidising Compound P1 Extractor + Factory")
            st.code("""[PH]""", language="plaintext")
            st.download_button(
                label="Download P1 Extractor + Factory",
                data="https://example.com/oxidising_compound_p1_factory.pi",
                file_name="oxidising_compound_p1_factory.pi",
                mime="application/octet-stream"
            )
elif planet_choice == "Ice":
    selection = st.pills("Ice Planet Templates", ["Water", "Toxic Metal", "Bacteria", "Oxygen", "Biomass"])
    if selection == "Water":
        with st.expander("Water P0 extractor"):
            st.code("""[PH]""", language="plaintext")
            st.download_button(
                label="Download P0 Extractor",
                data="https://example.com/water_p0_extractor.pi",
                file_name="water_p0_extractor.pi",
                mime="application/octet-stream"
            )
        with st.expander("Water P1 Factory"):
            st.caption("Water P1 Factory")
            st.code("""[PH]""", language="plaintext")
            st.download_button(
                label="Download P1 Factory",
                data="https://example.com/water_p1_factory.pi",
                file_name="water_p1_factory.pi",
                mime="application/octet-stream"
            )
        with st.expander("Water P1 Extractor + Factory"):
            st.caption("Water P1 Extractor + Factory")
            st.code("""[PH]""", language="plaintext")
            st.download_button(
                label="Download P1 Extractor + Factory",
                data="https://example.com/water_p1_factory.pi",
                file_name="water_p1_factory.pi",
                mime="application/octet-stream"
            )
    elif selection == "Toxic Metal":
        with st.expander("Toxic Metal P0 extractor"):
            st.code("""[PH]""", language="plaintext")
            st.download_button(
                label="Download P0 Extractor",
                data="https://example.com/frozen_gas_p0_extractor.pi",
                file_name="frozen_gas_p0_extractor.pi",
                mime="application/octet-stream"
            )
        with st.expander("Toxic Metal P1 Factory"):
            st.caption("Frozen Gas P1 Factory")
            st.code("""[PH]""", language="plaintext")
            st.download_button(
                label="Download P1 Factory",
                data="https://example.com/frozen_gas_p1_factory.pi",
                file_name="frozen_gas_p1_factory.pi",
                mime="application/octet-stream"
            )
        with st.expander("Toxic Metal P1 Extractor + Factory"):
            st.caption("Frozen Gas P1 Extractor + Factory")
            st.code("""[PH]""", language="plaintext")
            st.download_button(
                label="Download P1 Extractor + Factory",
                data="https://example.com/frozen_gas_p1_factory.pi",
                file_name="frozen_gas_p1_factory.pi",
                mime="application/octet-stream"
            )
    elif selection == "Bacteria":
        with st.expander("Bacteria P0 extractor"):
            st.code("""[PH]""", language="plaintext")
            st.download_button(
                label="Download P0 Extractor",
                data="https://example.com/bacteria_p0_extractor.pi",
                file_name="bacteria_p0_extractor.pi",
                mime="application/octet-stream"
            )
        with st.expander("Bacteria P1 Factory"):
            st.caption("Bacteria P1 Factory")
            st.code("""[PH]""", language="plaintext")
            st.download_button(
                label="Download P1 Factory",
                data="https://example.com/bacteria_p1_factory.pi",
                file_name="bacteria_p1_factory.pi",
                mime="application/octet-stream"
            )
        with st.expander("Bacteria P1 Extractor + Factory"):
            st.caption("Bacteria P1 Extractor + Factory")
            st.code("""[PH]""", language="plaintext")
            st.download_button(
                label="Download P1 Extractor + Factory",
                data="https://example.com/bacteria_p1_factory.pi",
                file_name="bacteria_p1_factory.pi",
                mime="application/octet-stream"
            )
    elif selection == "Oxygen":
        with st.expander("Oxygen P0 extractor"):
            st.code("""[PH]""", language="plaintext")
            st.download_button(
                label="Download P0 Extractor",
                data="https://example.com/oxygen_p0_extractor.pi",
                file_name="oxygen_p0_extractor.pi",
                mime="application/octet-stream"
            )
        with st.expander("Oxygen P1 Factory"):
            st.caption("Oxygen P1 Factory")
            st.code("""[PH]""", language="plaintext")
            st.download_button(
                label="Download P1 Factory",
                data="https://example.com/oxygen_p1_factory.pi",
                file_name="oxygen_p1_factory.pi",
                mime="application/octet-stream"
            )
        with st.expander("Oxygen P1 Extractor + Factory"):
            st.caption("Oxygen P1 Extractor + Factory")
            st.code("""[PH]""", language="plaintext")
            st.download_button(
                label="Download P1 Extractor + Factory",
                data="https://example.com/oxygen_p1_factory.pi",
                file_name="oxygen_p1_factory.pi",
                mime="application/octet-stream"
            )
    elif selection == "Biomass":
        with st.expander("Biomass P0 extractor"):
            st.code("""[PH]""", language="plaintext")
            st.download_button(
                label="Download P0 Extractor",
                data="https://example.com/biomass_p0_extractor.pi",
                file_name="biomass_p0_extractor.pi",
                mime="application/octet-stream"
            )
        with st.expander("Biomass P1 Factory"):
            st.caption("Biomass P1 Factory")
            st.code("""[PH]""", language="plaintext")
            st.download_button(
                label="Download P1 Factory",
                data="https://example.com/biomass_p1_factory.pi",
                file_name="biomass_p1_factory.pi",
                mime="application/octet-stream"
            )
        with st.expander("Biomass P1 Extractor + Factory"):
            st.caption("Biomass P1 Extractor + Factory")
            st.code("""[PH]""", language="plaintext")
            st.download_button(
                label="Download P1 Extractor + Factory",
                data="https://example.com/biomass_p1_factory.pi",
                file_name="biomass_p1_factory.pi",
                mime="application/octet-stream"
            )
elif planet_choice == "Lava":
    selection = st.pills("Reactive Metals", "Silicon", "Toxic Metals", " Chiral Structures", "Plasmoids")
    if selection == "Reactive Metals":
        with st.expander("Reactive Metals P0 extractor"):
            st.code("""[PH]""", language="plaintext")
            st.download_button(
                label="Download P0 Extractor",
                data="https://example.com/reactive_metals_p0_extractor.pi",
                file_name="reactive_metals_p0_extractor.pi",
                mime="application/octet-stream"
            )
        with st.expander("Reactive Metals P1 Factory"):
            st.caption("Reactive Metals P1 Factory")
            st.code("""[PH]""", language="plaintext")
            st.download_button(
                label="Download P1 Factory",
                data="https://example.com/reactive_metals_p1_factory.pi",
                file_name="reactive_metals_p1_factory.pi",
                mime="application/octet-stream"
            )
        with st.expander("Reactive Metals P1 Extractor + Factory"):
            st.caption("Reactive Metals P1 Extractor + Factory")
            st.code("""[PH]""", language="plaintext")
            st.download_button(
                label="Download P1 Extractor + Factory",
                data="https://example.com/reactive_metals_p1_factory.pi",
                file_name="reactive_metals_p1_factory.pi",
                mime="application/octet-stream"
            )
    elif selection == "Silicon":
        with st.expander("Silicon P0 extractor"):
            st.code("""[PH]""", language="plaintext")
            st.download_button(
                label="Download P0 Extractor",
                data="https://example.com/silicon_p0_extractor.pi",
                file_name="silicon_p0_extractor.pi",
                mime="application/octet-stream"
            )
        with st.expander("Silicon P1 Factory"):
            st.caption("Silicon P1 Factory")
            st.code("""[PH]""", language="plaintext")
            st.download_button(
                label="Download P1 Factory",
                data="https://example.com/silicon_p1_factory.pi",
                file_name="silicon_p1_factory.pi",
                mime="application/octet-stream"
            )
        with st.expander("Silicon P1 Extractor + Factory"):
            st.caption("Silicon P1 Extractor + Factory")
            st.code("""[PH]""", language="plaintext")
            st.download_button(
                label="Download P1 Extractor + Factory",
                data="https://example.com/silicon_p1_factory.pi",
                file_name="silicon_p1_factory.pi",
                mime="application/octet-stream"
            )
    elif selection == "Toxic Metals":
        with st.expander("Toxic Metals P0 extractor"):
            st.code("""[PH]""", language="plaintext")
            st.download_button(
                label="Download P0 Extractor",
                data="https://example.com/toxic_metals_p0_extractor.pi",
                file_name="toxic_metals_p0_extractor.pi",
                mime="application/octet-stream"
            )
        with st.expander("Toxic Metals P1 Factory"):
            st.caption("Toxic Metals P1 Factory")
            st.code("""[PH]""", language="plaintext")
            st.download_button(
                label="Download P1 Factory",
                data="https://example.com/toxic_metals_p1_factory.pi",
                file_name="toxic_metals_p1_factory.pi",
                mime="application/octet-stream"
            )
        with st.expander("Toxic Metals P1 Extractor + Factory"):
            st.caption("Toxic Metals P1 Extractor + Factory")
            st.code("""[PH]""", language="plaintext")
            st.download_button(
                label="Download P1 Extractor + Factory",
                data="https://example.com/toxic_metals_p1_factory.pi",
                file_name="toxic_metals_p1_factory.pi",
                mime="application/octet-stream"
            )
    elif selection == "Chiral Structures":
        with st.expander("Chiral Structures P0 extractor"):
            st.code("""[PH]""", language="plaintext")
            st.download_button(
                label="Download P0 Extractor",
                data="https://example.com/chiral_structures_p0_extractor.pi",
                file_name="chiral_structures_p0_extractor.pi",
                mime="application/octet-stream"
            )
        with st.expander("Chiral Structures P1 Factory"):
            st.caption("Chiral Structures P1 Factory")
            st.code("""[PH]""", language="plaintext")
            st.download_button(
                label="Download P1 Factory",
                data="https://example.com/chiral_structures_p1_factory.pi",
                file_name="chiral_structures_p1_factory.pi",
                mime="application/octet-stream"
            )
        with st.expander("Chiral Structures P1 Extractor + Factory"):
            st.caption("Chiral Structures P1 Extractor + Factory")
            st.code("""[PH]""", language="plaintext")
            st.download_button(
                label="Download P1 Extractor + Factory",
                data="https://example.com/chiral_structures_p1_factory.pi",
                file_name="chiral_structures_p1_factory.pi",
                mime="application/octet-stream"
            )
    elif selection == "Plasmoids":
        with st.expander("Plasmoids P0 extractor"):
            st.code("""[PH]""", language="plaintext")
            st.download_button(
                label="Download P0 Extractor",
                data="https://example.com/plasmoids_p0_extractor.pi",
                file_name="plasmoids_p0_extractor.pi",
                mime="application/octet-stream"
            )
        with st.expander("Plasmoids P1 Factory"):
            st.caption("Plasmoids P1 Factory")
            st.code("""[PH]""", language="plaintext")
            st.download_button(
                label="Download P1 Factory",
                data="https://example.com/plasmoids_p1_factory.pi",
                file_name="plasmoids_p1_factory.pi",
                mime="application/octet-stream"
            )
        with st.expander("Plasmoids P1 Extractor + Factory"):
            st.caption("Plasmoids P1 Extractor + Factory")
            st.code("""[PH]""", language="plaintext")
            st.download_button(
                label="Download P1 Extractor + Factory",
                data="https://example.com/plasmoids_p1_factory.pi",
                file_name="plasmoids_p1_factory.pi",
                mime="application/octet-stream"
            )
elif planet_choice == "Oceanic":
    selection = st.pills("Oceanic Planet Templates", ["Water", "Biofuel", "Proteins", "Bacteria", "Biomass"])
    if selection == "Water":
        with st.expander("Water P0 extractor"):
            st.code("""[PH]""", language="plaintext")
            st.download_button(
                label="Download P0 Extractor",
                data="https://example.com/water_p0_extractor.pi",
                file_name="water_p0_extractor.pi",
                mime="application/octet-stream"
            )
        with st.expander("Water P1 Factory"):
            st.caption("Water P1 Factory")
            st.code("""[PH]""", language="plaintext")
            st.download_button(
                label="Download P1 Factory",
                data="https://example.com/water_p1_factory.pi",
                file_name="water_p1_factory.pi",
                mime="application/octet-stream"
            )
        with st.expander("Water P1 Extractor + Factory"):
            st.caption("Water P1 Extractor + Factory")
            st.code("""[PH]""", language="plaintext")
            st.download_button(
                label="Download P1 Extractor + Factory",
                data="https://example.com/water_p1_factory.pi",
                file_name="water_p1_factory.pi",
                mime="application/octet-stream"
            )
    elif selection == "Biofuel":
        with st.expander("Biofuel P0 extractor"):
            st.code("""[PH]""", language="plaintext")
            st.download_button(
                label="Download P0 Extractor",
                data="https://example.com/biofuel_p0_extractor.pi",
                file_name="biofuel_p0_extractor.pi",
                mime="application/octet-stream"
            )
        with st.expander("Biofuel P1 Factory"):
            st.caption("Biofuel P1 Factory")
            st.code("""[PH]""", language="plaintext")
            st.download_button(
                label="Download P1 Factory",
                data="https://example.com/biofuel_p1_factory.pi",
                file_name="biofuel_p1_factory.pi",
                mime="application/octet-stream"
            )
        with st.expander("Biofuel P1 Extractor + Factory"):
            st.caption("Biofuel P1 Extractor + Factory")
            st.code("""[PH]""", language="plaintext")
            st.download_button(
                label="Download P1 Extractor + Factory",
                data="https://example.com/biofuel_p1_factory.pi",
                file_name="biofuel_p1_factory.pi",
                mime="application/octet-stream")
    elif selection == "Proteins":
        with st.expander("Proteins P0 extractor"):
            st.code("""[PH]""", language="plaintext")
            st.download_button(
                label="Download P0 Extractor",
                data="https://example.com/proteins_p0_extractor.pi",
                file_name="proteins_p0_extractor.pi",
                mime="application/octet-stream"
            )
        with st.expander("Proteins P1 Factory"):
            st.caption("Proteins P1 Factory")
            st.code("""[PH]""", language="plaintext")
            st.download_button(
                label="Download P1 Factory",
                data="https://example.com/proteins_p1_factory.pi",
                file_name="proteins_p1_factory.pi",
                mime="application/octet-stream"
            )
        with st.expander("Proteins P1 Extractor + Factory"):
            st.caption("Proteins P1 Extractor + Factory")
            st.code("""[PH]""", language="plaintext")
            st.download_button(
                label="Download P1 Extractor + Factory",
                data="https://example.com/proteins_p1_factory.pi",
                file_name="proteins_p1_factory.pi",
                mime="application/octet-stream"
            )
    elif selection == "Bacteria":
        with st.expander("Bacteria P0 extractor"):
            st.code("""[PH]""", language="plaintext")
            st.download_button(
                label="Download P0 Extractor",
                data="https://example.com/bacteria_p0_extractor.pi",
                file_name="bacteria_p0_extractor.pi",
                mime="application/octet-stream"
            )
        with st.expander("Bacteria P1 Factory"):
            st.caption("Bacteria P1 Factory")
            st.code("""[PH]""", language="plaintext")
            st.download_button(
                label="Download P1 Factory",
                data="https://example.com/bacteria_p1_factory.pi",
                file_name="bacteria_p1_factory.pi",
                mime="application/octet-stream"
            )
        with st.expander("Bacteria P1 Extractor + Factory"):
            st.caption("Bacteria P1 Extractor + Factory")
            st.code("""[PH]""", language="plaintext")
            st.download_button(
                label="Download P1 Extractor + Factory",
                data="https://example.com/bacteria_p1_factory.pi",
                file_name="bacteria_p1_factory.pi",
                mime="application/octet-stream"
            )
    elif selection == "Biomass":
        with st.expander("Biomass P0 extractor"):
            st.code("""[PH]""", language="plaintext")
            st.download_button(
                label="Download P0 Extractor",
                data="https://example.com/biomass_p0_extractor.pi",
                file_name="biomass_p0_extractor.pi",
                mime="application/octet-stream"
            )
        with st.expander("Biomass P1 Factory"):
            st.caption("Biomass P1 Factory")
            st.code("""[PH]""", language="plaintext")
            st.download_button(
                label="Download P1 Factory",
                data="https://example.com/biomass_p1_factory.pi",
                file_name="biomass_p1_factory.pi",
                mime="application/octet-stream"
            )
        with st.expander("Biomass P1 Extractor + Factory"):
            st.caption("Biomass P1 Extractor + Factory")
            st.code("""[PH]""", language="plaintext")
            st.download_button(
                label="Download P1 Extractor + Factory",
                data="https://example.com/biomass_p1_factory.pi",
                file_name="biomass_p1_factory.pi",
                mime="application/octet-stream"
            )
