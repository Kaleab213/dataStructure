class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sortedArray = sorted(nums)
        dic = {}
        newArray = []
        for i in range(len(sortedArray)):
            if sortedArray[i] not in dic:
                dic[sortedArray[i]] = i
        for i in range(len(sortedArray)):
            newArray.append(dic[nums[i]])
        return newArray