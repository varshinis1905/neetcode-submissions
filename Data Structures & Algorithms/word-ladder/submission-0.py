class Solution:
  def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
    wordSet = set(wordList)
    if endWord not in wordSet:
      return 0

    ans = 0
    q = deque([beginWord])

    while q:
      ans += 1
      for _ in range(len(q)):
        curr_word_chars = list(q.popleft())
        for i, cache in enumerate(curr_word_chars):
          for c in 'abcdefghijklmnopqrstuvwxyz':
            curr_word_chars[i] = c
            word = ''.join(curr_word_chars)
            if word == endWord:
              return ans + 1
            if word in wordSet:
              q.append(word)
              wordSet.remove(word)
          curr_word_chars[i] = cache

    return 0