def arrayRankTransform(arr):
    rank = {}
    for i in sorted(arr):
        rank.setd(i,len(rank)+1)
    return map(rank.get,arr)


arr=[40,10,20,30]
ans=arrayRankTransform(arr)
for i in ans:
    print(i)
