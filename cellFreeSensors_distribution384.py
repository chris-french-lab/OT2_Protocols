"""
@author MillacuraFA
@date September 30th, 2019
@version 1.0
"""
from opentrons import labware, instruments, robot

metadata = {
    'protocolName': 'CellFreeSensorProtocol',
    'author': 'MillacuraFA',
    'source': 'ChrisFrenchLab',
}

#tip_slots = ['4','7']
#for slot in tip_slots
#p10_tip_racks = [labware.load('opentrons_96_tiprack_10ul', slot) ]

    

p10Rack = labware.load('opentrons_96_tiprack_10ul', '4')
p10Rack = labware.load('opentrons_96_tiprack_10ul', '5')
p10Rack = labware.load('opentrons_96_tiprack_10ul', '6')
p10Rack = labware.load('opentrons_96_tiprack_10ul', '7')
p10Rack = labware.load('opentrons_96_tiprack_10ul', '8')
p10Rack = labware.load('opentrons_96_tiprack_10ul', '9')
p10Rack = labware.load('opentrons_96_tiprack_10ul', '10')
p10Rack = labware.load('opentrons_96_tiprack_10ul', '11')

#y = ['5', '6', '7', '8', '11']
#p200Rack = [labware.load('opentrons_96_tiprack_300ul', slot200Rack) for slot200Rack in y]
#p200Rack = labware.load('opentrons_96_tiprack_300ul', '10')
#p200Rack = labware.load('opentrons_96_tiprack_300ul', '11')


tubeRack7 = labware.load(
    'opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap', slot='2'
)
tubeRack8 = labware.load(
    'opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap', slot='3'
)
#tubeRack9 = labware.load(
#    'opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap', slot='11'
#)
#trashBox = labware.load('trash-box', slot='12')
pipette10 = instruments.P10_Single(
    mount='left', tip_racks=[p10Rack]#, trash_container=trashBox
    )
pipette300 = instruments.P300_Single(mount='right', #tip_racks=[p200Rack]#, trash_container=trashBox
    )
#Defining 384 well plate

custom_plate_name = 'greiner_384'

if custom_plate_name not in labware.list():
    labware.create(
        custom_plate_name,
        grid=(24, 16),
        spacing=(4.5, 4.5),
        diameter=4,
        depth=5.5,
        volume=20)

greiner380 = labware.load(custom_plate_name, slot='1')
# MMX (6.840 mL) was prepared by hand and split in to 6 tubes (1.14 mL)
tubeOTDBMMx = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6']
#tubeOTDB = ['A1']
#tubeNTPs = ['A2']
#tubeT7RNApol = ['A3']
#tubeDFHBI = ['A4']
tubeWater = ['B1', 'B2', 'B3', 'B4']
#tubeCFSMG1655 = ['B1']
#tubeCFSCH34 = ['B2']
# metals to be used
#tubeCu = ['B4']
#tubeAs5 = ['B5']
#tubeAs3 = ['B6']
#tubeZn = ['C1']
#tubePb = ['C2']
#tubeNi = ['C3']
#tubeCd = ['C4']
#tubeHg = ['C5']
# aptamers
tubeAptamerPbr = ['C1']
tubeAptamerMer = ['C2']
tubeAptamerArs = ['C3']
tubeAptamerT7 = ['C4']
tubeAptamerCue = ['D1']
tubeAptamerCnr = ['D2']
tubeAptamerCzc = ['D3']
# MMx no DNA no Metal no
#mmx = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6']


#metals = ['B3', 'B4', 'B5', 'B6', 'C1', 'C2', 'C3', 'C4', 'C5']
# transfer water
#pipette300.transfer(
 #   150,
  #  tubeRack7.wells(tubeWater),
   #tubeRack8.rows('A', to='D'),
    #new_tip='always')
# transfer metals
#pipette300.transfer(
 #  50,
  # tubeRack7.wells('B3', 'B4', 'B5', 'B6', 'C1', 'C2', 'C3', 'C4'),
   #tubeRack8.wells('A1', 'A4', 'B1', 'B4', 'C1', 'C4', 'D1', 'D4'),
   #new_tip='always').mix(4)
# dilution of metals

#pipette300.transfer(
 #   50, 
 #   tubeRack8.cols('1', '4'), 
  #  tubeRack8.cols('2', '5')
  #  )
#pipette300.transfer(
 #   50, 
  #  tubeRack8.wells('A1', 'B1', 'C1','D1', 'A4', 'B4', 'C4', 'D4'),
   # tubeRack8.wells('A2', 'B2', 'C2', 'D2', 'A5', 'B5', 'C5', 'D5'),
    #new_tip='always'
   # ).mix(4)
