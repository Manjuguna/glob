xit1 = int(input())
tit = int(xit1/2)
rit = []
for i in range(xit1, tit, -1):
    j = str(i)
    if i + sum([int(kit) for kit in j]) == xit1:
        print(1)
        print(i)
        break
else:
    print(0) 
