import re
import pprint 
import cProfile, pstats, io
from pstats import SortKey

pr = cProfile.Profile()
pr.enable()

pp = pprint.PrettyPrinter(indent=2)

char = r"[\?#]"
space = r"[^#]"
maybe_spaces = r"[^#]*?"

sum = 0
#file = open('day12/real.data','r')
file = open('day12/test.data','r')



for (lnum,line) in enumerate([l.strip() for l in file]):

    factor = 5
    (search,expected) = line.split(' ')
    print(lnum,search)
    search = "?".join([search]*factor)
    expected = ",".join([expected]*factor)

    expected = [int(x) for x in expected.split(',')]

    search = '.' + search + '.' # pad to ensure there's always a leading and trailing dot

    patterns = []

    total_damaged = 0
    for n in expected:
        total_damaged += n
        patterns.append(space + char + '{' + str(n) + '}')

    full_regex = maybe_spaces.join(patterns)

    matches = []
    matches.append((0,search))

    for (i,rex) in enumerate(patterns):
        rex += space
        rex = "(?=(" + rex + "))" # get a start index for possible matches

        remaining = maybe_spaces.join(patterns[i+1:])

        new_matches = []
        for (offset,match) in matches:
            m = match[offset:]
            for r in re.finditer(rex, m):
                start = r.span()[0]
                post = '.' + m[start+expected[i]+2:]

                replaced = match[:(offset + start)].replace('?','.')+'.' + ('#' * expected[i]) + post

                if (replaced.count('#') <= total_damaged) and re.search(full_regex,replaced): # edge case
                    new_matches.append(((offset + start + expected[i] +1 ), replaced))

            matches = new_matches

    
    sum += len(matches)

    """
    print('  ', search, expected)
    pp.pprint([m for (_,m) in matches])
    print(len(matches))
    print()
    """

print(sum)

p = pstats.Stats(pr)
p.strip_dirs().sort_stats(SortKey.CUMULATIVE).print_stats(20)
