treibstoff = 10
atmosphaere = True
landeplatz = False
if treibstoff >= 20 or (atmosphaere and landeplatz):
    print("Notlandung möglich")
else:
    print("Notlandung unmöglich")