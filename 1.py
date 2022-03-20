 # 两数之和
 # n^2 时间的双层循环，或者用 map 记录

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashtable = dict()
        for index,value in enumerate(nums):
            if target - value in hashtable:     # O(1) find target - value
                return [index, hashtable[target-value]]
            else:
                hashtable[value] = index
            
        return []