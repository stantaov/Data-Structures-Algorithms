"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

def telemarketers():

    incoming = set()
    outgoing = set()
    recieved_text = set()
    sent_text = set()
    results = []

    for row in calls:
      incoming.add(row[1])
      outgoing.add(row[0])

    for row in texts:
      recieved_text.add(row[1])
      sent_text.add(row[0])

    combined = list(recieved_text)+list(sent_text)+list(incoming)


    for item in outgoing:
      if item not in combined:
          results.append(item)

    results = sorted(results)
    print("These numbers could be telemarketers: ")
    for item in results:
      print(item)

if __name__ == "__main__":
    telemarketers()
