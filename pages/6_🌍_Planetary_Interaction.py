import streamlit as st
import pandas as pd
from pi_products import PI_Products

st.set_page_config(
    page_title="Planetary Interaction Guide",
    page_icon="🌍",
    layout="wide",
)

st.sidebar.success("This page will only contain templates and PI calculations for commodities that are produced natively in Dog Pound")

st.title("🌍 Planetary Interaction Guide")
st.markdown("""It's a love-hate relationship honestly.""")

st.divider()
st.header("Planetary Interaction Overview")
st.markdown("""
Planetary Interaction (PI) is a feature in EVE Online that allows players to establish colonies on planets and extract resources. It involves setting up structures, managing resources, and optimizing production chains. PI can be a lucrative activity, especially for players who invest time in understanding the mechanics and optimizing their operations.""")
st.write("There is too much to cover in this guide, so we will be linking a good playlist that covers everything you need to know about PI. Additionally, this page will store PI templates specifically for LUX and PI calculations")

st.info("It is highly recommended for players who do not wish to engage fully with PI to grab one of the 'P1 Extractor + Factory' templates below and use corp buy back for passive income. ")

st.video("https://www.youtube.com/watch?v=9lC-Cp8ymOY&list=PLXllDeIzDzd5t13rVjcTRpLxWEgzGVBmU")

st.divider()
st.header("PI Templates")

st.write('Even if you know nothing about PI, it is still worth setting up a basic extractor, this will provide you a steady passive income.')

st.info("These templates are made using command center level 5, as not everyone have command center level 6. Simply copy the code and paste it into your template window.")

planet_choice = st.selectbox("Select a planet type to view templates:", ("Gas", "Ice", "Lava", "Oceanic"), index=None)

