list1,list_pos,list_max = [],[],[]
with open('input.txt','r') as i:
    list1=eval(i.readline())
if len(list1)>=1 and len(list1)<=100:
    for x in list1:
        list_pos.append(list1.count(x))
    max1=max(list_pos)
for x in list1:
    if list1.count(x)==max1 and not(x in list_max):
        list_max.append(x)
for x in list_max:
    print('numere',x)