from datetime import datetime
import pytz

# utc = pytz.utc
# all_timezones = pytz.all_timezones

# est = pytz.timezone('America/New_York')
# print(datetime.now(tz=est))


# UTC = datetime.now(tz=pytz.UTC)
# print(UTC.strftime('%m%d%y-%H%M%S'))

class Foo:

    TOTAL_TRANS = 0

    def bar(self):
        Foo.TOTAL_TRANS += 1
        print(Foo.TOTAL_TRANS)

a = Foo()
a.bar()