class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        store = defaultdict(lambda: 0)
        for cpdomain in cpdomains:
            count, cpdomains = cpdomain.split()
            cpdomainlist = cpdomains.split(".")
            for idx in range(len(cpdomainlist)):
                domain = ".".join(cpdomainlist[idx:])
                store[domain]+=int(count)

        res = []
        for domain in store:
            res.append(str(store[domain])+" "+domain)
        return res
