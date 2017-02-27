from datetime import date

class MeetupDayException(Exception):
  pass

days =\
  ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

def meetup_day(year, month, day, ordinal):
  first_of_month_day = date(year, month, 1).weekday()
  first_date_of_day = (days.index(day) - first_of_month_day) % 7 + 1
  remaining_weeks = (days_in_month(month, year) - first_date_of_day) / 7
  if ordinal == 'last':
    weeks_to_go = remaining_weeks
  elif ordinal == 'teenth':
    if first_date_of_day >= 6:
      weeks_to_go = 1
    else:
      weeks_to_go = 2
  else:
    weeks_to_go = int(ordinal[0]) - 1
    if weeks_to_go > remaining_weeks:
      raise MeetupDayException
  return date(year, month, first_date_of_day + weeks_to_go * 7)

def days_in_month(month, year):
  if month == 2:
    if is_leap_year(year):
      return 29
    else:
      return 28
  elif month in (4, 6, 9, 11):
    return 30
  else:
    return 31

def is_leap_year(year):
  if year % 100 == 0:
    return year % 400 == 0
  else:
    return year % 4 == 0
