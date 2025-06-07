import datetime
from datetime import timedelta

current_date = datetime.datetime.now()

def display_current_datetime():
    print("Current date and time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))

display_current_datetime()
def calculate_future_date():
  future_date = current_date + timedelta(days=int(input("Enter days to add: ")))
  print(future_date)

calculate_future_date()