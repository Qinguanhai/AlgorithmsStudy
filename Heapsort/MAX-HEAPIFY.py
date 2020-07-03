#STATEMENT
#MAX-HEAPIFY
#DATE:2020-7-3
#AUTHOR:QIUSHI HUANG

def MaxHeapify(nums,i):
    left_index = 2*i+1
    right_index = 2*i+2
    temp = i

    if left_index >=len(nums) and right_index>=len(nums):
        return nums
 
    if left_index < len(nums):
        if nums[left_index] > nums[i]:
            temp = left_index
    if right_index < len(nums):
        if nums[right_index] > nums[temp]:
            temp = right_index

    if temp != i:
        temp_ = nums[temp]
        nums[temp] = nums[i]
        nums[i] = temp_

    MidProduct = MaxHeapify(nums,left_index)
    result = MaxHeapify(MidProduct,right_index)
    return result

A = [27,17,3,16,13,10,1,5,7,12,4,8,9,0]
print(MaxHeapify(A,0))