## Gas planet
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
            st.code("""{"CmdCtrLv": 4, "Cmt": "Gas - Reactive Metals - E2 F4", "Diam": 37980.0, "L": [{"D": 5, "Lv": 0, "S": 3}, {"D": 5, "Lv": 0, "S": 2}, {"D": 5, "Lv": 0, "S": 1}, {"D": 7, "Lv": 0, "S": 5}, {"D": 8, "Lv": 0, "S": 4}, {"D": 6, "Lv": 0, "S": 5}, {"D": 5, "Lv": 0, "S": 4}], "P": [{"H": 0, "La": 1.44013, "Lo": 3.15807, "S": 2398, "T": 2492}, {"H": 0, "La": 1.42815, "Lo": 3.13689, "S": 2398, "T": 2492}, {"H": 0, "La": 1.44653, "Lo": 3.14781, "S": 2398, "T": 2492}, {"H": 0, "La": 1.42228, "Lo": 3.14767, "S": 2398, "T": 2492}, {"H": 0, "La": 1.43429, "Lo": 3.14738, "S": null, "T": 2543}, {"H": 2, "La": 1.42812, "Lo": 3.15855, "S": 2267, "T": 3060}, {"H": 10, "La": 1.44044, "Lo": 3.13693, "S": 2267, "T": 3060}, {"H": 0, "La": 1.41608, "Lo": 3.13633, "S": null, "T": 2536}], "Pln": 13, "R": [{"P": [4, 5], "Q": 20, "T": 2398}, {"P": [2, 5], "Q": 20, "T": 2398}, {"P": [8, 4], "Q": 3000, "T": 2267}, {"P": [8, 4, 5, 2], "Q": 3000, "T": 2267}, {"P": [8, 4, 5, 1], "Q": 3000, "T": 2267}, {"P": [8, 4, 5, 3], "Q": 3000, "T": 2267}, {"P": [1, 5], "Q": 20, "T": 2398}, {"P": [3, 5], "Q": 20, "T": 2398}, {"P": [6, 5, 4, 8], "Q": 16308, "T": 2267}, {"P": [7, 5, 4, 8], "Q": 90100, "T": 2267}]}""", language="plaintext", wrap_lines=True)

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
            st.code("""{"CmdCtrLv": 4, "Cmt": "Gas - Electrolyte - E2 F4", "Diam": 37980.0, "L": [{"D": 2, "Lv": 0, "S": 4}, {"D": 2, "Lv": 0, "S": 1}, {"D": 2, "Lv": 0, "S": 3}, {"D": 2, "Lv": 0, "S": 6}, {"D": 2, "Lv": 0, "S": 8}, {"D": 2, "Lv": 0, "S": 7}, {"D": 1, "Lv": 0, "S": 5}], "P": [{"H": 0, "La": 2.33004, "Lo": 1.8916, "S": 2390, "T": 2492}, {"H": 0, "La": 2.34104, "Lo": 1.88484, "S": null, "T": 2543}, {"H": 2, "La": 2.33951, "Lo": 1.90247, "S": 2309, "T": 3060}, {"H": 10, "La": 2.34279, "Lo": 1.86827, "S": 2309, "T": 3060}, {"H": 0, "La": 2.32013, "Lo": 1.88063, "S": null, "T": 2536}, {"H": 0, "La": 2.35053, "Lo": 1.89561, "S": 2390, "T": 2492}, {"H": 0, "La": 2.3314, "Lo": 1.87486, "S": 2390, "T": 2492}, {"H": 0, "La": 2.35262, "Lo": 1.87894, "S": 2390, "T": 2492}], "Pln": 13, "R": [{"P": [5, 1], "Q": 3000, "T": 2309}, {"P": [5, 1, 2, 7], "Q": 3000, "T": 2309}, {"P": [5, 1, 2, 8], "Q": 3000, "T": 2309}, {"P": [1, 2], "Q": 20, "T": 2390}, {"P": [7, 2], "Q": 20, "T": 2390}, {"P": [8, 2], "Q": 20, "T": 2390}, {"P": [6, 2], "Q": 20, "T": 2390}, {"P": [4, 2, 1, 5], "Q": 74592, "T": 2309}, {"P": [3, 2, 1, 5], "Q": 16600, "T": 2309}, {"P": [5, 1, 2, 6], "Q": 3000, "T": 2309}]}""", language="markdown", wrap_lines=True)
 
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
            st.code("""{"CmdCtrLv": 4, "Cmt": "Gas - Oxygen - E2 F4", "Diam": 193520.0, "L": [{"D": 7, "Lv": 0, "S": 6}, {"D": 1, "Lv": 0, "S": 3}, {"D": 8, "Lv": 0, "S": 6}, {"D": 6, "Lv": 0, "S": 3}, {"D": 4, "Lv": 0, "S": 6}, {"D": 6, "Lv": 0, "S": 5}, {"D": 6, "Lv": 0, "S": 2}], "P": [{"H": 0, "La": 0.9158, "Lo": 3.11935, "S": null, "T": 2536}, {"H": 0, "La": 0.94803, "Lo": 3.11175, "S": 3683, "T": 2492}, {"H": 0, "La": 0.92623, "Lo": 3.12689, "S": 3683, "T": 2492}, {"H": 0, "La": 0.9367, "Lo": 3.10426, "S": null, "T": 3060}, {"H": 0, "La": 0.92629, "Lo": 3.11175, "S": 3683, "T": 2492}, {"H": 0, "La": 0.93709, "Lo": 3.12025, "S": null, "T": 2543}, {"H": 10, "La": 0.93728, "Lo": 3.13522, "S": 2310, "T": 3060}, {"H": 0, "La": 0.9478, "Lo": 3.127, "S": 3683, "T": 2492}], "Pln": 13, "R": [{"P": [3, 6], "Q": 20, "T": 3683}, {"P": [5, 6], "Q": 20, "T": 3683}, {"P": [8, 6], "Q": 20, "T": 3683}, {"P": [2, 6], "Q": 20, "T": 3683}, {"P": [1, 3], "Q": 3000, "T": 2310}, {"P": [1, 3, 6, 5], "Q": 3000, "T": 2310}, {"P": [1, 3, 6, 8], "Q": 3000, "T": 2310}, {"P": [1, 3, 6, 2], "Q": 3000, "T": 2310}, {"P": [7, 6, 3, 1], "Q": 60940, "T": 2310}]}""", language="plaintext", wrap_lines=True)

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

