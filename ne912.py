#912. Sort an Array. Given an array of integers nums, sort the array in ascending order and return it. You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.

class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        def merge(arr, L, M, R):
            left, right = arr[L:M+1],arr[M+1:R+1]
            i, lp, rp=L,0,0

            while lp<len(left) and rp<len(right):
                if left[lp]<=right[rp]:
                    arr[i]=left[lp]
                    lp+=1
                else:
                    arr[i]=right[rp]
                    rp+=1
                i+=1
            while lp<len(left):
                arr[i]=left[lp]
                lp+=1
                i+=1
            while rp<len(right):
                arr[i]=right[rp]
                rp+=1
                i+=1
        def mergeSort(arr, l, r):
            if l==r:
                return arr
            m=(l+r)//2
            mergeSort(arr,l,m)
            mergeSort(arr,m+1,r)
            merge(arr,l,m,r)
            return arr
        return mergeSort(nums, 0, len(nums)-1)

solution=Solution()
print(solution.sortArray([5,2,3,1]))

