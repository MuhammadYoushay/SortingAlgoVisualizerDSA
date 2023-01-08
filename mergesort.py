import time
def merge_sort(arr, left, right,drawData,speed):
    N=len(arr) #the number of elements present in the array
    if left < right: #the left index is compared with the right index
        m = (left + right) // 2 #mid is assigned to divide the data into two halves
        merge_sort(arr, left, m,drawData,speed) #recursive call on the left half of the list
        merge_sort(arr, m + 1, right,drawData,speed) #recursive call on the right half of the list
        j = m + 1
        if arr[m] <= arr[m + 1]: #if list is already sorted it is returned
            return
        while left <= m and j <= right: #loops keep running while the left index is lower than than mid part and mid is lower than right index
            drawData(arr, ['yellow' if x == left or x == j else 'grey' for x in range(N)]) #the current data being processed turns yellow while everything else in the data remains grey
            time.sleep(speed)
            if arr[left] <= arr[j]: #condition to check if left element is less than element at 'm+1' index
                left += 1
            else:
                drawData(arr, ['blue' if x == left or x == j else 'grey' for x in range(N)])#the data being moves turns blue
                time.sleep(speed)
                temp = arr[j] #temporary variable is assigned with the value of the data present at 'j' index
                i = j
                while i != left:
                    arr[i] = arr[i - 1]
                    drawData(arr, ['blue' if x == i or x ==j else 'grey' for x in range(N)]) #data being moved turns blue 
                    time.sleep(speed)
                    i -= 1
                arr[left] = temp #new values are assigned to the left, right and mid 
                left += 1
                m += 1
                j += 1
#Yellow--> When comparison is being performed.
#Blue--> When an element is being moved to its correct position.