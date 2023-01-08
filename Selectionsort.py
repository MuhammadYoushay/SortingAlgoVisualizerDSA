import time
def selection_sort(data,drawData, speed):
    for i in range(len(data)-1): #loops runs for the number of data elements present
        low=i 
        for j in range(i+1,len(data)): #loop runs from the data present at 'i+1' index
            drawData(data, ['yellow' if x == low or x == i else 'green' if x<=i else 'grey' for x in range(len(data))]) #data being traversed turns yellow and the sorted elements turn green
            time.sleep(speed)
            if data[j] < data[low]:#condition to check whether the data in current loop is less than being processed by the previous loop
                drawData(data, ['blue' if x == j or x==low else 'green' if x <= i else 'grey' for x in range(len(data))])
                time.sleep(speed)
                low=j
        if low !=i:
            data[i], data[low] = data[low], data[i] #data is swapped
            drawData(data,['white' if x == low or x == i else 'green' if x <= i else 'grey' for x in range(len(data))]) 
            time.sleep(speed)
#Yellow-->For traversing bw elements....b/w low and the next smallest
#Blue--> For moving the element until the correct element is found
#White-->When swapping two elements
#Green-->For sorted elements