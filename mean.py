lists = [1,2,3,2,5,2,7,2,3]
def Mean():
    sumdata = 0
    for i in range(len(lists)) :
        a = lists[i-1] + lists[i]
        sumdata += lists[i]
    mean = sumdata / len(lists)
    print(round(mean))

Mean()
