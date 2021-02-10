with open('input.txt','r') as i:
    list1=eval(i.readline())
if len(list1)>=1 and len(list1)<=100:
    n,nrc,nrnec=1,0,0
    while n!=len(list1)-1:
        if list1[n-1:n+2]==sorted(list1[n-1:n+2]):
            nrc+=1
            n+=1
        else:
            nrnec+=1
            n+=1
print('crescatoare=',nrc,'\n','nici crescatoare nici descrescatoare=',nrnec)