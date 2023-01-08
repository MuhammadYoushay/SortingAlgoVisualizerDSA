import time
def partition(data,low,high,drawData,speed):
    #low is the starting index.
    #high is the ending index.
    i=low-1
    pivot=data[high]
    drawData(data,colorArray(len(data),low,high,i,i))
    time.sleep(speed) #slowing down the speed of the movement of bars.
    for j in range(low,high):
        #Comparing the current element with the pivot element.
        if data[j] <= pivot:
            drawData(data,colorArray(len(data),low,high,i,j,True))
            time.sleep(speed)
            i=i+1
            data[i],data[j]=data[j],data[i]
        drawData(data,colorArray(len(data),low,high,i,j))
        time.sleep(speed)
    #Swapping of pivot
    drawData(data,colorArray(len(data),low,high,i,high,True))
    time.sleep(speed)
    data[i+1],data[high]=data[high],data[i+1]
    return i+1
def quick_sort(data,low,high,drawData,speed):
    #low is the starting index
    #high is the ending index
    if low<high:
        #Recursive calls
        partitionIdx=partition(data,low,high,drawData,speed)
        quick_sort(data, low, partitionIdx-1, drawData, speed)
        quick_sort(data,partitionIdx + 1, high, drawData, speed)

def colorArray(dataLen,low,high,border,currIdx,isSwapping=False):
    colorArray=[]
    for i in range(dataLen):
        if i >= low and i <= high:
            colorArray.append('grey')
        else:
            colorArray.append('white')
        if i == high:
            colorArray[i]='blue'
        if isSwapping:
            if i == border or i == currIdx:
                colorArray[i] = 'green'
    return colorArray
#Blue-->Pivot element
#White-->Represents sorted partitions
#Green-->For Traversal
#Grey-->Unsorted elements
