# from datetime import datetime
from datetime import date

import random


class DateEquals:
    def __init__(self, today=date.today()):
        self.today = today
        self.check_date = date(2019, random.randint(1, 12), random.randint(1, 28))
        self.iterate = 0

    def date_eq(self):

        check_date = self.check_date
        iterate = self.iterate
        today = self.today

        while True:
            if check_date != today:
                # print('today is {} but check date is {}'.format(today, check_date))
                iterate += 1
            elif check_date == today:
                iterate += 1
                probably = 1/iterate
                # print('today is check date! and probably equal {}'.format(probably))
                return probably
            check_date = date(2019, random.randint(1, 12), random.randint(1, 28))
