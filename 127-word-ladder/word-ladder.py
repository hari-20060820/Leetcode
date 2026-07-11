class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        wordSet=set(wordList)
        if endWord not in wordSet:
            return 0
        queue=deque()
        queue.append((beginWord,1))
        while queue:
            size=len(queue)
            
            word,level =queue.popleft()
            if word == endWord:
                    return level
            for i in range(len(word)):
                for ch in "abcdefghijklmnopqrstuvwxyz":
                    newWord=word[:i]+ch+word[i+1:]
                    
                    if newWord in wordSet:
                        wordSet.remove(newWord)
                        queue.append((newWord,level+1))
        return 0

"""**Algorithm (Short Steps)**

1. Convert `wordList` into a `set` for **O(1)** lookup.
2. If `endWord` is not in the set, return `0`.
3. Create a **queue** and push `(beginWord, 1)`.
4. While the queue is not empty:

   * Pop the front word and its level.
   * If the word is `endWord`, return the level.
   * For each character position in the word:

     * Replace it with every letter from `'a'` to `'z'`.
     * If the new word exists in the set:

       * Push `(newWord, level + 1)` into the queue.
       * Remove it from the set (mark as visited).
5. If the queue becomes empty without finding `endWord`, return `0`.
""" 