#pipette300.transfer(
 #   50,
  #  tubeRack8.cols('2', '5'),
   # tubeRack8.cols('3', '6'),
    #new_tip='always'
    #).mix(4)
# Preparation of Mastermix can be don by hand, if not just use per rxn:
# OTDB (10X)         2.00 uL
# NTP (20 mM each)   2.00 uL
# T7 RNApol          0.75 uL
# Water              6.75 uL
# CFS                6.00 uL
# Fluorophore (200 uM) 0.5 uL
# # pipette300.distribute()

# pipette10.pick_up_tip()

# Mastermix distribution

pipette10.distribute(
    18,tubeRack7.wells(tubeOTDBMMx), greiner380.rows('A', to='O'))
# Adds DNA in proper cols locations
pipette10.distribute(
    1,tubeRack7.wells(tubeAptamerPbr), greiner380.cols('1', to='3'), new_tip='always')

pipette10.distribute(
    1,tubeRack7.wells(tubeAptamerMer), greiner380.cols('4', to='6'), new_tip='always')

pipette10.distribute(
    1,tubeRack7.wells(tubeAptamerArs), greiner380.cols('7', to='9'), new_tip='always')

pipette10.distribute(
    1,tubeRack7.wells(tubeAptamerT7), greiner380.cols('10', to='12'), new_tip='always')

pipette10.distribute(
    1,tubeRack7.wells(tubeAptamerCue), greiner380.cols('13', to='15'), new_tip='always')

pipette10.distribute(
    1,tubeRack7.wells(tubeAptamerCnr), greiner380.cols('16', to='18'), new_tip='always')
pipette10.distribute(
    1,tubeRack7.wells(tubeAptamerCzc), greiner380.cols('19', to='21'), new_tip='always')
pipette10.distribute(
    1,tubeRack7.wells(tubeWater), greiner380.cols('22', to='24'), new_tip='always')

# Adds metals to be used
# Adds Copper dilutions
pipette10.distribute(
    1,tubeRack8.wells('A1'), greiner380.rows('A'), new_tip='always')
pipette10.distribute(
    1,tubeRack8.wells('A2'), greiner380.rows('B'), new_tip='always')
pipette10.distribute(
    1,tubeRack8.wells('A3'), greiner380.rows('C'), new_tip='always')
# Adds As5 dilutions
pipette10.distribute(
    1,tubeRack8.wells('A4'), greiner380.rows('D'), new_tip='always')
pipette10.distribute(
    1,tubeRack8.wells('A5'), greiner380.rows('E'), new_tip='always')
pipette10.distribute(
    1,tubeRack8.wells('A6'), greiner380.rows('F'), new_tip='always')
# Adds As3 dilutions
pipette10.distribute(
    1,tubeRack8.wells('B1'), greiner380.rows('G'), new_tip='always')
pipette10.distribute(
    1,tubeRack8.wells('B2'), greiner380.rows('H'), new_tip='always')
pipette10.distribute(
    1,tubeRack8.wells('B3'), greiner380.rows('I'), new_tip='always')
# Adds Zn dilutions
pipette10.distribute(
    1,tubeRack8.wells('B4'), greiner380.rows('J'), new_tip='always')
pipette10.distribute(
    1,tubeRack8.wells('B5'), greiner380.rows('K'), new_tip='always')
pipette10.distribute(
    1,tubeRack8.wells('B6'), greiner380.rows('L'), new_tip='always')
# Adds Lead dilutions
pipette10.distribute(
    1,tubeRack8.wells('C1'), greiner380.rows('M'), new_tip='always')
pipette10.distribute(
    1,tubeRack8.wells('C2'), greiner380.rows('N'), new_tip='always')
pipette10.distribute(
    1,tubeRack8.wells('C3'), greiner380.rows('O'), new_tip='always')


#tubeCu = ['B4']
#tubeAs5 = ['B5']
#tubeAs3 = ['B6']
#tubeZn = ['C1']
#tubePb = ['C2']
#tubeNi = ['C3']
#tubeCd = ['C4']
#tubeHg = ['C5']
# aptamers
#tubeAptamerPbr = ['C6']
#tubeAptamerMer = ['D1']
#tubeAptamerArs = ['D2']
#tubeAptamerT7 = ['D3']
#tubeAptamerCue = ['D4']
#tubeAptamerCnr = ['D5']
#tubeAptamerCzc = ['D6']
