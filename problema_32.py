with open('input.txt','r') as i:
    list1=eval(i.readline())
    s=int(i.readline())
if len(list1)>=1 and len(list1)<=100:
    sum1,list2,nr=0,[],0
    while sum1<s:
        sum1+=max(list1)
        nr+=1
        list2.append(max(list1))
        list1.remove(max(list1))
print(nr)
print(list2)

    