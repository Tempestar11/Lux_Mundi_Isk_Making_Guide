import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Lux PvP Guide",
    page_icon="☠️",
)

st.title("☠️ Lux PvP Guide")
st.markdown("""So you found some new friends... and you want to stab them in the back?""")
st.divider()

st.header("PvP with LUX?")
st.write("""Lux is not a PvP focused corporation, but we do have a few PvP enthusiasts who are willing to help you learn the ropes. We cannot teach how to PvP on a general basis, hence this page will document our doctrines, fits and how to fly them.""")
st.info("While you can earn isk doing PvP, it should not be your main source of income and you should expect to lose ships. If you are looking for a PvP focused corporation, we recommend you look elsewhere.")

st.divider()

st.header("Home Defense Fleet")
st.caption("These are ships to use when any of our structures are attacked and reinforced.")
st.write("Sniper DPS Ships")
with st.expander("Tornado Sniper Home Defense"):
    st.write("Run targetting range script for lock ranges beyond 100km, tracking speed as needed. Hits beyond 150km with Depleted Uranium and Optimal range script.")
    st.caption("Tornado Sniper - 150M ISK")
    st.code("""
        [Tornado, Tornado Home Defence]
        Signal Amplifier II
        Gyrostabilizer II
        Gyrostabilizer II
        Gyrostabilizer II

        Sensor Booster II
        Large Shield Extender II
        50MN Y-T8 Compact Microwarpdrive
        Tracking Computer II
        Tracking Computer II

        1400mm Prototype Siege Cannon
        1400mm Prototype Siege Cannon
        1400mm Prototype Siege Cannon
        1400mm Prototype Siege Cannon
        1400mm Prototype Siege Cannon
        1400mm Prototype Siege Cannon
        1400mm Prototype Siege Cannon
        1400mm Prototype Siege Cannon

        Medium Ancillary Current Router I
        Medium Ancillary Current Router I
        Medium Ancillary Current Router I

        Republic Fleet EMP L x1660
        Optimal Range Script x2
        Tracking Speed Script x2
        Republic Fleet Depleted Uranium L x1500
        Republic Fleet Fusion L x1500
        Targeting Range Script x1
        Scan Resolution Script x1
    """, language="markdown")
with st.expander("Naga Sniper Home Defense"):
    st.write("Run targetting range script for lock ranges beyond 80km, tracking speed as needed. Hits beyond 150km with Depleted Uranium and Optimal range script.")
    st.caption("Naga Sniper - 130M ISK")
    st.code("""
        [Naga, Naga Home Defense]
        Magnetic Field Stabilizer II
        Magnetic Field Stabilizer II
        Magnetic Field Stabilizer II

        F-12 Enduring Tracking Computer
        F-12 Enduring Tracking Computer
        F-12 Enduring Tracking Computer
        Alumel-Wired Enduring Sensor Booster
        10MN Y-S8 Compact Afterburner
        Large F-S9 Regolith Compact Shield Extender

        425mm Prototype Gauss Gun
        425mm Prototype Gauss Gun
        425mm Prototype Gauss Gun
        425mm Prototype Gauss Gun
        425mm Prototype Gauss Gun
        425mm Prototype Gauss Gun
        425mm Prototype Gauss Gun
        425mm Prototype Gauss Gun

        Medium Ancillary Current Router I
        Medium Hybrid Locus Coordinator II
        Medium Hybrid Locus Coordinator II

        Caldari Navy Uranium Charge L x2000
        Optimal Range Script x3
        Tracking Speed Script x3
        Caldari Navy Antimatter Charge L x2320
        Targeting Range Script x1
        Scan Resolution Script x1
    """, language="markdown")

