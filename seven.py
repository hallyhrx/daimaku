list1=range(1,101)
for i in list1:
    a=str(i).find('7')
    if int(i)%7==0 or a !=-1:
        print(i)