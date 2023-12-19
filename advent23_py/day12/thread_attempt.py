import re
import pprint 
import cProfile, pstats, io
from pstats import SortKey

from concurrent.futures import ThreadPoolExecutor

pr = cProfile.Profile()
pr.enable()

pp = pprint.PrettyPrinter(indent=2)

char = r"[^.]"
space = r"[^#]"
maybe_spaces = r"[^#]*?"

sum = 0
#file = open('day12/real.data','r')
file = open('day12/test.data','r')


def parse_match(r):
    start = r.span()[0]
    post = '.' + m[start+expected[i]+2:]

    #replaced = match[:(offset + start)].replace('?','.')+'.' + ('#' * expected[i]) + post
    replaced = match[:(offset + start)]+'.' + ('#' * expected[i]) + post

    if fr.match(replaced): 
        return ((offset + start + expected[i] +1 ), replaced)
    else:
        return None

thread_pool = ThreadPoolExecutor(max_workers=16)
for (lnum,line) in enumerate([l.strip() for l in file]):
    factor = 1
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

    full_regex = maybe_spaces + maybe_spaces.join(patterns)
    fr = re.compile(full_regex)

    matches = []
    matches.append((0,search))

    for (i,rex) in enumerate(patterns):
        rex += space
        rex = "(?=(" + rex + "))" # get a start index for possible matches

        rexmaining = maybe_spaces.join(patterns[i:])
        rex = "(?=(" + rexmaining + "))" # get a start index for possible matches

        remaining = maybe_spaces.join(patterns[i+1:]) + r'$'

        new_matches = []
        for (offset,match) in matches:
            m = match[offset:]
            new_matches = thread_pool.map(parse_match, re.finditer(rex, m))
            matches += [m for m in new_matches if m is not None]

    
    sum += len(matches)

    """
    print('  ', search, expected)
    pp.pprint([m for (_,m) in matches])
    print(len(matches))
    print()
    """

thread_pool.shutdown()

print(sum)

p = pstats.Stats(pr)
p.strip_dirs().sort_stats(SortKey.CUMULATIVE).print_stats(15)



