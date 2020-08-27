import os

with os.scandir('/') as entries:
    for entry in entries:
        print(entry.name)
