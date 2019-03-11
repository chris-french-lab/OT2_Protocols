"""
@author MillacuraFA
@date January 8th, 2019
@version 1.1
"""
from opentrons import labware, instruments


def run_custom_protocol(pipette_type: 'StringSelection...'='p300-Single',
    dye_labware_type: 'StringSelection...'='trough-12row'):
    if pipette_type == 'p300-Single':
        tiprack = labware.load('tiprack-200ul', '1')
        pipette = instruments.P300_Single(
            mount='left',
            tip_racks=[tiprack])
    elif pipette_type == 'p50-Single':
        tiprack = labware.load('tiprack-200ul', '1')
        pipette = instruments.P50_Single(
            mount='left',
            tip_racks=[tiprack])
    elif pipette_type == 'p10-Single':
        tiprack = labware.load('tiprack-10ul', '1')
        pipette = instruments.P10_Single(
            mount='left',
            tip_racks=[tiprack])

    if dye_labware_type == 'trough-12row':
        dye_container = labware.load('trough-12row', '2')
    else:
        dye_container = labware.load('tube-rack-2ml', '2')

    output = labware.load('96-flat', '3')
    # Well Location set-up
    dye1_wells = ['B2']

    dye2_wells = ['A1','A2','A3','A4','A5','A6','A7','A8','A9','A10','A11','A12'
				 'B1','B6','B7', 'B12',
				  'C1','C3','C4','C5','C6','C7', 'C9', 'C10','C11','C12'
				 'D1','D3','D4','D5','D6','D7','D12',
				  'E1', 'E3', 'E4','E4','E5','E6','E7','E9','E10','E11','E12'
				  'F1','F3','F4','F5','F6','F7','F9','F10','F11','F12'
				  'G1','G6','G7','G9','G10','G11','G12'
				  'H1','H2','H3','H4','H5','H6','H7','H8','H9','H10','H11','H12'
				 ]

    dye2 = dye_container.wells('A1')
    dye1 = dye_container.wells('A2')

    pipette.distribute(
        15,
        dye1,
        output.wells(dye1_wells),
        new_tip='once')
    pipette.distribute(
        15,
        dye2,
        output.wells(dye2_wells),
        new_tip='once')


run_custom_protocol(**{'pipette_type': 'p10-Single', 'dye_labware_type': 'tube-rack-2ml'})
