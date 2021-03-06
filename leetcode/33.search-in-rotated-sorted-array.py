class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        if nums is None or len(nums) == 0:
            return -1

        start = 0
        end = len(nums) - 1

        while(start + 1 < end):
            mid = start + (end - start) / 2

            if target == nums[mid]:
                return mid

            if nums[mid] < nums[end]:
                if nums[mid] < target and target <= nums[end]:
                    start = mid
                else:
                    end = mid

            elif nums[mid] > nums[end]:
                if nums[end] < target and target < nums[mid]:
                    end = mid
                else:
                    start = mid
            else:
                pass

        if nums[start] == target:
            return start

        if nums[end] == target:
            return end

        return -1
