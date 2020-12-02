import datetime
import pytz

def get_utc_formatted():
    return datetime.datetime.now(tz=pytz.UTC).strftime('%m%d%y%H%M%S')

class DB:

    ACCT_NUMS = [100000]
    TOTAL_TRANSACTIONS = 0
    CONFIRMATION_NUMS = []

    def generate_account_number():
        acct_num = DB.ACCT_NUMS[-1] + 1
        DB.ACCT_NUMS.append(acct_num)
        return acct_num

class Account:
    
    INT_RATE = 0.02

    def __init__(self, first_name, last_name, pref_time_zone='UTC', balance=0):
        self.first_name = first_name
        self.last_name = last_name
        self.pref_time_zone = pref_time_zone
        self._account_number = DB.generate_account_number()
        self._balance = float(balance)

    @property
    def balance(self):
        if self._balance < 0:
            raise ValueError('Balance must be positive.')
        return self._balance

    @property
    def account_number(self):
        return self._account_number

    @property
    def full_name(self):
        return f'{self.first_name.title()} {self.last_name.title()}'

    def deposit(self, amount, transaction_type='D'):
        utc_formatted = get_utc_formatted()
        self._balance += amount
        DB.TOTAL_TRANSACTIONS += 1
        conf_num = ConfirmationNumber(transaction_type, self.account_number, utc_formatted, DB.TOTAL_TRANSACTIONS).get_num()
        DB.CONFIRMATION_NUMS.append(conf_num)
        return f'Deposit complete, new balance: {self._balance}. Confirmation number: {conf_num}.'

    def withdraw(self, amount):
        utc_formatted = get_utc_formatted()
        DB.TOTAL_TRANSACTIONS += 1
        if (self._balance - amount) < 0:
            conf_num = ConfirmationNumber('X', self.account_number, utc_formatted, DB.TOTAL_TRANSACTIONS).get_num()
            DB.CONFIRMATION_NUMS.append(conf_num)
            raise ValueError(f'Transaction declined. You can not withdraw more then {self._balance}. Please try again. Confirmation number: {conf_num}.')
        self._balance -= amount
        conf_num = ConfirmationNumber('W', self.account_number, utc_formatted, DB.TOTAL_TRANSACTIONS).get_num()
        DB.CONFIRMATION_NUMS.append(conf_num)
        return f'Withdraw complete, new balance: {self._balance}. Confirmation number: {conf_num}.'

    def add_interest(self):
        accrued_interest = self._balance * (1 * Account.INT_RATE)
        return self.deposit(accrued_interest, transaction_type='I')

    @staticmethod
    def inspect_conf_num(num, pref_time_zone='UTC'):
        split = num.split('-')
        transaction_type, account_number, time, transaction_id = split
        conf_num = ConfirmationNumber(transaction_type, account_number, time, transaction_id, pref_time_zone)
        return conf_num

class ConfirmationNumber:

    def __init__(self, transaction_type, account_number, time, transaction_id, pref_time_zone='UTC'):
        self.transaction_type = transaction_type
        self.account_number = account_number
        self.time = time
        self.transaction_id = transaction_id
        if pref_time_zone != 'UTC':
            dt_naive_obj = datetime.datetime.strptime(time, '%m%d%y%H%M%S')
            utc_now = pytz.utc.localize(dt_naive_obj)
            user_time = utc_now.astimezone(pytz.timezone(pref_time_zone)).strftime('%b %d, %Y %I:%M:%S-%z-%Z')
            self.user_time = user_time
        else:
            self.user_time = time

    def get_num(self):
        return f'{self.transaction_type}-{self.account_number}-{self.time}-{self.transaction_id}'


user1 = Account('elon', 'musk', pref_time_zone='US/Pacific', balance=100)
user2 = Account('lex', 'fridman', pref_time_zone='US/Central', balance=50)

                        # ------------ Notes -----------------

# Could have used a generator function for the transaction ids or itertools.count()
# Force floats in the initializer so it applies downwards
# Transaction types could be in a dictionary
# Could have utilized a tuple to read inspect_conf_num instead of a class and just put the get_num function inside the Account class

c = user1.inspect_conf_num('D-100001-120220101703-1', pref_time_zone='US/Central')

print(c.user_time)