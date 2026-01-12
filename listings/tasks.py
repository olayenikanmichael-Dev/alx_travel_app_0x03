from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_booking_confirmation_email(email, booking_reference):
    send_mail(
        subject='Booking Confirmation',
        message=f'Your booking {booking_reference} has been confirmed.',
        from_email=None,
        recipient_list=[email],
        fail_silently=False,
    )
