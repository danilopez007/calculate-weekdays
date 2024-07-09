## MyDataClass
MyDataClass is a Python class that determines the number of weekdays, inclusively, between two dates. It determines this by:
  1. Finding the number of days between two dates, taking into account leap years. 
  2. Calculating the number of weekend days in between said dates
  3. Subtracting the number of weekend days from the number of days between the dates. 

## Features
- Determine whether a year is a leap year or not
- Determine the day of the week
- Calculate the total number of days between two dates
- Calculate the number of weekend days between two dates
- Calculate the number of weekdays between two dates

## Usage Example
```
first_date = MyDataClass(1, 1, 2000)
second_date = MyDataClass(12, 31, 2000)
weekdays = MyDataClass.num_week_days(first_date, second_date)

print("Number of week days between given dates, inclusive:")
print(weekdays)
```

## Testing
The test_myDataClass.py file contains unit tests for MyDataClass. To run the tests, use the following command:
```python -m unittest test_myDataClass.py```

## Author
Dani Lopez
Last updated 2024-07-09