## Ice planet
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
            st.code("""{"CmdCtrLv": 4, "Cmt": "Ice - Water - E2 F4", "Diam": 52280.0, "L": [{"D": 2, "Lv": 0, "S": 6}, {"D": 5, "Lv": 0, "S": 2}, {"D": 4, "Lv": 0, "S": 7}, {"D": 2, "Lv": 0, "S": 8}, {"D": 2, "Lv": 0, "S": 7}, {"D": 2, "Lv": 0, "S": 1}, {"D": 3, "Lv": 0, "S": 2}], "P": [{"H": 0, "La": 0.48728, "Lo": 6.23779, "S": 3645, "T": 2493}, {"H": 0, "La": 0.49794, "Lo": 6.22587, "S": null, "T": 2552}, {"H": 2, "La": 0.49876, "Lo": 6.25096, "S": 2268, "T": 3061}, {"H": 0, "La": 0.47674, "Lo": 6.22501, "S": null, "T": 2257}, {"H": 10, "La": 0.49801, "Lo": 6.2007, "S": 2268, "T": 3061}, {"H": 0, "La": 0.50896, "Lo": 6.23632, "S": 3645, "T": 2493}, {"H": 0, "La": 0.48724, "Lo": 6.212, "S": 3645, "T": 2493}, {"H": 0, "La": 0.50891, "Lo": 6.21158, "S": 3645, "T": 2493}], "Pln": 12, "R": [{"P": [8, 2], "Q": 20, "T": 3645}, {"P": [6, 2], "Q": 20, "T": 3645}, {"P": [7, 2], "Q": 20, "T": 3645}, {"P": [1, 2], "Q": 20, "T": 3645}, {"P": [4, 7], "Q": 3000, "T": 2268}, {"P": [4, 7, 2, 1], "Q": 3000, "T": 2268}, {"P": [4, 7, 2, 8], "Q": 3000, "T": 2268}, {"P": [4, 7, 2, 6], "Q": 3000, "T": 2268}, {"P": [3, 2, 7, 4], "Q": 18012, "T": 2268}, {"P": [5, 2, 7, 4], "Q": 61776, "T": 2268}]}""", language="plaintext", wrap_lines=True)

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
            st.code("""{"CmdCtrLv": 4, "Cmt": "Ice - Toxic Metals - E2 F4", "Diam": 52280.0, "L": [{"D": 7, "Lv": 0, "S": 4}, {"D": 7, "Lv": 0, "S": 5}, {"D": 7, "Lv": 0, "S": 1}, {"D": 7, "Lv": 0, "S": 6}, {"D": 6, "Lv": 0, "S": 2}, {"D": 8, "Lv": 0, "S": 7}, {"D": 7, "Lv": 0, "S": 3}], "P": [{"H": 10, "La": 1.5185, "Lo": 5.77048, "S": 2272, "T": 3061}, {"H": 0, "La": 1.49425, "Lo": 5.76984, "S": null, "T": 2257}, {"H": 0, "La": 1.51813, "Lo": 5.79148, "S": 2400, "T": 2493}, {"H": 0, "La": 1.50628, "Lo": 5.77042, "S": 2400, "T": 2493}, {"H": 0, "La": 1.52441, "Lo": 5.781, "S": 2400, "T": 2493}, {"H": 0, "La": 1.50026, "Lo": 5.78113, "S": 2400, "T": 2493}, {"H": 0, "La": 1.51231, "Lo": 5.78086, "S": null, "T": 2552}, {"H": 2, "La": 1.50611, "Lo": 5.79192, "S": 2272, "T": 3061}], "Pln": 12, "R": [{"P": [1, 7, 6, 2], "Q": 87032, "T": 2272}, {"P": [8, 7, 6, 2], "Q": 22168, "T": 2272}, {"P": [3, 7], "Q": 20, "T": 2400}, {"P": [5, 7], "Q": 20, "T": 2400}, {"P": [6, 7], "Q": 20, "T": 2400}, {"P": [4, 7], "Q": 20, "T": 2400}, {"P": [2, 6], "Q": 3000, "T": 2272}, {"P": [2, 6, 7, 4], "Q": 3000, "T": 2272}, {"P": [2, 6, 7, 3], "Q": 3000, "T": 2272}, {"P": [2, 6, 7, 5], "Q": 3000, "T": 2272}]}""", language="plaintext", wrap_lines=True)

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
            st.code("""{"CmdCtrLv": 4, "Cmt": "Ice - Bacteria - E2 F4", "Diam": 52280.0, "L": [{"D": 5, "Lv": 0, "S": 1}, {"D": 5, "Lv": 0, "S": 2}, {"D": 6, "Lv": 0, "S": 5}, {"D": 5, "Lv": 0, "S": 4}, {"D": 8, "Lv": 0, "S": 4}, {"D": 5, "Lv": 0, "S": 3}, {"D": 7, "Lv": 0, "S": 5}], "P": [{"H": 0, "La": 1.58934, "Lo": 6.07632, "S": 2393, "T": 2493}, {"H": 0, "La": 1.59555, "Lo": 6.05248, "S": 2393, "T": 2493}, {"H": 0, "La": 1.601, "Lo": 6.07346, "S": 2393, "T": 2493}, {"H": 0, "La": 1.58383, "Lo": 6.05537, "S": 2393, "T": 2493}, {"H": 0, "La": 1.59172, "Lo": 6.06451, "S": null, "T": 2552}, {"H": 2, "La": 1.58019, "Lo": 6.06787, "S": 2073, "T": 3061}, {"H": 10, "La": 1.60341, "Lo": 6.06157, "S": 2073, "T": 3061}, {"H": 0, "La": 1.5872, "Lo": 6.04377, "S": null, "T": 2257}], "Pln": 12, "R": [{"P": [6, 5, 4, 8], "Q": 16464, "T": 2073}, {"P": [7, 5, 4, 8], "Q": 86292, "T": 2073}, {"P": [4, 5], "Q": 20, "T": 2393}, {"P": [2, 5], "Q": 20, "T": 2393}, {"P": [3, 5], "Q": 20, "T": 2393}, {"P": [1, 5], "Q": 20, "T": 2393}, {"P": [8, 4, 5, 2], "Q": 3000, "T": 2073}, {"P": [8, 4, 5, 1], "Q": 3000, "T": 2073}, {"P": [8, 4, 5, 3], "Q": 3000, "T": 2073}, {"P": [8, 4], "Q": 3000, "T": 2073}]}""", language="plaintext", wrap_lines=True)

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

