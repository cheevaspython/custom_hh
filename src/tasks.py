import smtplib 

from email.message import EmailMessage
from celery import Celery
from src.config import SMTP_USER, SMTP_PASSWORD

SMTP_HOST = 'smtp.test'
SMTP_PORT = 465

celery = Celery('tasks', broker='redis://localhost:6379')

def get_email_template_dashboard(contender_mail: str, employer_mail: str):
    email = EmailMessage()
    email['Subject'] = 'Приглашение'
    email['From'] = employer_mail
    email['To'] = contender_mail

    email.set_content(
        '<div>'
        f'<h1 style="color: red;">Здравствуйте, приглашаем на интервью</h1>'
        '-management-dashboard-ui-design-template-suitable-designing-application-for-android-and-ios-clean-style-app'
        '-mobile-free-vector.jpg" width="600">'
        '</div>',
        subtype='html'
    )
    return email


@celery.task
def send_invite_to_meet(mails: list[str], hunter_email: str):
    for mail in mails:
        mail_to_send = get_email_template_dashboard(mail, hunter_email)
        with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT) as server:
            server.login(SMTP_USER, SMTP_PASSWORD)
            server.send_message(mail_to_send)

    
