class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        maxw = 0
        while(left < right):
            water = min(height[left], height[right])*(right-left)
            if(water>maxw):
                maxw = water
            if(height[left]<height[right]):
                left = left+1
            else:
                right = right - 1
        
        return maxw

        