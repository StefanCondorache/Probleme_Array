with open('input.txt','r') as i:
    list1=eval(i.readline())
    list2=eval(i.readline())
list_ren,list_int,list_dif1,list_dif2=[],[],[],[]
for x in list1:
    if type(x)==int:
        continue
    else:
        print('nu este o multime')
        break
for x in list2:
    if type(x)==int:
        continue
    else:
        print('nu este o multime')
        break
for x in list1:
    if x in list2:
        list_int.append(x)
    if x not in list_ren:
        list_ren.extend([x])
for x in list2:
    if x not in list_ren:
        list_ren.extend([x])
list_dif1=list(filter(lambda x:x not in list_int,list1))
list_dif2=list(filter(lambda x:x not in list_int,list2))
print(list_int,'\n',sorted(list_ren))
print(list_dif1)
print(list_dif2)