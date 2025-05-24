import time

from celery import shared_task

from django.core.mail import EmailMessage, send_mail

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

import tempfile
import logging
from xhtml2pdf import pisa

from .models import CV


@shared_task
def send_cv_pdf(cv_id, email):
    from .models import CV
    try:
        cv = CV.objects.prefetch_related('skills', 'projects').get(id=cv_id)

        html = render_to_string('core/cv_pdf.html', {'cv': cv})

        with tempfile.NamedTemporaryFile(suffix='.pdf', delete=False) as pdf_file:
            pisa.CreatePDF(html, dest=pdf_file)
            pdf_path = pdf_file.name

        subject = f'CV - {cv.first_name} {cv.last_name}'
        message = f'Please find attached the CV for {cv.first_name} {cv.last_name}'
        from_email = "TEST@gmail.com"

        with open(pdf_path, 'rb') as f:
            pdf_data = f.read()

        email_msg = EmailMessage(
            subject,
            message,
            from_email,
            [email],
        )
        email_msg.attach(f'cv_{cv.id}.pdf', pdf_data, 'application/pdf')
        email_msg.send()

        return True
    except Exception as e:
        print(f"Error sending CV: {str(e)}")
        return False
