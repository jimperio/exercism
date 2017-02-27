import re
import string
from collections import defaultdict

emoji_pattern = re.compile(
  u"(\ud83d[\ude00-\ude4f])|"  # emoticons
  u"(\ud83c[\udf00-\uffff])|"  # symbols & pictographs (1 of 2)
  u"(\ud83d[\u0000-\uddff])|"  # symbols & pictographs (2 of 2)
  u"(\ud83d[\ude80-\udeff])|"  # transport & map symbols
  u"(\ud83c[\udde0-\uddff])"  # flags (iOS)
  "+", flags=re.UNICODE)

def word_count(phrase):
  # Replace punctuation with spaces.
  phrase = phrase.translate(
    string.maketrans(string.punctuation, ' '*len(string.punctuation)))
  # Replace emoji with spaces.
  # Note that we convert to unicode here, and keep it in unicode, because the
  # test expects unicode (see `test_unicode`).
  phrase = emoji_pattern.sub(' ', unicode(phrase, 'utf-8'))
  phrase = phrase.lower().strip()
  # Split on any whitespace.
  words = phrase.split()
  count_dict = defaultdict(int)
  for word in words:
    count_dict[word] += 1
  return count_dict
