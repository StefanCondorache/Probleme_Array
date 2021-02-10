with open('input.txt','r') as i:
    list1=eval(i.readline())
if len(list1)<100:
    max1=max(list1)
    list1.remove(max1)
    print(max(list1))