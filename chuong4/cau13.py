def oscillate(start, count):
    value = abs(start)
    for i in range(value,-1,-1):
        if i == 0:
            yield 0
            yield 0
        else: 
            yield -i
            yield i
    for i in range(1,count):
        yield i 
        yield -i

for n in oscillate(-3,5):
    print(n,end=" ")