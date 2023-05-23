import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


email_from = 'vishalhirandagi33@gmail.com'
email_password = 'ukgljpopnvbcwbao'
email_subject = 'Daily Goods Arrival Notification'
email_body = 'Hello,\n\nThis is to inform you that new goods have arrived in our store today.\n\nThank you for your continued patronage.\n\nBest regards,\nSender'

recipients = ['vishalhirandagi33@gmail.com']
cc_recipients = ['rsrinivas@msystechnologies.com','vinayakhavannavar@gmail.com',"anjansriram.98@gmail.com"]


msg = MIMEMultipart()
msg['From'] = email_from
msg['To'] = ', '.join(recipients)
msg['Cc'] = ', '.join(cc_recipients)
msg['Subject'] = email_subject
msg.attach(MIMEText(email_body, 'plain'))


server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(email_from, email_password)

server.sendmail(email_from, recipients + cc_recipients, msg.as_string())
print('Email notification sent successfully!')

server.quit()
