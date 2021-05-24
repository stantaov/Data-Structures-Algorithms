"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

def max_time(data):
  myDict1 = {}
  for row in calls:
    myDict1.setdefault(row[0], []).append(row[3])
    myDict1.setdefault(row[1], []).append(row[3])

  myDict2 = {}
  for key, value in myDict1.items():
    count = 0
    for item in value:
      count += int(item)
    myDict2[key] = count

  max_duration =  max(myDict2.values())
  for key, value in myDict2.items():
    if value == max_duration:
      print(f"{key} spent the longest time, {max_duration} seconds, on\
the phone during September 2016.")


if __name__ == '__main__':
    max_time(calls)
