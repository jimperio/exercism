
def hey(what):
  what = what.strip()
  # Someone shouting a question should totally chill out.
  if what.isupper():
    return 'Whoa, chill out!'
  elif what.endswith('?'):
    return 'Sure.'
  elif what == '':
    return 'Fine. Be that way!'
  else:
    return 'Whatever.'
