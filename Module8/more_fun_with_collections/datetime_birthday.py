"""
Program: datetime_birthday.py
Author: Bobby Parsons

Contains a function to calvulate a half-birthday
"""
from datetime import datetime, timedelta

def half_birthday(birthday):
    result = birthday + timedelta(days = 183)

    #print(result.isoformat())
    return result

if __name__ == "__main__":
    birthday = datetime(2019, 12, 3)
    result = half_birthday(birthday)
    print(result.isoformat())