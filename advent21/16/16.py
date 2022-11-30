import pprint 
import functools 
from operator import mul
pp = pprint.PrettyPrinter(indent=2)

filename = 'data'

def bit_gen(file):
    while True:
        ch = file.read(1)
        if ch not in ['A','B','C','D','E','F','0','1','2','3','4','5','6','7','8','9']: break
        binary = format(int('0x'+ch,16), '04b')
        for i in range(4):
            yield binary[i]



def parse_packet(bits):
    packet = {}
    
    packet['version'] = int(next(bits) + next(bits) + next(bits),2)
    type_id = int(next(bits) + next(bits) + next(bits),2)
    packet['type'] = type_id
    packet['bit_count'] = 6

    if type_id == 4:
        literal = ''
        while True:
            packet['bit_count'] += 5
            lead_bit = next(bits)
            for i in range(4):
                literal += next(bits)
            if lead_bit == '0': break
        packet['value'] = int(literal,2)
    else:
        length_type = next(bits)
        packet['payload'] = []

        if length_type == '0': 
            packet['bit_count'] += 16
            length = int(''.join([next(bits) for _ in range(15)]),2)
        else: 
            packet['bit_count'] += 12
            length = int(''.join([next(bits) for _ in range(11)]),2)

        packet['len_type'] = length_type
        packet['length'] = length

        values = []
        while length > 0:
            sub_packet = parse_packet(bits)
            packet['bit_count'] += sub_packet['bit_count']
            packet['payload'].append(sub_packet)

            values.append(sub_packet['value'])

            if length_type == '0': length -= sub_packet['bit_count']
            else: length -= 1

        import math
        if type_id == 0: packet['value']=sum(values)
        elif type_id == 1: packet['value']=functools.reduce(mul,values,1)
        elif type_id == 2: packet['value']=min(values)
        elif type_id == 3: packet['value']=max(values)
        elif type_id == 5: packet['value']=1 if values[0] > values[1] else 0
        elif type_id == 6: packet['value']=1 if values[0] < values[1] else 0
        elif type_id == 7: packet['value']=1 if values[0] == values[1] else 0

        
    return packet

with open(filename) as file:
    bits = bit_gen(file)
    packet = parse_packet(bits)
    pp.pprint(packet)

