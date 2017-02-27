
def square_of_sum(N):
  return sum(xrange(N+1)) ** 2

def sum_of_squares(N):
  return sum(map(lambda n: n ** 2, xrange(N+1)))

def difference(N):
  return abs(sum_of_squares(N) - square_of_sum(N))
