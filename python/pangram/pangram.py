import string
import unicodedata

def is_pangram(sentence):
  sentence = sentence.lower()
  # Remove accents by normalizing then re-encoding to ASCII.
  sentence = unicode(sentence, 'utf-8')
  normalized_sentence = unicodedata.normalize('NFD', sentence)
  stripped_sentence = normalized_sentence.encode('ascii', 'ignore')
  # Get unique alpha characters.
  letters = set(filter(lambda c: c.isalpha(), stripped_sentence))
  return ''.join(sorted(letters)) == string.ascii_lowercase
