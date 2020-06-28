import email
import smtplib
import imaplib
from email.MIMEText import MIMEText
from email.MIMEMultipart import MIMEMultipart


class Mail:
    def __init__(self):
        self.GMAIL_SMTP = "smtp.gmail.com"
        self.GMAIL_IMAP = "imap.gmail.com"
        self.params = {
            'login': 'login@gmail.com',
            'password': 'qwerty',
            'subject': 'Subject',
            'recipients': ['vasya@email.com', 'petya@email.com'],
            'text': 'Message',
            'header': None
        }


    def connect(self):
        message = MIMEMultipart()
        responce = smtplib.SMTP(GMAIL_SMTP, 587)
        return message, responce


    def sending(self):
        self.connect()
        message['From'] = self.params['login']
        message['To'] = ', '.join(self.params['recipients'])
        message['Subject'] = self.params['subject']
        message.attach(MIMEText(self.params['text']))

        responce.ehlo()
        # secure our email with tls encryption
        responce.starttls()
        # re-identify ourselves as an encrypted connection
        responce.ehlo()
        responce.login(l, passwORD)
        responce.sendmail(self.params['login'], responce, message.as_string())
        responce.quit()
        return None


    def receiving(self):
        responce = imaplib.IMAP4_SSL(self.GMAIL_IMAP)
        responce.login(self.params['login'], self.params['password'])
        responce.list()
        responce.select("inbox")

        criterion = '(HEADER Subject "%s")' % header if header else 'ALL'
        result, data = responce.uid('search', None, criterion)
        assert data[0], 'There are no letters with current header'
        latest_email_uid = data[0].split()[-1]
        result, data = mail.uid('fetch', latest_email_uid, '(RFC822)')
        raw_email = data[0][1]
        email_message = email.message_from_string(raw_email)
        responce.logout()


if __name__ == '__main__':
    pass