## Lava planet
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
            st.code("""{"CmdCtrLv": 4, "Cmt": "Lava - Chiral Structures - E2 F4", "Diam": 14640.0, "L": [{"D": 7, "Lv": 0, "S": 3}, {"D": 7, "Lv": 0, "S": 6}, {"D": 7, "Lv": 0, "S": 5}, {"D": 8, "Lv": 0, "S": 7}, {"D": 7, "Lv": 0, "S": 4}, {"D": 2, "Lv": 0, "S": 6}, {"D": 1, "Lv": 0, "S": 7}], "P": [{"H": 10, "La": 0.49959, "Lo": 3.28876, "S": 2306, "T": 3062}, {"H": 0, "La": 0.48394, "Lo": 3.25002, "S": null, "T": 2558}, {"H": 0, "La": 0.48552, "Lo": 3.31994, "S": 2401, "T": 2469}, {"H": 0, "La": 0.49194, "Lo": 3.26927, "S": 2401, "T": 2469}, {"H": 0, "La": 0.49714, "Lo": 3.31361, "S": 2401, "T": 2469}, {"H": 0, "La": 0.48014, "Lo": 3.27475, "S": 2401, "T": 2469}, {"H": 0, "La": 0.48787, "Lo": 3.29468, "S": null, "T": 2555}, {"H": 2, "La": 0.47632, "Lo": 3.30179, "S": 2306, "T": 3062}], "Pln": 2015, "R": [{"P": [3, 7], "Q": 20, "T": 2401}, {"P": [5, 7], "Q": 20, "T": 2401}, {"P": [6, 7], "Q": 20, "T": 2401}, {"P": [4, 7], "Q": 20, "T": 2401}, {"P": [2, 6], "Q": 3000, "T": 2306}, {"P": [2, 6, 7, 4], "Q": 3000, "T": 2306}, {"P": [2, 6, 7, 3], "Q": 3000, "T": 2306}, {"P": [2, 6, 7, 5], "Q": 3000, "T": 2306}, {"P": [8, 7, 6, 2], "Q": 16436, "T": 2306}, {"P": [1, 7, 6, 2], "Q": 63740, "T": 2306}]}""", language="plaintext", wrap_lines=True)

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

