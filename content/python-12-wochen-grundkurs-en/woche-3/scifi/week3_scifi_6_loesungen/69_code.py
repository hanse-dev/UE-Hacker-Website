speed = 640
if speed >= 800:
    print("Stage: Hyperdrive")
elif speed >= 600:
    print("Stage: Fast flight")
elif speed >= 400:
    print("Stage: Cruise flight")
elif speed >= 200:
    print("Stage: Maneuvering flight")
else:
    print("Stage: Crawl")
