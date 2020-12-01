from datetime import datetime
import pytz

# utc = pytz.utc
# all_timezones = pytz.all_timezones

# est = pytz.timezone('America/New_York')
# print(datetime.now(tz=est))


# UTC = datetime.now(tz=pytz.UTC)
# print(UTC.strftime('%m%d%y-%H%M%S'))

class MyClass:
    def my_method(self, obj):
        print('In my_method of MyClass')
        print(f'Name: {obj.name}')
        print(f'Age: {obj.age}')

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        inst = MyClass()
        inst.my_method(self)

# a = Person('Elon', 44)
# a.display()


acct_num_db = [100000]
total_transactions = 0

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
        self._account_number = generate_account_number()
        self._balance = balance

    @property
    def balance(self):
        if self._balance < 0:
            raise ValueError('Balance must be positive.')
        return self._balance

    @property
    def account_number(self):
        return self._account_number

    def deposit(self, amount, transaction_type='D'):
        utc_formatted = Account.get_utc().strftime('%m%d%y%H%M%S')
        self._balance += amount
        global total_transactions
        total_transactions += 1
        conf_num = ConfirmationNumber(transaction_type, self.account_number, utc_formatted, total_transactions).get_num()
        return f'Deposit complete, new balance: {self._balance}. Confirmation number: {conf_num}.'

    def withdraw(self, amount):
        utc_formatted = Account.get_utc().strftime('%m%d%y%H%M%S')
        global total_transactions
        total_transactions += 1
        if (self._balance - amount) < 0:
            conf_num = ConfirmationNumber('X', self.account_number, utc_formatted, total_transactions).get_num()
            raise ValueError(f'Transaction declined. You can not withdraw more than {self._balance}. Please try again. Confirmation number: {conf_num}.')
        self._balance -= amount
        conf_num = conf_num = ConfirmationNumber('W', self.account_number, utc_formatted, total_transactions).get_num()
        return f'Withdraw complete, new balance: {self._balance}. Confirmation number: {conf_num}.'

    def add_interest(self):
        accrued_interest = self._balance * (1 * Account.INT_RATE)
        return self.deposit(accrued_interest, transaction_type='I')

    @classmethod
    def inspect_conf_num(cls, num, pref_time_zone='UTC'):
        split = num.split('-')
        transaction_type, account_number, time, transaction_id = split[0], split[1], split[2], split[3]
        conf_num = ConfirmationNumber(transaction_type, account_number, time, transaction_id, pref_time_zone)
        return conf_num

    def get_utc():
        return datetime.now(tz=pytz.UTC)

    def get_user_time(self):
        user_time = Account.get_utc().astimezone(pytz.timezone(self.pref_time_zone))
        return user_time

class ConfirmationNumber:

    def __init__(self, transaction_type, account_number, time, transaction_id, pref_time_zone='UTC'):
        self.transaction_type = transaction_type
        self.account_number = account_number
        self.time = time
        self.transaction_id = transaction_id
        if pref_time_zone != 'UTC':
            dt_time = datetime.strptime(time, '%m%d%y%H%M%S')
            user_time = dt_time.astimezone(pytz.timezone(pref_time_zone))
            self.user_time = user_time

    def get_num(self):
        return f'{self.transaction_type}-{self.account_number}-{self.time}-{self.transaction_id}'

    


user1 = Account('elon', 'musk', pref_time_zone='US/Pacific', balance=100)

# 'W-100001-112920024215-2'

conf_num = user1.inspect_conf_num('W-100001-113020004935-2', 'US/Central')
print(conf_num.transaction_type)
print(conf_num.account_number)
print(conf_num.time)
print(conf_num.transaction_id)
print(conf_num.user_time)