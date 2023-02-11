import csv
from twilio.rest import Client

# Your Twilio account SID and Auth Token
account_sid = '<your_twilio_account_sid>'
auth_token = '<your_twilio_auth_token>'

# Your Twilio WhatsApp number
from_whatsapp_number = 'whatsapp:<your_twilio_whatsapp_number>'

# Load the phone numbers and message from the CSV file
numbers = []
message = None
with open('numbers.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        if message is None:
            message = row[0]
        else:
            numbers.append(row[0])

# Create a Twilio client
client = Client(account_sid, auth_token)

# Send the message to each number
for to_number in numbers:
    message = client.messages.create(
        from_=from_whatsapp_number,
        to='whatsapp:' + to_number,
        body=message
    )

print(f'Sent {len(numbers)} messages')