st.write("Mid Range DPS Ships")
with st.expander("Caracal Home Defense (Alpha)"):
    st.write("This is a kiting fit. Keep your speed up while staying out of 10km of any hostiles. Missile range within 20km")
    st.caption("Caracal Mid Range - 40M ISK")
    st.code("""
        [Caracal, Caracal Home Defence Alpha]
        Damage Control II
        Ballistic Control System II
        Ballistic Control System II
        Ballistic Control System II

        Large Shield Extender II
        Large Shield Extender II
        Multispectrum Shield Hardener II
        Small F-RX Compact Capacitor Booster
        50MN Cold-Gas Enduring Microwarpdrive

        Experimental SV-2000 Rapid Light Missile Launcher
        Experimental SV-2000 Rapid Light Missile Launcher
        Experimental SV-2000 Rapid Light Missile Launcher
        Experimental SV-2000 Rapid Light Missile Launcher
        Experimental SV-2000 Rapid Light Missile Launcher

        Medium EM Shield Reinforcer I
        Medium Core Defense Field Extender I
        Medium Core Defense Field Extender I

        Warrior I x2

        Caldari Navy Scourge Light Missile x1500
        Caldari Navy Mjolnir Light Missile x1595
        Caldari Navy Nova Light Missile x1500
        Navy Cap Booster 400 x11
        """, language="markdown")
with st.expander("Caracal Home Defense (Omega)"):
    st.write("This is a kiting fit. Keep your speed up while staying out of 10km of any hostiles. Missile range within 20km")
    st.caption("Caracal Mid Range - 40M ISK")
    st.code("""
        [Caracal, Caracal Home Defence]
        Damage Control II
        Ballistic Control System II
        Ballistic Control System II
        Ballistic Control System II

        Large Shield Extender II
        Large Shield Extender II
        Multispectrum Shield Hardener II
        Small F-RX Compact Capacitor Booster
        50MN Cold-Gas Enduring Microwarpdrive

        Rapid Light Missile Launcher II
        Rapid Light Missile Launcher II
        Rapid Light Missile Launcher II
        Rapid Light Missile Launcher II
        Rapid Light Missile Launcher II

        Medium EM Shield Reinforcer I
        Medium Core Defense Field Extender I
        Medium Core Defense Field Extender I

        Warrior II x2

        Caldari Navy Scourge Light Missile x2000
        Mjolnir Fury Light Missile x1600
        Navy Cap Booster 400 x11
        Nova Fury Light Missile x1500
        """, language="markdown")

st.write("Ewar/Logi Ships")
with st.expander("Blackbird Home Defense"):
    st.write("Your sole job is to stay out of any DPS and jam the hell out of the ships with the highest DPS")
    st.caption("Blackbird Home Defense - 30M ISK")
    st.code("""
        [Blackbird, Blackbird Home Defence]
        Signal Distortion Amplifier II
        Signal Distortion Amplifier II
        Signal Distortion Amplifier II

        Compulsive Scoped Multispectral ECM
        Compulsive Scoped Multispectral ECM
        Compulsive Scoped Multispectral ECM
        Compulsive Scoped Multispectral ECM
        50MN Quad LiF Restrained Microwarpdrive
        Alumel-Wired Enduring Sensor Booster

        Experimental SV-2000 Rapid Light Missile Launcher
        Experimental SV-2000 Rapid Light Missile Launcher
        Experimental SV-2000 Rapid Light Missile Launcher

        Medium Particle Dispersion Projector I
        Medium Particle Dispersion Projector I
        Medium Signal Disruption Amplifier II

        'Integrated' Hobgoblin x2

        Targeting Range Script x1
        Caldari Navy Mjolnir Light Missile x1257
        Umbra Scoped Radar ECM x4
        BZ-5 Scoped Gravimetric ECM x4
        Enfeebling Scoped Ladar ECM x4
        Hypnos Scoped Magnetometric ECM x4
        """)

st.divider()
st.header("Stealth Torper Doctrine")
st.caption("Stealth bombers are long range glass cannons, if you're caught by anything you're dead. Torps have very high alpha, but low application to anything smaller than a battleship. Target painters can remedy this, however the more bombers fly together, the stronger they are.")
st.error("This fleet requires a separate ship to act as primary tackle, such as a dictor or a frigate with a warp disruptor. Bombers are not meant to be primary tackle, but rather pure DPS.")
st.markdown("Bombers")
with st.expander("Purifier"):
    st.write("Popular bomber as the extra low slot gives extra DPS.")
    st.caption("Purifier - 50M ISK")
    st.code("""
        [Purifier, Purifier Bomber]
        Ballistic Control System II
        Ballistic Control System II
        Ballistic Control System II

        Target Painter II
        Target Painter II
        1MN Afterburner II

        Covert Ops Cloaking Device II
        Prototype 'Arbalest' Torpedo Launcher
        Prototype 'Arbalest' Torpedo Launcher
        Prototype 'Arbalest' Torpedo Launcher

        Small Processor Overclocking Unit II
        Small Warhead Rigor Catalyst I

        Caldari Navy Mjolnir Torpedo x216
    """, language="markdown")
