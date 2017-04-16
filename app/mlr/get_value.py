import sys 
import os
import re
import json
import time

fout = file('label_value', 'w')

for line in sys.stdin:
    match = re.search('.*Label = .*', line)
    if match:
        _label = match.group().split(' ')[7]
        _value = match.group().split(' ')[10] 
        fout.write(_label + " " + _value + "\n")

fout.close()
