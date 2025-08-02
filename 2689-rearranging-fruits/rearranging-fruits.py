from collections import Counter 
class Solution(object):
    def minCost(self, basket1, basket2):
        """
        :type basket1: List[int]
        :type basket2: List[int]
        :rtype: int
        """
        c1=Counter(basket1)
        c2=Counter(basket2)
        combined=Counter(basket1)+Counter(basket2)
        for fruits in combined.values():
            if(fruits%2 !=0):
                return -1
        half={k:v//2 for k,v in combined.items()}
        ext1=[]
        ext2=[]
        for fruit in combined:
            diff1=c1.get(fruit,0)-half[fruit]
            diff2=c2.get(fruit,0)-half[fruit]
            if(diff1>0):
                ext1.extend([fruit] *diff1)
            if(diff2>0):
                ext2.extend([fruit] *diff2)
        ext1.sort()
        ext2.sort(reverse=True)
        min_b=min(basket1+basket2)
        cost=0
        for a,b in zip(ext1,ext2):
            cost+=min(min(a,b),2*min_b)
        return cost
            