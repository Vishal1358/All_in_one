import argparse        
import email            
import imaplib          
import sqlite3
import unittest
import time

def fetch_emails(name_or_duration):

    conn = imaplib.IMAP4_SSL('vishalhirandagi@gmail.com')
    conn.login('vishalhirandagi33@gmail.com', 'Vishal#1358')
    conn.select('Inbox')
    result, data = conn.search(None, f'(SUBJECT "{name_or_duration}" BODY "{name_or_duration}")')
    emails = []
    for num in data[0].split():
        _, data = conn.fetch(num, '(RFC822)')
        raw_email = data[0][1]
        email_message = email.message_from_bytes(raw_email)
        emails.append(email_message)
    conn.close()

    conn = sqlite3.connect('emails.db')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS emails (subject TEXT, body TEXT)')
    for email_message in emails:
        subject = email_message['Subject']
        body = email_message.get_payload()
        c.execute('INSERT INTO emails (subject, body) VALUES (?, ?)', (subject, body))
    conn.commit()
    conn.close()

    return emails

class TestEmailFetching(unittest.TestCase):
    def test_fetch_emails(self):
       
        conn = imaplib.IMAP4_SSL('localhost',49.37.251.56)
        conn.login('vishalhirandagi33@gmail.com', 'Vishal#1358')
        conn.select('Inbox')
        conn.append('Inbox', None, imaplib.Time2Internaldate(time.time()), b'Subject: Test email\r\n\r\nThis is a test email.')
        conn.close()


        emails = fetch_emails('Test email')
        self.assertEqual(len(emails), 1)
        self.assertEqual(emails[0]['Subject'], 'Test email')
        self.assertEqual(emails[0].get_payload(), 'This is a test email.')