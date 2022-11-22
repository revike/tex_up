from django.core.mail import send_mail

from tex_up.settings import EMAIL_HOST_USER, EMAIL_SEND


def send_mail_client(client):
    subject = f'Новая заявка'
    message = f'Имя: {client["first_name"]}\nТелефон: {client["phone"]}'
    return send_mail(subject, message, EMAIL_HOST_USER,
                     EMAIL_SEND, fail_silently=False)
