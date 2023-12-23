import pprint 
import copy 
import os 
pp = pprint.PrettyPrinter(indent=2)


file = open(os.path.dirname(__file__)+'/real.data','r')

#file = open(os.path.dirname(__file__)+'/test2.data','r')
#11687500
#file = open(os.path.dirname(__file__)+'/test.data','r')
#32000000

DEBUG = 0

LOW_PULSE = 0
HIGH_PULSE = 1

low_pulse_count = 0
high_pulse_count = 0

next_tick = []

class Module:
    def __init__(self, name, destinations=''):
        self.name = name
        self.destinations = []
        if destinations:
            self.add_destinations(destinations)
        self.sources = []

    def add_destinations(self, s):
        for d in s.split(', '):
            self.destinations.append(d)

    def add_source(self, s):
        self.sources.append(modules[s])
    
    def bake_destinations(self):
        dest_modules = []
        for d in self.destinations:
            dest_modules.append(modules[d])
        self.destinations = dest_modules

    def fire_pulse(self, pulse):
        global low_pulse_count, high_pulse_count
        for d in self.destinations:
            if pulse == LOW_PULSE:
                low_pulse_count += 1
            else:
                high_pulse_count += 1

            if DEBUG:
                print("firing", self.name, pulse, d.name)
            next_tick.append((d,self.name,pulse))

    def pulse(self, src, type):
        pass

class FlipFlop(Module):
    def __init__(self, name, destinations):
        self.state = 0
        super().__init__(name, destinations)
    
    def pulse(self, src, type):
        if type == LOW_PULSE:
            self.state = (self.state + 1) % 2
            if self.state == 1:
                self.fire_pulse(HIGH_PULSE)
            else:
                self.fire_pulse(LOW_PULSE)

class And(Module):
    def __init__(self, name, destinations):
        self.source_states = {}
        super().__init__(name, destinations)

    def add_source(self, s):
        self.source_states[s] = LOW_PULSE
        super().add_source(s)

    def pulse(self, src, type):
        self.source_states[src] = type
        if sum(self.source_states.values()) == len(self.source_states.values()):
            self.fire_pulse(LOW_PULSE)
        else:
            self.fire_pulse(HIGH_PULSE)

class Broadcast(Module):
    def pulse(self, src, type):
        self.fire_pulse(type)

class NullModule(Module):
    pass

modules = {}
sources = {}

output_list = set()

for line in [l.strip() for l in file]:
    (module, destinations) = line.split(' -> ')
    if module == 'broadcaster':
        broadcaster = Broadcast(module,destinations)
        modules[module] = broadcaster
    else:
        if module[0] == '%':
            modules[module[1:]] = FlipFlop(module[1:], destinations)
        else:
            modules[module[1:]] = And(module[1:], destinations)
        output_list.update(destinations.split(', '))

for o in output_list:
    if o not in modules:
        modules[o] = NullModule(o)

button = Broadcast('button','broadcaster')

modules['button'] = button
# link in the objects that have been built
for m in modules.values():
    m.bake_destinations()
    for d in m.destinations:
        d.add_source(m.name)



DEBUG = 0
pushes = 1000
for i in range(pushes):
    button.fire_pulse(LOW_PULSE)
    while len(next_tick):
        this_tick = copy.copy(next_tick)
        next_tick = []
        for (m, src, type) in this_tick:
            m.pulse(src, type)


    if DEBUG:
        print('==')

print(high_pulse_count*low_pulse_count,low_pulse_count,high_pulse_count)