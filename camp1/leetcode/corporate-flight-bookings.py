class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        ans=[0]*(n+3)
        for i in bookings:ans[i[0]]+=i[2];ans[i[1]+1]-=i[2]
        for j in range(1,n+3):ans[j]+=ans[j-1]
        return ans[1:-2]
        