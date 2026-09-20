# ⏳ Archive Spell 5: Time with time and datetime

```python
import time
from datetime import datetime

start = time.time()        # current timestamp (seconds)
time.sleep(0.2)            # wait 0.2 seconds
end = time.time()
print(end - start)         # about 0.2

now = datetime.now()       # current date and time
print(now.hour)            # just the hour (0–23)
print(now.strftime("%Y-%m-%d"))   # format the date as text
```

- **`time.sleep(seconds)`** pauses the program
- **`time.time()`** returns a timestamp – the **difference** of two timestamps is the elapsed time
- **`datetime.now()`** returns date and time; `.hour`, `.minute`, `.year` … fetch single parts
- **`strftime("...")`** formats the time as text: `%Y` year, `%m` month, `%d` day, `%H:%M` clock time

> 💡 Keep waiting times short here (under a second) – the tasks should run quickly.
