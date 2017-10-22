def crowded_cows(cowlist,k):
    cowdict = {}
    cowdictnum = {}
    maxid = -1
    for i in range(len(cowlist)):
        if cowdict.get(cowlist[i]) is None:
            cowdict[cowlist[i]] = i
           else:
               if i - cowdict[cowlist[i]] <= k:
                   maxid = max(maxid,cowlist(i))
               else:
                   cowdict[cowlist[i]] = i
    return (maxid)
cowlist = [7,3,4,2,3,4]
k = 3
a = crowded_cows(cowlist,k)
print(a)