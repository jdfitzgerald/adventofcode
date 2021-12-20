import pprint 
pp = pprint.PrettyPrinter(indent=2)


# 5382 guess too high
# 4962 too low

#file = open('test','r')
file = open('data','r')

algo = next(file).strip().replace('#','1').replace('.','0')
next(file)

image=[]
for line in file:
	image.append(line.strip().replace('#','1').replace('.','0'))

def pad(image):
	size_y = len(image)+2
	size_x = len(image[0])+2
	empty = '0'*size_x

	result = []
	result.append(empty)
	for line in image: result.append('0'+line+'0')
	result.append(empty)
	return result

def enhance(image,algo):
	image = pad(image)
	result = image.copy()
	for y in range(1, len(image) -1):
		result[y] = '0'
		for x in range(1, len(image[0]) -1):
			bstr = image[y-1][x-1:x+2] + image[y][x-1:x+2] + image[y+1][x-1:x+2] 
			result[y]+=algo[int(bstr,2)]
		result[y] += '0'
	return result

# initial pad required
image = pad(image)

for line in image: print(line,sum([int(c) for c in line]))
	
image = enhance(image,algo)

for line in image: print(line,sum([int(c) for c in line]))
	
image = enhance(image,algo)

for line in image: print(line,sum([int(c) for c in line]))
	

print(sum([int(c) for line in image for c in line]))
