
class Allergies(object):

  allergens = {
    1: 'eggs',
    2: 'peanuts',
    4: 'shellfish',
    8: 'strawberries',
    16: 'tomatoes',
    32: 'chocolate',
    64: 'pollen',
    128: 'cats'
  }

  def __init__(self, score):
    self.lst = []
    for value, allergen in self.allergens.iteritems():
      if score & value == value:
        self.lst.append(allergen)

  def is_allergic_to(self, allergen):
    return allergen in self.lst
