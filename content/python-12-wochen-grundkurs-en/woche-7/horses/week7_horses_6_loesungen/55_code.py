from datetime import datetime

hour = datetime.now().hour
if 6 <= hour <= 17:
    daytime = "Day"
else:
    daytime = "Night"
print(f"Time of day valid: {daytime in ['Day', 'Night']}")
