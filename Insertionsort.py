import time
def insertion_sort(data,drawData, speed):
    for j in range(1,len(data)):#to iterate through the elements starting from the second element 
        sorted=data[j] #assigning the data element currently being processed to a temporary variable
        i=j-1 #index of data element before the current one 
        drawData(data, ['yellow' if x == i else 'green' if x <= j else 'grey' for x in range(len(data))]) #turns the data element being processed to a yellow bar while the sorted ones are green
        time.sleep(speed)
        while i >=0 and data[i] > sorted: #loop will loop till 'i'th index is greater than zero and current data at 'i'th index is greater than data stored in sorted variable. 
            data[i+1]=data[i]  #the data present at 'i'th position is assigned to data at 'i+1'th index
            drawData(data,['blue' if x == i  else 'green' if x <= j else 'grey' for x in range(len(data))]) #the data being moved to its correct position turns blue while the data moved turns green
            time.sleep(speed)
            i=i-1
        data[i+1]=sorted  #data assigned to the to temporary variable is now assigned to the data present at 'i+1' index for the next cycle
#Yellow-->specifying the element being worked on
#Blue-->moving the element in yellow to its correct position
#Green-->represent sorted elements




