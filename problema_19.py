n,nr_oa=str(input(':')),0
print('a=',len(list(filter(lambda x:x=='a',n))))
print('b=',len(list(filter(lambda x:x=='b',n))))
for x in n:
    if x=='o' and n[n.index(x)+1]=='a':
        nr_oa+=1
print('oa',nr_oa)