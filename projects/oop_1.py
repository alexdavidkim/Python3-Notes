from datetime import datetime
import pytz

acct_num_db = [100000]

def generate_account_number():
    acct_num = acct_num_db[-1] + 1
    acct_num_db.append(acct_num)
    return acct_num

class Account:
    
    INT_RATE = 0.02

    def __init__(self, first_name, last_name, pref_time_zone='UTC', balance=0):
        self.first_name = first_name
        self.last_name = last_name
        self.pref_time_zone = pref_time_zone
        self.account_number = generate_account_number()
        self.balance = balance

class TimeZone:

    UTC = pytz.utc

    def get_utc(self):
        return datetime.now(tz=TimeZone.UTC)


# a = Account('elon', 'musk')
# b = Account('lex', 'fridman')

tz = TimeZone()
print(tz.get_utc())