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
    if x in list2 and x not in list_int:
        list_int.append(x)
    if x not in list_ren:
        list_ren.extend([x])
for x in list2:
    if x not in list_ren:
        list_ren.extend([x])
list_dif1,list_dif2=list1,list2
for x in list_dif2:
    if x in list_dif1:
        list_dif1.remove(x)
for x in list_dif1:
    if x in list_dif2:
        list_dif2.remove(x)
print(list_int)
print(sorted(list_ren))
print(list_dif1)
print(list_dif2)