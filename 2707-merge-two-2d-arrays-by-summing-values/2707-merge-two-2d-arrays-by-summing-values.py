class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        ans, i, j = [], 0, 0
        while i < len(nums1) and j < len(nums2):
            key1, val1 = nums1[i]
            key2, val2 = nums2[j]
            if key1 == key2:
                ans.append([key1, val1 + val2])
                i += 1
                j += 1
            elif key1 < key2:
                ans.append([key1, val1])
                i += 1
            else:
                ans.append([key2, val2])
                j += 1
        while i < len(nums1):
            ans.append(nums1[i])
            i += 1
        while j < len(nums2):
            ans.append(nums2[j])
            j += 1
        return ans