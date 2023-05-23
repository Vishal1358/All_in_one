import argparse
import imaplib
import email
from datetime import datetime, timedelta

# Define the command-line arguments
parser = argparse.ArgumentParser()
parser.add_argument('--name', type=str, help='Name of sender')
parser.add_argument('--days', type=int, help='Number of days to search')
args = parser.parse_args()

# Set up the email server connection
mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login('vishalhirandagi1432@gmail.com', 'Vishal#1358')
mail.select("inbox")

# Calculate the search date range based on the input duration
if args.days:
    date_since = (datetime.now() - timedelta(days=args.days)).strftime("%d-%b-%Y")
else:
    date_since = None

# Search for emails matching the criteria
search_criteria = f"FROM {args.name} SINCE {date_since}" if args.name else f"SINCE {date_since}"
result, data = mail.search(None, search_criteria)

# Print the email details for each matching email
if not data[0]:
    print('No matching emails found')
else:
    print(f'Found {len(data[0].split())} matching email(s):')
    for num in data[0].split():
        result, data = mail.fetch(num, '(RFC822)')
        msg = email.message_from_bytes(data[0][1])
        print('\nFrom:', msg['From'])
        print('Subject:', msg['Subject'])
        print('Date:', msg['Date'])
