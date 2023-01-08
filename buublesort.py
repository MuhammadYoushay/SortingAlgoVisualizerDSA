import time
def bubble_sort(data,drawData, speed):
    for i in range(len(data)-1): #runs the loop for the total number of elements present within data
        for j in range(len(data)-1-i):
            if data[j] > data[j+1]: #compares the data in the list with the data of next index
                data[j],data[j+1]=data[j+1],data[j] #swaps the data if the data next in line is smaller than data on previous index
                drawData(data,['yellow' if x==j+1 else 'grey' for x in range(len(data))]) #the data element that is about to be swapped will be colored yellow while every other will be grey in the graph.
                time.sleep(speed)
    drawData(data,['green' for x in range(len(data))]) #to draw rest of the data using green bars
