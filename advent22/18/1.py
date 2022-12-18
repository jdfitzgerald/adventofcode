import pprint 
import os 

pp = pprint.PrettyPrinter(indent=2)

#filename = os.path.dirname(__file__)+'/test'
filename = os.path.dirname(__file__)+'/data'

file = open(filename,'r')

class VoxGrid:
    grid = {}
    kt = "%d,%d,%d"

    def add_point(self,x,y,z):
        k = self.kt % (x,y,z)
        self.grid[k] = 1

    def total_surface_area(self):
        area = 0
        for k in self.grid:
            area += 6-self.num_neighbours(*self.xyz(k))
        return area

    def xyz(self, key):
        return (int(d) for d in key.split(','))

    def num_neighbours(self, x,y,z):
        total = 0
        if self.kt % (x+1,y,z) in self.grid: total += 1
        if self.kt % (x-1,y,z) in self.grid: total += 1
        if self.kt % (x,y+1,z) in self.grid: total += 1
        if self.kt % (x,y-1,z) in self.grid: total += 1
        if self.kt % (x,y,z+1) in self.grid: total += 1
        if self.kt % (x,y,z-1) in self.grid: total += 1
        return total
        
    def exists(self,x,y,z):
        k = "%d,%d,%d" % (x,y,z)
        if k in self.grid:
            return 1
        else:
            return 0

    def print(self):
        pp.pprint(self.grid)

grid = VoxGrid()

for line in [l.strip() for l in file]:
    (x,y,z) = (int(d) for d in line.split(','))
    grid.add_point(x,y,z)
    
grid.print()
print(grid.total_surface_area())