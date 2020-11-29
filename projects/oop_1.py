print('running oop_1.py')

from datetime import datetime
import pytz

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

    def deposit(self, amount, deposit_type='D'):
        self._balance += amount
        conf_num = self.new_confirmation_number(deposit_type)
        return f'Deposit complete, new balance: {self._balance}. Confirmation number: {conf_num}.'     

    def withdraw(self, amount):
        if (self._balance - amount) < 0:
            conf_num = self.new_confirmation_number('X')
            raise ValueError(f'Transaction declined. You can not withdraw more than {self._balance}. Please try again. Confirmation number: {conf_num}.')
        self._balance -= amount
        conf_num = self.new_confirmation_number('W')
        return f'Withdraw complete, new balance: {self._balance}. Confirmation number: {conf_num}.'

    def add_interest(self):
        accrued_interest = self._balance * (1 * Account.INT_RATE)
        return self.deposit(accrued_interest, 'I')

    def new_confirmation_number(self, transaction_type):
        utc_formatted = Account.get_utc().strftime('%m%d%y-%H%M%S')
        global total_transactions
        total_transactions += 1
        conf_num = f'{transaction_type}-{self.account_number}-{utc_formatted}-{total_transactions}'
        return conf_num

    def inspect_confirmation_number(num):
        split = num.split('-')
        transaction_type, account_number, date, time, transaction_id = split[0], split[1], split[2], split[3], split[4]
        return transaction_type, account_number, date, time, transaction_id

    def get_utc():
        return datetime.now(tz=pytz.UTC)

    def get_user_time(self):
        user_time = Account.get_utc().astimezone(pytz.timezone(self.pref_time_zone))
        return user_time

user1 = Account('elon', 'musk', pref_time_zone='US/Pacific', balance=100)

conf = Account.inspect_confirmation_number('W-100001-112920-024215-2')
print(conf)