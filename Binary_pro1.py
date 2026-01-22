arr = [1,22,33,44,55,66]
target = 22

def Binary(arr,target):
    start = 0
    end = len(arr)
    while start <= end:
        mid = start + (end-start) // 2
        
        for i in range(0,len(arr)):
            if arr[mid] == target:
                return True
            elif arr[mid] < target:
                start = mid + 1
            else:
                end = mid - 1

    
    return False
print(Binary(arr,target))
