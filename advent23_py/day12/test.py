from concurrent.futures import ThreadPoolExecutor

def square(n):
    return n * n

ook = ThreadPoolExecutor(max_workers=2)
results = ook.map(square, range(4))
print(list(results))

for r in results:
    print(r)