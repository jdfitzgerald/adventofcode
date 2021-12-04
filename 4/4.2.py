import pprint 
pp = pprint.PrettyPrinter(indent=2)

file = open('test','r')
file = open('data','r')

lines = []

v = [[],[],[],[],[]]
cards = []

for lnum,l in enumerate(file):
	l = l.strip()
	if lnum > 1:
		if l=='':

			card = {
				'complete':False,
				'rows':[set(x) for x in lines],
				'cols':[set(x) for x in v]
			}
			cards.append(card)

			lines = []
			v = [[],[],[],[],[]]
		else:
			a = [int(x) for x in l.split()]
			lines.append(a)
			for i in range(5):
				v[i].append(a[i])

	elif lnum==0:
		nums = [int(x) for x in l.split(',')]

card = {
	'complete':False,
	'rows':[set(x) for x in lines],
	'cols':[set(x) for x in v]
}
cards.append(card)


for n in nums:
	for index,card in enumerate(cards):
		if card['complete'] == False:
			bingo = False
			for r in card['rows']:
				r.discard(n)
				if len(r) == 0:
					bingo = True
			for c in card['cols']:
				c.discard(n)
				if len(c) == 0:
					bingo = True
			
			if bingo:
				total = 0
				for r in card['rows']:
					total += sum(r)
				score = total * n
				card['complete'] = True
				print("Card %d completed at %d with score %d"%(index,n,score))

