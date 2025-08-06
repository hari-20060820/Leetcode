class Solution(object):
    def numOfUnplacedFruits(self, fruits, baskets):
        n = len(baskets)
        
        # Segment Tree to store the maximum capacity in a range of baskets.
        # This allows us to quickly find a basket with sufficient capacity.
        segment_tree = [0] * (4 * n)
        
        def build(node, start, end):
            if start == end:
                segment_tree[node] = baskets[start]
                return
            mid = (start + end) // 2
            build(2 * node + 1, start, mid)
            build(2 * node + 2, mid + 1, end)
            segment_tree[node] = max(segment_tree[2 * node + 1], segment_tree[2 * node + 2])

        def update(node, start, end, idx, new_val):
            if start == end:
                segment_tree[node] = new_val
                return
            mid = (start + end) // 2
            if start <= idx <= mid:
                update(2 * node + 1, start, mid, idx, new_val)
            else:
                update(2 * node + 2, mid + 1, end, idx, new_val)
            segment_tree[node] = max(segment_tree[2 * node + 1], segment_tree[2 * node + 2])

        def find_first_fit_index(node, start, end, fruit_size):
            # Base case: we've found the first valid index.
            if start == end:
                return start if segment_tree[node] >= fruit_size else -1
            
            mid = (start + end) // 2
            
            # Check the left child first, as we need the smallest index.
            if segment_tree[2 * node + 1] >= fruit_size:
                result = find_first_fit_index(2 * node + 1, start, mid, fruit_size)
                if result != -1:
                    return result
            
            # If not found in the left, check the right child.
            if segment_tree[2 * node + 2] >= fruit_size:
                return find_first_fit_index(2 * node + 2, mid + 1, end, fruit_size)
            
            return -1

        if n > 0:
            build(0, 0, n - 1)
        
        unplaced = 0
        for fruit_size in fruits:
            if n > 0 and segment_tree[0] >= fruit_size:
                # Find the first basket that can hold the fruit.
                idx = find_first_fit_index(0, 0, n - 1, fruit_size)
                
                if idx != -1:
                    # Place the fruit and update the basket's capacity to 0.
                    # This marks it as "used".
                    update(0, 0, n - 1, idx, 0)
                else:
                    unplaced += 1
            else:
                unplaced += 1
                
        return unplaced