with st.expander("Manticore"):
    st.write("Extra mid slot for ECM burst allows you to get out if tackled.")    
    st.caption("Manticore - 50M ISK")
    st.code("""
        [Manticore, Manticore Bomber]
        Ballistic Control System II
        Ballistic Control System II

        1MN Y-S8 Compact Afterburner
        Target Painter II
        Target Painter II
        Multispectral ECM II

        Prototype 'Arbalest' Torpedo Launcher
        Prototype 'Arbalest' Torpedo Launcher
        Prototype 'Arbalest' Torpedo Launcher
        Covert Ops Cloaking Device II

        Small Warhead Rigor Catalyst II
        Small Processor Overclocking Unit I

        Caldari Navy Scourge Torpedo x216
    """, language="markdown")
with st.expander("Hound"):
    st.write("Use implants if CPU is over.")
    st.caption("Hound - 50M ISK")
    st.code("""
        [Hound, Hound Bomber]
        Ballistic Control System II
        Ballistic Control System II
        Ballistic Control System II

        Target Painter II
        Target Painter II
        1MN Afterburner I

        Prototype 'Arbalest' Torpedo Launcher
        Prototype 'Arbalest' Torpedo Launcher
        Prototype 'Arbalest' Torpedo Launcher
        Covert Ops Cloaking Device II

        Small Processor Overclocking Unit I
        Small Warhead Rigor Catalyst II

        Caldari Navy Nova Torpedo x218
    """, language="markdown")
with st.expander("Nemesis"):
    st.write("Lowest CPU available, rigged for align rather than application.")
    st.caption("Nemesis - 50M ISK")
    st.code("""
        [Nemesis, Nemesis Bomber]
        Ballistic Control System II
        Ballistic Control System II

        1MN Afterburner I
        Target Painter II
        Target Painter II
        Multispectral ECM II

        Prototype 'Arbalest' Torpedo Launcher
        Prototype 'Arbalest' Torpedo Launcher
        Prototype 'Arbalest' Torpedo Launcher
        Covert Ops Cloaking Device II

        Small Low Friction Nozzle Joints II
        Small Processor Overclocking Unit II

        Caldari Navy Inferno Torpedo x218
    """, language="markdown")

st.divider()
st.header("Triglavian Doctrine")
st.caption("This doctrine is focused on using the Triglavian ships, which are known for their speed and remote repair capabilities. Use your speed to kite, while spider tanking to spool up your damage. If there are significant jammers from the enemy, this doctrine should not engage.")
st.info("You may swap for T1 modules for all fits, but you will be outputting significant less DPS and remote rep. Other armor based ships may also be flown with this fleet.")
st.write("Command Ships")
with st.expander("Command Drekavac"):
    st.write("This is the main command ship for this doctrine, without remote repair however. One armor burst for extra EHP and two skirmish bursts for extra speed and tackle range.")
    st.error("This fit requires a CPU implant to fly")
    st.caption("Command Drekavac - 400m ISK")
    st.code("""
        [Drekavac, Command Drekavac]
        Medium Ancillary Armor Repairer
        Entropic Radiation Sink I
        Entropic Radiation Sink II
        Reactive Armor Hardener
        Multispectrum Coating II
        Nanofiber Internal Structure II
        Shadow Serpentis Medium Armor Repairer

        Warp Disruptor II
        Medium Capacitor Booster II
        50MN Microwarpdrive I
        Fleeting Compact Stasis Webifier

        Veles Heavy Entropic Disintegrator
        Armor Command Burst I
        Skirmish Command Burst I
        Skirmish Command Burst I

        Medium Command Processor I
        Medium Auxiliary Nano Pump I
        Medium Command Processor I
        
        Hobgoblin II x5

        Navy Cap Booster 800 x11
        Armor Reinforcement Charge x350
        Interdiction Maneuvers Charge x50
        Rapid Deployment Charge x50
        Occult M x500
        Mystic M x500
        Nanite Repair Paste x120
    """, language="markdown")
