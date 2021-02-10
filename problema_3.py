with open('input.txt','r') as i:
    list1=eval(i.readline())
if len(list1)>=1 and len(list1)<=100:
    nrn=0
    nrp=0
    nr0=0
    nr35=0
    nr7911=0
    nrabs=0
    for x in list1:
        if x<0:
            nrn+=1
        if x%2==0:
            nrp+=1
        if x!=0:
            nr0+=1
        if x>0 and (x%3==0 and x%5==0):
            nr35+=1
        if x%7==0 or x%9==0 or x%11==0:
            nr7911+=1
        if abs(x)>3:
            nrabs+=1
print(nrn,nrp,nr0,nr35,nr7911,nrabs)

