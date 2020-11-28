from datetime import datetime
import pytz

utc = pytz.utc
all_timezones = pytz.all_timezones

est = pytz.timezone('America/New_York')
print(datetime.now(tz=est))



