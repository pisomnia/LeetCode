import collections
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        queue=collections.deque()
        queue.append((beginWord,1))
        wordset=set(wordList)
        visited=set()
        while queue:
            word,step=queue.popleft()
            if word==endWord:
                return step
            for i in range(len(word)):
                for char in 'abcdefghijklmnopqrstuvwxyz':
                    newWord=word[:i]+char+word[i+1:]
                    if newWord in wordset and newWord not in visited:
                        queue.append((newWord,step+1))
                        visited.add(newWord)
                        #wordset.remove(newWord)
        return 0