## Oceanic planet
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
            st.code("""{"CmdCtrLv": 4, "Cmt": "Oceanic - Water - E2 F4", "Diam": 6460.0, "L": [{"D": 5, "Lv": 0, "S": 1}, {"D": 6, "Lv": 0, "S": 5}, {"D": 5, "Lv": 0, "S": 4}, {"D": 7, "Lv": 0, "S": 2}, {"D": 5, "Lv": 0, "S": 2}, {"D": 5, "Lv": 0, "S": 3}, {"D": 8, "Lv": 0, "S": 5}], "P": [{"H": 0, "La": 2.04519, "Lo": 5.00393, "S": 3645, "T": 2490}, {"H": 0, "La": 2.02705, "Lo": 4.98529, "S": 3645, "T": 2490}, {"H": 0, "La": 2.04816, "Lo": 4.99079, "S": 3645, "T": 2490}, {"H": 0, "La": 2.02409, "Lo": 4.99831, "S": 3645, "T": 2490}, {"H": 0, "La": 2.03585, "Lo": 4.99529, "S": null, "T": 2542}, {"H": 2, "La": 2.03346, "Lo": 5.00846, "S": 2268, "T": 3063}, {"H": 0, "La": 2.01541, "Lo": 4.98897, "S": null, "T": 2535}, {"H": 10, "La": 2.03877, "Lo": 4.98223, "S": 2268, "T": 3063}], "Pln": 2014, "R": [{"P": [8, 5, 2, 7], "Q": 142420, "T": 2268}, {"P": [6, 5, 2, 7], "Q": 31756, "T": 2268}, {"P": [3, 5], "Q": 20, "T": 3645}, {"P": [1, 5], "Q": 20, "T": 3645}, {"P": [2, 5], "Q": 20, "T": 3645}, {"P": [4, 5], "Q": 20, "T": 3645}, {"P": [7, 2], "Q": 3000, "T": 2268}, {"P": [7, 2, 5, 4], "Q": 3000, "T": 2268}, {"P": [7, 2, 5, 3], "Q": 3000, "T": 2268}, {"P": [7, 2, 5, 1], "Q": 3000, "T": 2268}]}""", language="plaintext", wrap_lines=True)

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
            st.code("""{"CmdCtrLv": 4, "Cmt": "Oceanic - Biofuel - E2 F4", "Diam": 6460.0, "L": [{"D": 5, "Lv": 0, "S": 4}, {"D": 4, "Lv": 0, "S": 2}, {"D": 4, "Lv": 0, "S": 8}, {"D": 1, "Lv": 0, "S": 2}, {"D": 4, "Lv": 0, "S": 7}, {"D": 6, "Lv": 0, "S": 4}, {"D": 4, "Lv": 0, "S": 3}], "P": [{"H": 0, "La": 0.83518, "Lo": 3.30075, "S": null, "T": 2535}, {"H": 0, "La": 0.83155, "Lo": 3.31631, "S": 2396, "T": 2490}, {"H": 0, "La": 0.84855, "Lo": 3.3408, "S": 2396, "T": 2490}, {"H": 0, "La": 0.83932, "Lo": 3.32877, "S": null, "T": 2542}, {"H": 2, "La": 0.82776, "Lo": 3.33319, "S": 2288, "T": 3063}, {"H": 10, "La": 0.85103, "Lo": 3.325, "S": 2288, "T": 3063}, {"H": 0, "La": 0.83689, "Lo": 3.34464, "S": 2396, "T": 2490}, {"H": 0, "La": 0.84332, "Lo": 3.3127, "S": 2396, "T": 2490}], "Pln": 2014, "R": [{"P": [1, 2], "Q": 3000, "T": 2288}, {"P": [1, 2, 4, 8], "Q": 3000, "T": 2288}, {"P": [1, 2, 4, 7], "Q": 3000, "T": 2288}, {"P": [1, 2, 4, 3], "Q": 3000, "T": 2288}, {"P": [8, 4], "Q": 20, "T": 2396}, {"P": [2, 4], "Q": 20, "T": 2396}, {"P": [7, 4], "Q": 20, "T": 2396}, {"P": [3, 4], "Q": 20, "T": 2396}, {"P": [5, 4, 2, 1], "Q": 17928, "T": 2288}, {"P": [6, 4, 2, 1], "Q": 66132, "T": 2288}]}""", language="plaintext", wrap_lines=True)
            
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
            st.code("""{"CmdCtrLv": 4, "Cmt": "Oceanic - Proteins - E2 F4", "Diam": 6460.0, "L": [{"D": 5, "Lv": 0, "S": 1}, {"D": 2, "Lv": 0, "S": 1}, {"D": 4, "Lv": 0, "S": 2}, {"D": 3, "Lv": 0, "S": 2}, {"D": 2, "Lv": 0, "S": 6}, {"D": 2, "Lv": 0, "S": 7}, {"D": 2, "Lv": 0, "S": 8}], "P": [{"H": 0, "La": 1.84993, "Lo": 1.62161, "S": 2395, "T": 2490}, {"H": 0, "La": 1.86143, "Lo": 1.61794, "S": null, "T": 2542}, {"H": 2, "La": 1.85978, "Lo": 1.63035, "S": 2287, "T": 3063}, {"H": 10, "La": 1.86341, "Lo": 1.60552, "S": 2287, "T": 3063}, {"H": 0, "La": 1.84058, "Lo": 1.61378, "S": null, "T": 2535}, {"H": 0, "La": 1.87124, "Lo": 1.62519, "S": 2395, "T": 2490}, {"H": 0, "La": 1.85191, "Lo": 1.6092, "S": 2395, "T": 2490}, {"H": 0, "La": 1.87333, "Lo": 1.61274, "S": 2395, "T": 2490}], "Pln": 2014, "R": [{"P": [7, 2], "Q": 20, "T": 2395}, {"P": [1, 2], "Q": 20, "T": 2395}, {"P": [8, 2], "Q": 20, "T": 2395}, {"P": [6, 2], "Q": 20, "T": 2395}, {"P": [4, 2, 1, 5], "Q": 46332, "T": 2287}, {"P": [3, 2, 1, 5], "Q": 12424, "T": 2287}, {"P": [5, 1, 2, 7], "Q": 3000, "T": 2287}, {"P": [5, 1], "Q": 3000, "T": 2287}, {"P": [5, 1, 2, 8], "Q": 3000, "T": 2287}, {"P": [5, 1, 2, 6], "Q": 3000, "T": 2287}]}""", language="plaintext", wrap_lines=True)

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

