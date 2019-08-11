lists = [1,2,3,2,5,2,7,2,3,3,3]
def Median():
    sort = sorted(lists)
    half = len(sort)//2
    if len(sort) % 2 == 0:
        median = (sort[half-1] + sort[half]) / 2 
    elif len(sort) % 2 == 1:
        median = sort[half-1]
    print(median)

Median()
