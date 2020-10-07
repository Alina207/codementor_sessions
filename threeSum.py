class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # we have to check if there are 3 elements whose sum = 0
        # a+b+c = 0
        # [-1,0,1,2,-1,-4] = [[-1,0,1][-1,-1,2]]
        n = len(nums)
        if n < 3:
            return []
            
        res = set()  # final result
        nums.sort()  # sort the array in ascending order
        # print("nums: ", nums) # [-4,-1,-1,0,1,2,4]   (-4,-1,4) => -4+(-1)+4 = -4-1+4 = -1
                              
        for i in range(n-2):
            l = i+1
            r = n-1
            
            while l<r:
                total = nums[i] + nums[l] + nums[r]
                if total == 0:
                    triplet = (nums[i], nums[l], nums[r])
                   if triplet not in res:
                        res.add(triplet)
                        # print("res: ", res)
                elif total < 0:
                    l+=1
                elif total > 0:
                    r-=1
                l+=1
                r-=1
        return res
    
    
 
