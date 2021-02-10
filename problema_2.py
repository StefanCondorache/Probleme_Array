def prod(x):
    produs=1
    for y in x:
        produs*=y
    return produs
with open('input.txt','r') as i:
    list1=eval(i.readline())
if len(list1)>=1 and len(list1)<=100:
    print(sum(list1))
    print(prod(list1))
