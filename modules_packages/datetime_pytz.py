import datetime
import pytz
from pprint import pprint

                        # -------------- Dates -------------------

dean_birthday = datetime.date(2017, 5, 30)
# print(specific_date)

today = datetime.date.today()
# print(today)
# print(f'Year: {today.year}, month: {today.month}, day: {today.day}')

tdelta = datetime.timedelta(days=7)
days_of_dean = today - dean_birthday
# print(f'A week ago: {today - tdelta}, a week from today: {today + tdelta}')
# print(f'It\'s been {days_of_dean.days} days since Dean was born!')

                        # -------------- Times -------------------

t = datetime.time(9, 30, 45, 100000)
# print(t)
# print(f'Hours: {t.hour}, minutes: {t.minute}, seconds: {t.second}, microseconds: {t.microsecond}')

                        # --------- Date, Times, Pytz --------------

# All of the above getters and time_delta etc work too

# pprint(pytz.common_timezones)

dt_today = datetime.datetime.today()
# print(f'{dt_today} is the current date/time on this local machine.')

# Could use .utcnow() but this isn't timezone aware. So use .now(tz=pytz.UTC).
# Can pass in any timezone as argument.
dt_utcnow = datetime.datetime.now(tz=pytz.UTC)
# print(f'The current timezone aware UTC time is: {dt_utcnow}.')

current_user_time = dt_utcnow.astimezone(pytz.timezone('US/Pacific'))
# print(f'If I want to store UTC times in a db, I will need this variable: {current_user_time.time()} to display the users preferred time.')

                        # ------------ Formatting -----------------

# https://docs.python.org/3/library/datetime.html

dt_central = datetime.datetime.now(tz=pytz.timezone('US/Central'))
# print(dt_central.strftime('%B %d, %Y'))

dt_str = 'November 28, 2020'
convert_dt_str = datetime.datetime.strptime(dt_str, '%B %d, %Y')
# print(convert_dt_str)