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

    def deposit(self, amount, transaction_type='D'):
        utc_formatted = Account.get_utc().strftime('%m%d%y%H%M%S')
        self._balance += amount
        global total_transactions
        total_transactions += 1
        conf_num = ConfirmationNumber(transaction_type, self.account_number, utc_formatted, total_transactions).get_num()
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

    @classmethod
    def inspect_confirmation_number(cls, num, pref_time_zone='UTC'):
        split = num.split('-')
        transaction_type, account_number, date, transaction_id = split[0], split[1], split[2], split[3]
        conf_num = ConfirmationNumber(transaction_type, account_number, date, transaction_id)
        return conf_num

    def get_utc():
        return datetime.now(tz=pytz.UTC)

    def get_user_time(self):
        user_time = Account.get_utc().astimezone(pytz.timezone(self.pref_time_zone))
        return user_time

class ConfirmationNumber:

    def __init__(self, transaction_type, account_number, date, transaction_id):
        self.transaction_type = transaction_type
        self.account_number = account_number
        self.date = date
        self.transaction_id = transaction_id

    def get_num(self):
        return f'{self.transaction_type}-{self.account_number}-{self.date}-{self.transaction_id}'


user1 = Account('elon', 'musk', pref_time_zone='US/Pacific', balance=100)

# 'W-100001-112920024215-2'

print(user1.deposit(10))