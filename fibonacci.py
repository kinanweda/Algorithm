inputs = int(input('Angka : '))
def fibo(urut) : 
    listData = [1,1]
    for i in range(2,urut): 
        listData.append(listData[i-2] + listData[i-1]) 
    return listData
print(fibo(inputs))
