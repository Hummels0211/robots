#!/usr/bin/env python

# TODO: Replace this with a module that computes buffer recipes automatically.
filename = 'citric-phosphate.txt'
infile = open(filename, 'r')
lines = infile.readlines()
infile.close()
conditions = list()
for line in lines:
    # ignore comments
    if line[0] == '#': continue

    # processs data
    elements = line.split()
    entry = dict()
    entry['pH'] = float(elements[0])
    entry['citric acid'] = float(elements[1])
    entry['sodium phosphate'] = float(elements[2])

    # Adjust for 0.1M sodium phosphate.
    entry['sodium phosphate'] *= 2
    total = entry['citric acid'] + entry['sodium phosphate'] 
    entry['citric acid'] /= total
    entry['sodium phosphate'] /= total

    # Store entry.
    conditions.append(entry)

def aspirate(RackLabel, RackType, position, volume, tipmask):
    return 'A;%s;;%s;%d;;%f;;;%d\r\n' % (RackLabel, RackType, position, volume, tipmask)

def dispense(RackLabel, RackType, position, volume, tipmask):
    return 'D;%s;;%s;%d;;%f;;;%d\r\n' % (RackLabel, RackType, position, volume, tipmask)

def washtips():
    return 'W;\r\n' # queue wash tips

assay_volume = 100.0 # assay volume (uL)
compound_volume = 5.0 # compound volume (uL)
buffer_volume = assay_volume - compound_volume
assay_RackType = 'Corning 3651'

# Build worklist.
worklist = ""
for (condition_index, condition) in enumerate(conditions):
    print "pH : %8.1f" % condition['pH']

    # destination well of assay plate
    destination_position = condition_index + 1

    # compound
    volume = compound_volume
    worklist += aspirate('Compound Plate', '4x3 Vial Holder', 1, volume, 1)
    worklist += dispense('Assay Plate', assay_RackType, destination_position, volume, 1)
    worklist += washtips()

    # citric acid
    volume = condition['citric acid']*buffer_volume
    worklist += aspirate('Citric Acid', 'Trough 100ml', 2, volume, 2)
    worklist += dispense('Assay Plate', assay_RackType, destination_position, volume, 2)
    worklist += washtips()
    
    # sodium phosphate
    volume = condition['sodium phosphate']*buffer_volume
    worklist += aspirate('Sodium Phosphate', 'Trough 100ml', 3, volume, 4)
    worklist += dispense('Assay Plate', assay_RackType, destination_position, volume, 4)
    worklist += washtips()
    

# Write worklist.
worklist_filename = 'ph-worklist.gwl'
outfile = open(worklist_filename, 'w')
outfile.write(worklist)
outfile.close()
