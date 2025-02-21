"""
169. Majority Element

Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

Example 1:
Input: nums = [3,2,3]
Output: 3

Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2 

Constraints:
    n == nums.length
    1 <= n <= 5 * 104
    -109 <= nums[i] <= 109

"""

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        numbers_count = {}

        for number in nums:
            if number not in numbers_count.keys():
                numbers_count[number] = 1
            else:
                numbers_count[number] += 1
                
        major_element = list(numbers_count.keys())[0]
        for key in list(numbers_count.keys()):
            if numbers_count[key] > numbers_count[major_element]:
                major_element = key
            
        return major_element