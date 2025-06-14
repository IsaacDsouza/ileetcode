#11. Container With Most Water. You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]). Find two lines that together with the x-axis form a container, such that the container contains the most water. Return the maximum amount of water a container can store. Notice that you may not slant the container.

class Solution:
    def maxArea(self, height:list[int])->int:
        l, r = 0, len(height)-1
        max_area = 0

        while l<r:
            w=r-l
            h = min(height[l], height[r])
            max_area= max(max_area, w*h)

            if height[l]<height[r]:
                l+=1
            else:
                r-=1
            
        return max_area
solution=Solution()
print(solution.maxArea([1,8,6,2,5,4,8,3,7]))
print(solution.maxArea([1,1]))
