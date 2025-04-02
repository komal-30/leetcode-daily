
#Problem Statement : leetcode.com/problems/maximum-value-of-an-ordered-triplet-i/
'''Input: nums = [12,6,1,2,7]
Output: 77
Explanation: The value of the triplet (0, 2, 4) is (nums[0] - nums[2]) * nums[4] = 77.
It can be shown that there are no ordered triplets of indices with a value greater than 77. '''

def maximumTripletValue(nums):
    max_val = 0
    #Iterate from 0 to n-2, as last 2 elements will be j,k
    for i in range(0,len(nums)-2):
        #Iterate from 1 to n-1, as last 1 element will be k
        for j in range(1,len(nums)-1):
            #Iterate from 2 to n,upto last element
            for k in range(2,len(nums)):
                if i<j<k:
                    #For debugging and checking triplets
                    triplet = [nums[i],nums[j],nums[k]]
                    calculated_val = (nums[i] - nums[j]) * nums[k]
                    #Handles the edge case for negative values
                    if calculated_val > max_val:
                        max_val=calculated_val
                    #For debugging and checking triplets
                    print(triplet)
    return max_val
print(maximumTripletValue([1,2,3]))

