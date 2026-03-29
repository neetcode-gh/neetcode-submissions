class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        for n in nums:
            if n not in seen:
                seen[n] = 0
            seen[n] += 1
        
        top_k_vals = sorted([(seen[k], k) for k in seen], reverse=True)[:k]
        top_k = [e[1] for e in top_k_vals]
        # sorted by add to dict
        by_add = []
        for k in seen:
            if k in top_k:
                by_add.append(k)
        return by_add