import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email credentials
MY_EMAIL = 'vishalhirandagi3331@gmail.com' # replace with your admin email address
MY_PASSWORD = 'Vishal#1358' # replace with your admin email password
SMTP_SERVER = 'smtp.example.com' # replace with your SMTP server domain name
SMTP_PORT = 587 # replace with your SMTP server port number

# Sample data for customers
CUSTOMER_LIST = [
    {'name': 'John', 'email': 'john@example.com'},
    {'name': 'Mary', 'email': 'mary@example.com'},
    {'name': 'Steve', 'email': 'steve@example.com'}
]

# Sample message to customers
MESSAGE_TEMPLATE = """
Hello {name},

We are pleased to inform you that your goods have arrived and are ready for pickup.

Best regards,
Admin
"""

# Create a connection to the SMTP server
server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
server.starttls()
server.login(MY_EMAIL, MY_PASSWORD)

# Send the email to all customers
for customer in CUSTOMER_LIST:
    message = MIMEMultipart()
    message['From'] = MY_EMAIL
    message['To'] = customer['email']
    message['Cc'] = "sales@example.com" # Add cc candidates
    message['Subject'] = 'Arrival of Goods Notification'
    text = MESSAGE_TEMPLATE.format(name=customer['name'])
    message.attach(MIMEText(text))
    server.sendmail(MY_EMAIL, [customer['email'],"sales@example.com"], message.as_string())

# Disconnect from the SMTP server
server.quit()
