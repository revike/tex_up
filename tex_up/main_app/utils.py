from django.core.mail import send_mail

from tex_up import settings


def send_mail_client(client):
    subject = f'{client}'
    message = f''
    return send_mail(subject, message, settings.EMAIL_HOST_USER,
                     [settings.EMAIL_HOST_USER], fail_silently=False)
