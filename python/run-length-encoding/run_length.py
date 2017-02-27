
def encode(data):
  data = data.strip()
  count = 0
  current_char = None
  compressed = u''
  for char in data:
    if current_char is None:
      current_char = char
    if char == current_char:
      count += 1
    else:
      compressed += '%s%s' % (count if count > 1 else '', current_char)
      current_char = char
      count = 1
  compressed += '%s%s' % (count if count > 1 else '', current_char)
  return compressed

def alt_encode(data):
  # XXX: This is an attempt to only construct/append to the compressed string
  # at one point in the code. It doesn't seem like an improvement over the
  # simpler solution above...
  data = data.strip()
  compressed = u''
  char_counts = []
  for char in data:
    if len(char_counts) == 0:
      char_counts.append([char, 0])
    curr_char, curr_count = char_counts[-1]
    if char == char_counts[-1][0]:
      char_counts[-1][1] += 1
    else:
      char_counts.append([char, 1])
  compressed = ''.join(
    map(lambda c: '%s%s' % (c[1] if c[1] > 1 else '', c[0]), char_counts))
  return compressed

def decode(compressed):
  compressed = compressed.strip()
  count_string = ''
  data = ''
  for char in compressed:
    if char.isdigit():
      count_string += char
    else:
      count = int(count_string) if count_string else 1
      data += char * count
      count_string = ''
  return data
