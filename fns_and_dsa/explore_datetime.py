import datetime
from datetime import timedelta

year = datetime.datetime.now().year
month = datetime.datetime.now().month
day = datetime.datetime.now().day
hour = datetime.datetime.now().hour
minute = datetime.datetime.now().minute
second = datetime.datetime.now().second


def display_current_datetime():
  print(f"{year}-{month}-{day} {hour}:{minute}:{second}")

