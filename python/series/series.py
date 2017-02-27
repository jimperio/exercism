
def slices(digits, length):
  if length == 0:
    raise ValueError("Slices cannot be empty!")
  if length > len(digits):
    raise ValueError("Slices cannot be longer than the source!")
  start_index = 0
  slices = []
  while start_index <= (len(digits) - length):
    slices.append(digits[start_index:start_index+length])
    start_index += 1
  return [[int(d) for d in digit_slice] for digit_slice in slices]
