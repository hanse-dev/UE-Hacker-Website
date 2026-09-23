from datetime import datetime

now = datetime.now()
print(f"Hour valid: {0 <= now.hour <= 23}")
print(f"Year has 4 digits: {len(now.strftime('%Y')) == 4}")
