with open('input.txt','r') as i:
    list1=eval(i.readline())
    list2=eval(i.readline())
if type(list1)==set and type(list2)==set:
    print(list1 | list2)
    print(list1 & list2)
    print(list1 - list2)
    print(list2 - list1)