st.divider()

st.header("PI calculator")
st.subheader("Calculate your PI profits with the PI calculator.")
options = ["P1", "P2", "P3"]
tier = st.segmented_control("Select PI level", options)

try:
    selected_products = st.multiselect(
        "Select product(s)",
        list(PI_Products[tier].keys())
    )

    st.header("PI Output Calculator")

    with st.expander("PI Output Calculator"):
        st.markdown(
            "Enter the number of **P1 Factories** you are running per P1 commodity . "
            "Each P2 factory requires **2 P1 factory**. "
            "This calculator will estimate your **P1, P2, or P3 output per hour** based on the standard PI cycle times."
        )

            # Updated PI rates (per EVE standard):
        # Each P1 factory: 80 P1/hr, intakes 6000 P0/hr
        # Each P2 factory: 10 P2/hr, requires 160 P1/hr input (from 2 P1 factories)
        # Each P3 factory: 3 P3/hr, requires 10 P2/hr input (from 1 P2 factory)

        P1_per_factory_per_hour = 80
        P2_per_factory_per_hour = 10
        P3_per_factory_per_hour = 3

        # User enters number of P1 factories
        num_p1_factories = st.number_input("Number of P1 factories", min_value=1, value=4)

        # Calculate max number of P2 and P3 factories that can be fully fed
        max_p2_factories = num_p1_factories // 2  # 2 P1 factories feed 1 P2
        max_p3_factories = max_p2_factories // 1  # 1 P2 factory feeds 1 P3

        P1_per_hour = int((num_p1_factories/2) * P1_per_factory_per_hour)
        P2_per_hour = max_p2_factories * P2_per_factory_per_hour
        P3_per_hour = max_p3_factories * P3_per_factory_per_hour

        # Output for selected tier/product
        if tier == "P1":
            st.write(f"**P1 produced/Hr:** `{P1_per_hour}` units")
        elif tier == "P2":
            st.write(f"**P1 produced/Hr:** `{P1_per_hour}` units")
            st.write(f"**P2 produced/Hr:** `{P2_per_hour}` units")
            st.divider()
            st.write(f"**P3 produced/Day:** `{P2_per_hour*24}` units")
            st.write(f"**P3 produced/Month:** `{P2_per_hour*24*31}` units")
        elif tier == "P3":
            st.write(f"**P1 produced/Hr:** `{P1_per_hour}` units")
            st.write(f"**P2 produced/Hr:** `{P2_per_hour}` units")
            st.write(f"**P3 produced/Hr:** `{P3_per_hour}` units")
            st.divider()
            st.write(f"**P3 produced/Day:** `{P3_per_hour*24}` units")
            st.write(f"**P3 produced/Month:** `{P3_per_hour*24*31}` units")
        
        st.success("Multiply the output by the ISK of the product to get your total profit.")

        st.divider()
        st.write(f"**Average P0 extracted/Hr to maintain efficiency** `{num_p1_factories * 6000}` units")
        

        col1, col2 = st.columns(2)

        from graphviz import Digraph

        def build_graph(tier, product, dot=None, parent=None):
            """Recursively build a Graphviz Digraph for the PI breakdown."""
            if dot is None:
                dot = Digraph()
                dot.attr(rankdir='LR', size='8,4')
            node_label = f"{product}\n({tier})"
            dot.node(node_label, shape="box", font_name="Helvetica", fontsize="12")
            inputs = PI_Products[tier][product]["Input"]
            for item, qty in inputs.items():
                # Determine the correct tier for the child node
                if tier == "P3":
                    child_tier = "P2"
                elif tier == "P2":
                    child_tier = "P1"
                elif tier == "P1":
                    # If the item is in P0, label as P0, else as P1
                    child_tier = "P0" if "P0" in PI_Products and item in PI_Products["P0"] else "P1"
                else:
                    child_tier = tier  # fallback

                child_label = f"{item}\n({child_tier})"
                dot.node(child_label, shape="box", font_name="Helvetica", fontsize="12")
                dot.edge(child_label, node_label, label=f"x{qty}")

                # Only go deeper if not at P0
                if tier == "P3" and item in PI_Products["P2"]:
                    build_graph("P2", item, dot, child_label)
                elif tier == "P2" and item in PI_Products["P1"]:
                    build_graph("P1", item, dot, child_label)
                elif tier == "P1" and "P0" in PI_Products and item in PI_Products["P0"]:
                    # Optionally, you can expand P0 if you want to show raw resource sources
                    pass  # Usually P0 is the base, so stop here
            return dot

        st.markdown("#### PI Breakdown Flowchart")
        if selected_products:
            dot = Digraph()
            dot.attr(rankdir='LR', size='20,4')
            dot.attr(nodesep='0.5', ranksep='0.5')
            for product in selected_products:
                build_graph(tier, product, dot)
            st.graphviz_chart(dot, use_container_width=True)
        else:
            st.info("Please select at least one product to see the flowchart.")

except:
    st.info("Please select a PI level to see the products.") 