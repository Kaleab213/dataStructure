class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def newfunc(left, right):
            if left < right:
                s[left], s[right] = s[right], s[left]
                newfunc(left + 1, right - 1)
        newfunc(0, len(s) - 1)
