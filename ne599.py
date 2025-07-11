#599. Minimum Index Sum of Two Lists. Given two arrays of strings list1 and list2, find the common strings with the least index sum. A common string is a string that appeared in both list1 and list2. A common string with the least index sum is a common string such that if it appeared at list1[i] and list2[j] then i + j should be the minimum value among all the other common strings. Return all the common strings with the least index sum. Return the answer in any order.

class Solution:
    def findRestaurant(self, list1: list[str], list2: list[str]) -> list[str]:
        isum=float('inf')
        res=[]
        l1={}
        l2={}

        for i in range(len(list1)):
            l1[list1[i]]=i
        for i in range(len(list2)):
            l2[list2[i]]=i
        
        for key in l1:
            if key in l2:
                index_sum=l1[key]+l2[key]

                if index_sum<isum:
                    res=[key]
                    isum=index_sum
                elif index_sum==isum:
                    res.append(key)
        return res


solution = Solution()
print(solution.findRestaurant(["Shogun","Tapioca Express","Burger King","KFC"],["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]))