import random

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort(reverse=True)
        return nums[k-1]
        
    #     return self._quick_sort(nums, 0, len(nums)-1, k-1)

    # def _quick_sort(self, li, first, last, k):
    #     if first < last:
    #         pivot = self._get_pivot(li, first, last)
    #         if pivot == k:
    #             return li[pivot]
    #         elif pivot > k:
    #             return self._quick_sort(li, first, pivot-1, k)
    #         else:
    #             return self._quick_sort(li, pivot+1, last, k)
    #     return li[first]
    
    # def _get_pivot(self, li, first, last):
    #     rand_idx = random.randint(first, last)
    #     li[first], li[rand_idx] = li[rand_idx], li[first]
    #     pivot = li[first]
    #     left, right = first+1, last
    #     while True:
    #         while left <= right and li[left] >= pivot:
    #             left += 1
    #         while left <= right and li[right] <= pivot:
    #             right -= 1
    #         if left > right:
    #             break
    #         li[left], li[right] = li[right], li[left]
    #     li[first], li[right] = li[right], li[first]
    #     return right