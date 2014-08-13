#!/usr/bin/python
#fun tool to calculate a given colony's requirements

import sys

b={'resi': {'name':'Resiblocks',     'power':2,  'support':150,  'cost':3000, 'num':0},
   'life': {'name':'Life Support',   'power':2,  'support':500,  'cost':13000,'num':0},
   'water':{'name':'Hydration Plant','power':1,  'support':500,  'cost':5000, 'num':0},
   'food': {'name':'Hydroponics',    'power':2,  'support':400,  'cost':7000, 'num':0},
   'med':  {'name':'Medical Centre', 'power':1,  'support':100,  'cost':5000, 'num':0},
   'sec':  {'name':'Security Centre','power':2,  'support':100,  'cost':4500, 'num':0},
   'pow':  {'name':'Solar Matrix',   'power':16, 'support':99999,'cost':5000, 'num':0},
   }

IGNORE_MED = True
IGNORE_SEC = True

####


####
pop = int(sys.argv[1])

# buildings required
b['resi']['num']  = 1 + ((pop-1) / b['resi']['support'])
b['life']['num']  = 1 + ((pop-1) / b['life']['support'])
b['water']['num'] = 1 + ((pop-1) / b['water']['support'])
b['food']['num']  = 1 + ((pop-1) / b['food']['support'])
if pop > 50:
  b['med']['num']   = ((pop-50) / b['med']['support'])
  b['sec']['num']   = ((pop-50) / b['sec']['support'])


if IGNORE_MED:
  b['med']['num'] = 0
if IGNORE_SEC:
  b['sec']['num'] = 0

# power required
power_required = 0
power_required += b['resi']['num'] * b['resi']['power']
power_required += b['life']['num'] * b['life']['power']
power_required += b['water']['num'] * b['water']['power']
power_required += b['food']['num'] * b['food']['power']
power_required += b['med']['num'] * b['med']['power']
power_required += b['sec']['num'] * b['sec']['power']

b['pow']['num'] = 1 + ((power_required-1) / b['pow']['power'])

total_buildings = 0
total_buildings += b['resi']['num']
total_buildings += b['life']['num']
total_buildings += b['water']['num']
total_buildings += b['food']['num']
total_buildings += b['med']['num']
total_buildings += b['sec']['num']
total_buildings += b['pow']['num']

total_cost = 0
total_cost += b['resi']['num'] * b['resi']['cost']
total_cost += b['life']['num'] * b['life']['cost']
total_cost += b['water']['num'] * b['water']['cost']
total_cost += b['food']['num'] * b['food']['cost']
total_cost += b['med']['num'] * b['med']['cost']
total_cost += b['sec']['num'] * b['sec']['cost']
total_cost += b['pow']['num'] * b['pow']['cost']

print "A colony of %d population requires %d buildings:" % (pop, total_buildings)
for n in ['resi','life','water','food','med','sec','pow']:
  print "%d %s" % (b[n]['num'], b[n]['name'])
print "at a total cost of %d CR and earning %d/day." % (total_cost, 100+(2*pop))
