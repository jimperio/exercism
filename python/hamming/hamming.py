
def distance(strand, other_strand):
  if len(strand) != len(other_strand):
    raise ValueError("Strands must be of equal length!")
  length_left = len(strand)
  distance = 0
  while length_left > 0:
    if strand[length_left - 1] != other_strand[length_left - 1]:
      distance += 1
    length_left -= 1
  return distance
