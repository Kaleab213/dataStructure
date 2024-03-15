class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.persons = persons
        self.times = times
        self.winner = {}
        counter = {}
        max_count = 0
        max_p = None
        for i in range(len(self.times)):
            p = persons[i]
            counter[p] = counter.get(p,0)+1
            if counter[p]>=max_count:
                max_count = counter[p]
                max_p=p
            self.winner[i]=max_p
 
            
        
    def binary_search(self,arr,start,end,target):
        while start<=end:
            mid = (start+end+1)//2
            if arr[mid]==target:
                return mid
            elif arr[mid]<target:
                val = mid
                start = mid+1
            else:
                end = mid-1
        return val

    def q(self, t: int) -> int:
        k = self.binary_search(self.times,0,len(self.times)-1,t)
        return self.winner[k]