st.write("DPS Ships")
with st.expander("DPS Drekavac"):
    st.write("This is the main battlecruiser and DPS for this doctrine, with remote repair capabilities and high speed.")
    st.caption("Fleet Drekavac - 480M ISK")
    st.code("""
        [Drekavac, DPS Drekavac]
        Damage Control II
        Entropic Radiation Sink II
        Multispectrum Energized Membrane II
        Multispectrum Energized Membrane II
        Multispectrum Energized Membrane II
        800mm Rolled Tungsten Compact Plates
        Reactive Armor Hardener

        Initiated Compact Warp Disruptor
        Medium F-RX Compact Capacitor Booster
        50MN Y-T8 Compact Microwarpdrive
        Optical Compact Tracking Computer

        Medium Remote Armor Repairer II
        Medium Remote Armor Repairer II
        Veles Heavy Entropic Disintegrator
        Medium Ancillary Remote Armor Repairer

        Medium Trimark Armor Pump II
        Medium Trimark Armor Pump II
        Medium Capacitor Control Circuit II

        Hobgoblin II x5

        Occult M x500
        Mystic M x500
        Nanite Repair Paste x120
        Navy Cap Booster 800 x10
    """, language="markdown")
with st.expander("DPS Vedmak"):
    st.write("This is the main cruiser and DPS for this doctrine, with remote repair capabilities and high speed.")
    st.caption("Fleet Vedmak - 320M ISK")
    st.code("""
        [Vedmak, DPS Vedmak]
        Damage Control II
        Multispectrum Energized Membrane II
        Multispectrum Energized Membrane II
        Entropic Radiation Sink II
        Entropic Radiation Sink II
        Entropic Radiation Sink II

        Stasis Webifier II
        Warp Disruptor II
        Medium Capacitor Booster II
        50MN Y-T8 Compact Microwarpdrive

        Small Remote Armor Repairer II
        Veles Heavy Entropic Disintegrator
        Small Remote Armor Repairer II
        Small Remote Armor Repairer II

        Medium Auxiliary Nano Pump I
        Medium Auxiliary Nano Pump II
        Medium Nanobot Accelerator II

        Imperial Navy Infiltrator x5

        Occult M x500
        Mystic M x500
        Navy Cap Booster 800 x10
    """, language="markdown")
with st.expander("DPS Kikimora"):
    st.write("This is the main destroyer and DPS for this doctrine, with remote repair capabilities and high speed.")
    st.caption("Fleet Kikimora - 150M ISK")
    st.code("""
        [Kikimora, DPS Kikimora]
        Damage Control II
        Entropic Radiation Sink II
        Entropic Radiation Sink II
        Small Ancillary Armor Repairer

        5MN Y-T8 Compact Microwarpdrive
        Small F-RX Compact Capacitor Booster
        Warp Disruptor II

        Veles Light Entropic Disintegrator
        Small Energy Neutralizer II

        Small Transverse Bulkhead II
        Small Transverse Bulkhead II
        Small Transverse Bulkhead II

        Nanite Repair Paste x120
        Occult S x500
        Navy Cap Booster 400 x10
        Mystic S x500
    """, language="markdown")
