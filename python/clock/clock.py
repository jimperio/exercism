
class Clock(object):

  def __init__(self, hour, minutes):
    self.hour = self.__validate_hour(hour)
    self.minutes = 0
    self.add(minutes)

  def __str__(self):
    return '%s:%s' % (
      str(self.hour).zfill(2),
      str(self.minutes).zfill(2))

  def __repr__(self):
    return '<Clock %s>' % str(self)

  def __eq__(self, other):
    return (self.hour == other.hour
      and self.minutes == other.minutes)

  def add(self, minutes):
    new_hour = self.hour
    new_minutes = self.minutes + minutes
    while new_minutes >= 60:
      new_minutes -= 60
      new_hour += 1
    while new_minutes < 0:
      new_minutes += 60
      new_hour -= 1
    self.hour = self.__validate_hour(new_hour)
    self.minutes = new_minutes
    return self

  def __validate_hour(self, hour):
    while hour < 0:
      hour += 24
    while hour > 24:
      hour -= 24
    if hour == 24:
      hour = 0
    return hour
