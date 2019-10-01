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
p10Rack = labware.load('opentrons_96_filtertiprack_10ul', slot='2' & '3' & '4')
p200Rack = labware.load('opentrons_96_filtertiprack_200ul', slot='5' & '6')
tubeRack = labware.load(
    'opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap', slot='7' & '8' & '9'
)
trashBox = labware.load('trash-box', slot='12')
pipette10 = instruments.P10_Single(
    mount='left', tip_racks=[p10Rack], trash_container=trashBox)
pipette300 = instruments.P300_Single(mount='right', tip_racks=[
    p200Rack], trash_container=trashBox)


custom_plate_name = 'greiner_384'

labware.create(
    custom_plate_name,
    grid=(24, 16),
    spacing=(4.5, 4.5),
    diameter=(4),
    depth=(5.5),
    volume=(20),
)
greiner380 = labware.load(custom_plate_name, slot='1')
# MMX (6.840 mL) was prepared by hand and split in to 6 tubes (1.14 mL)
tubeOTDBMMx = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6']
#tubeOTDB = ['A1']
#tubeNTPs = ['A2']
#tubeT7RNApol = ['A3']
#tubeDFHBI = ['A4']
tubeWater = ['B1', 'B2', 'B3']
#tubeCFSMG1655 = ['B1']
#tubeCFSCH34 = ['B2']
# metals to be used
tubeCu = ['B4']
tubeAs5 = ['B5']
tubeAs3 = ['B6']
tubeZn = ['C1']
tubePb = ['C2']
tubeNi = ['C3']
tubeCd = ['C4']
tubeHg = ['C5']
# aptamers
tubeAptamerPbr = ['C6']
tubeAptamerMer = ['D1']
tubeAptamerArs = ['D2']
tubeAptamerT7 = ['D3']
tubeAptamerCue = ['D4']
tubeAptamerCnr = ['D5']
tubeAptamerCzc = ['D6']
# MMx no DNA no Metal no
mmx = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6']


#metals = ['B3', 'B4', 'B5', 'B6', 'C1', 'C2', 'C3', 'C4', 'C5']
# transfer water
pipette300.transfer(
    150,
    tubeRack[0].wells(tubeWater),
    tubeRack[1].rows('A', to='D'),
    new_tip='never')
# transfer metals
pipette300.transfer(
    50,
    tubeRack[0].wells('B3', to='C4'),
    tubeRack[1].wells('A1', 'A4', 'B1', 'B4', 'C1', 'C4', 'D1', 'D4'),
    new_tip='always'
)
# dilution of metals
pipette300.mix(4, 100, tubeRack[1].rows('A', to='B'))
pipette300.transfer(
    50,
    tubeRack[1].cols('1', '4'),
    tubeRack[1].cols('2', '5')
)
pipette300.mix(4, 100, tubeRack[1].cols('2', '5'))
pipette300.transfer(50, tubeRack[1].cols('2', '5'), tubeRack[1].cols('3', '6'))
pipette300.mix(4, 100, tubeRack[1].cols('3', '6'))

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

pipette300.distribute(
    18, tubeRack[0].wells.tubeOTDBMMx, greiner380.rows('A', to='O'))
# Adds DNA in proper cols locations
pipette10.distribute(
    1, tubeRack[0].wells.tubeAptamerPbr, greiner380.cols('1', to='3'))

pipette10.distribute(
    1, tubeRack[0].wells.tubeAptamerMer, greiner380.cols('4', to='6'))

pipette10.distribute(
    1, tubeRack[0].wells.tubeAptamerArs, greiner380.cols('7', to='9'))

pipette10.distribute(
    1, tubeRack[0].wells.tubeAptamerT7, greiner380.cols('10', to='12'))

pipette10.distribute(
    1, tubeRack[0].wells.tubeAptamerCue, greiner380.cols('13', to='15'))

pipette10.distribute(
    1, tubeRack[0].wells.tubeAptamerCnr, greiner380.cols('16', to='18'))
pipette10.distribute(
    1, tubeRack[0].wells.tubeAptamerCzc, greiner380.cols('19', to='21'))
pipette10.distribute(
    1, tubeRack[0].wells.tubeWater, greiner380.cols('22', to='24'))

# Adds metals to be used
# Adds Copper dilutions
pipette10.distribute(
    1, tubeRack[1].wells('A1'), greiner380.rows('A'))
pipette10.distribute(
    1, tubeRack[1].wells('A2'), greiner380.rows('B'))
pipette10.distribute(
    1, tubeRack[1].wells('A3'), greiner380.rows('C'))
# Adds As5 dilutions
pipette10.distribute(
    1, tubeRack[1].wells('A4'), greiner380.rows('D'))
pipette10.distribute(
    1, tubeRack[1].wells('A5'), greiner380.rows('E'))
pipette10.distribute(
    1, tubeRack[1].wells('A6'), greiner380.rows('F'))
# Adds As3 dilutions
pipette10.distribute(
    1, tubeRack[1].wells('B1'), greiner380.rows('G'))
pipette10.distribute(
    1, tubeRack[1].wells('B2'), greiner380.rows('H'))
pipette10.distribute(
    1, tubeRack[1].wells('B3'), greiner380.rows('I'))
# Adds Zn dilutions
pipette10.distribute(
    1, tubeRack[1].wells('B4'), greiner380.rows('J'))
pipette10.distribute(
    1, tubeRack[1].wells('B5'), greiner380.rows('K'))
pipette10.distribute(
    1, tubeRack[1].wells('B6'), greiner380.rows('L'))
# Adds Lead dilutions
pipette10.distribute(
    1, tubeRack[1].wells('C1'), greiner380.rows('M'))
pipette10.distribute(
    1, tubeRack[1].wells('C2'), greiner380.rows('N'))
pipette10.distribute(
    1, tubeRack[1].wells('C3'), greiner380.rows('O'))


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
