def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        result = []
        # if(len(nums))
        for index, number in enumerate(nums):
            if(index>0 and number == nums[index-1]):
                continue
            
            i, j = index+1, len(nums)-1
            print(i,j, number)
            while(i<j):
                
                if(number + nums[i]+nums[j] > 0):
                    j=j-1
                elif(number + nums[i]+nums[j]<0):
                    i=i+1
                else:
                    result.append([number, nums[i], nums[j]])
                    i = i+1
                    while(nums[i] == nums[i-1] and i<j):
                        i = i+1
        
        return result