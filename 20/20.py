import pprint 
pp = pprint.PrettyPrinter(indent=2)


# 5382 guess too high
# 4962 too low

# p2 32028 too high

#file = open('test','r')
file = open('data','r')

algo = next(file).strip()
next(file)

image=[]
for line in file:
	image.append(line.strip())

def pad(image):
	size_y = len(image)+2
	size_x = len(image[0])+2
	empty = '.'*size_x

	result = []
	result.append(empty)
	for line in image: result.append('.'+line+'.')
	result.append(empty)
	return result

def discard_outer(image):
	result = []
	for y in range(1,len(image)-1):
		result.append(image[y][1:-1])
	return result


def enhance(image,algo):
	image = pad(image)
	result = []
	for y in range(1, len(image) -1):
		result.append('')
		for x in range(1, len(image[0]) -1):
			bstr = (image[y-1][x-1:x+2] + image[y][x-1:x+2] + image[y+1][x-1:x+2]).replace('#','1').replace('.','0')
			result[y-1]+=algo[int(bstr,2)]
	
	return result

# initial pad required
iterations = 50
for i in range(iterations):
	image = pad(image)
	image = pad(image)
	image = pad(image)
	image = pad(image)

for i in range(iterations):
	image = enhance(image,algo)
	image = discard_outer(image)



print(sum([line.count('#') for line in image]))