st.write("Logi/Ewar Ships")
with st.expander("Logi Rodiva"):
    st.write("The rodiva should stay away from the gunfight as far as possible as it has viturally no tank. Main focus is to remote rep your teammates and dampen the closest enemy in range.")
    st.caption("Logi Rodiva - 160M ISK")
    st.code("""
        [Rodiva, Logi Rodiva]
        Reactive Armor Hardener
        800mm Steel Plates II
        Multispectrum Energized Membrane II
        Multispectrum Energized Membrane II
        Reactor Control Unit II
        Explosive Energized Membrane II

        Remote Sensor Dampener II
        50MN Quad LiF Restrained Microwarpdrive
        Republic Fleet Medium Cap Battery
        Medium F-RX Compact Capacitor Booster

        Heavy Mutadaptive Remote Armor Repairer II
        Small Energy Neutralizer II
        Small Energy Neutralizer II

        Medium Kinetic Armor Reinforcer I
        Medium Remote Repair Augmentor I
        Medium Trimark Armor Pump I

        Valkyrie II x5
        Warrior II x5
        Hornet EC-300 x5

        Nanite Repair Paste x100
        Scan Resolution Dampening Script x1
        Navy Cap Booster 800 x11
        Targeting Range Dampening Script x1
    """, language="markdown")

st.divider()
st.header("Mosquito Doctrine")
st.caption("This fleet is a sniping doctrine, using the long range of the Jackdaw and speed, hence Mosquito. While kiting can be achieved, it is not recommended.")
st.info("Additional tackle or interdictor ships are recommended to fly with this fleet.")
st.write("Command Links")
with st.expander("Command Jackdaw"):
    st.caption("Command Stork - 175M ISK")
    st.code("""
        [Stork, Mosquitos - Infolinks]
        Damage Control II
        Co-Processor II

        Micro Jump Field Generator
        5MN Quad LiF Restrained Microwarpdrive
        Caldari Navy Medium Shield Extender
        EM Shield Amplifier II
        Initiated Compact Warp Disruptor
        Target Painter II

        Information Command Burst II
        Information Command Burst II
        Information Command Burst II

        Small Command Processor I
        Small Command Processor I

        Sensor Optimization Charge x300
        Electronic Superiority Charge x300
        Electronic Hardening Charge x300
        Information Command Mindlink x1
    """, language="markdown")

st.write("DPS Ships")
with st.expander("DPS"):
    st.caption("Jackdaw - 155M ISK")
    st.info("Swap for T1 as needed")
    st.code("""
        [Jackdaw, *Mosquitos - DPS]
        Nanofiber Internal Structure II
        Ballistic Control System II
        Ballistic Control System II

        5MN Quad LiF Restrained Microwarpdrive
        Missile Guidance Computer II
        Pithum C-Type EM Shield Amplifier
        Phased Muon Scoped Sensor Dampener
        Republic Fleet Medium Shield Extender

        Light Missile Launcher II
        Light Missile Launcher II
        Light Missile Launcher II
        Light Missile Launcher II
        Light Missile Launcher II

        Small Polycarbon Engine Housing I
        Small Hydraulic Bay Thrusters II
        Small Rocket Fuel Cache Partition II

        Scourge Fury Light Missile x795
        Nova Fury Light Missile x795
        Missile Range Script x1
        Inferno Fury Light Missile x795
        Mjolnir Fury Light Missile x795
        Targeting Range Dampening Script x1
        Synth Crash Booster x1
        Agency 'Pyrolancea' DB5 Dose II x1
    """, language="markdown")

st.write("Ewar/Logi Ships")
with st.expander("Painter Hyena"):
    st.caption("Ewar Hyena - 40M ISK")
    st.code("""
        [Hyena, Mosquitos - Paint/web support]
        Damage Control II
        Signal Amplifier II
        Signal Amplifier II

        Stasis Webifier II
        5MN Y-T8 Compact Microwarpdrive
        Medium Shield Extender II
        Target Painter II

        Small Particle Dispersion Projector I
        Small Capacitor Control Circuit I
    """, language="markdown")
with st.expander("ECM Kitsune"):
    st.caption("ECM Kitsune - 90M ISK")
    st.code("""
        [Kitsune, Mosquitos - ECM]
        Signal Distortion Amplifier II
        Signal Distortion Amplifier II

        5MN Quad LiF Restrained Microwarpdrive
        Radar ECM II
        Radar ECM II
        Radar ECM II
        Radar ECM II

        Small Ionic Field Projector II
        Small Low Friction Nozzle Joints II

        Magnetometric ECM II x4
        Gravimetric ECM II x4
        Ladar ECM II x4
        Multispectral ECM II x4
        Mobile Depot
    """, language="markdown")