# Datetime Module

```python
import datetime

my_hour = datetime.time(17, 35, 50, 1500)
print(type(my_hour))
print(my_hour)
print(my_hour.minute)
print(my_hour.hour)
```

```python
my_day = datetime.date(2025, 10, 17)
print(my_day)
print(my_day.ctime())
```

```python
from datetime import date, datetime

my_date = datetime(2025, 5, 15, 22, 10, 15, 2500)
my_date = my_date.replace(month=11)
print(my_date)

birth = date(1995, 3, 5)
death = date(2095, 6, 19)

life = death - birth
print(life)
print(life.days)

wake_up = datetime(2022, 10, 5, 7, 30)
sleep = datetime(2022, 10, 5, 23, 45)

vigil = sleep - wake_up

print(vigil)
print(vigil.seconds)
```
