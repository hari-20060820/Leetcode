class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        queue=deque([0])
        visited={0}
        level=0
        while queue:
            level+=1
            for _ in range(len(queue)):
                current=queue.popleft()
                for coin in coins :
                    s=current+coin
                    if s==amount:
                        return level
                    if s < amount and s not in visited:
                        visited.add(s)
                        queue.append(s)
        return -1