with open('input.txt','r') as i:
    list1=eval(i.readline())
if len(list1)>=10 and len(list1)<=100:
    print('III-',list1[2])
    print('IV-',list1[3])
    print('IX-',list1[8])
    print(sum([list1[1],list1[2],list1[8]]))
    list1[0]+=5
    list1[len(list1)-1]+=5
    print(list1)
    if len(list1)%2!=0:
        list1[len(list1)//2]-=10
        print(list1)
    elif len(list1)%2==0:
        list1[len(list1)//2-1]-=10
        list1[len(list1)//2]-=10
        print(list1)
