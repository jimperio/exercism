
def detect_anagrams(target, candidates):
  return [word for word in candidates if is_anagram(target, word)]

def is_anagram(target, word):
  target = target.lower()
  word = word.lower()
  return target != word and sorted(target) == sorted(word)
