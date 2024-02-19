class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        x = len(nums2) - 1
        array = []
        while x >= 0:
            value = nums2[x]
            if  value in nums1:
                index1 = nums1.index(value)
                if not array:
                    nums1[index1] = -1
                    array.append(nums2[x])
                else:
                    added = False
                    for i in reversed(array):
                        if i > value:
                            nums1[index1] = i
                            array.append(value)
                            added = True
                            break
                        else:
                            array.pop()
                    if not added:
                        array.append(value)
                        nums1[index1] = -1
            else:
                array.append(value)
            x-=1
        return nums1