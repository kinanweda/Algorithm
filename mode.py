lists = [1,2,3,2,5,2,7,2,3,3,3]
def Mode():
    sort = sorted(lists) 
    list1 = list(set(sort))
    
    z = []
    for item in range(0,len(list1)):
        cari = list(filter(lambda lists: list1[item] == lists,lists))
        z.append(len(cari))
        
    dictionary = {list1[i]:z for i,z in enumerate(z)}
    filter1 = [item for item in dictionary if dictionary[item] == max(z)]
    print(filter1)
Mode()
