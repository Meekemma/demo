from django.shortcuts import redirect
from django.http import HttpResponse
from .forms import ContactForm,NewsletterForm
from django.core.mail import EmailMessage, send_mail
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib import messages
from.models import Newsletter




def common_functionality(view_func):
    def wrapper(request, *args, **kwargs):

        if request.method == 'POST':
            form_contact=ContactForm(request.POST)
            if form_contact.is_valid():
                email_name=request.POST.get('email') 
                message=request.POST.get('message')  

                subject = "Contact Form Submission: " + email_name
                send_mail(
                    subject,
                    message,
                    settings.EMAIL_HOST_USER,
                    ['meek.emma007@gmail.com'],
                    fail_silently=False,
                ) 
                form_contact.save()
                return redirect('home')
        else:
            form_contact=ContactForm()

        context = {'form_contact':form_contact}

        return view_func(request, *args, **kwargs)
    return wrapper 


def newsUpdate(view_func):
    def wrapper(request, *args,**kwargs):
        if request.method == 'POST':
            news_form=NewsletterForm(request.POST)
            if news_form.is_valid():
                email = request.POST.get('email')
                email_exists = Newsletter.objects.filter(email=email).exists()
                template = render_to_string('blend/newsinfo.html')

                if email_exists:
                     messages.error(request, "Email already subscribed to the newsletter")
                else:
                    messages.success(request, "Thanks for subscribing for the newsletter")

                    email_message=EmailMessage(
                        'Thanks for subscribing for the newsletter',
                        template,
                        settings.EMAIL_HOST_USER,
                        [email]
                    )  
                    email_message.fail_silently = False  
                    email_message.send()

                    news_form.save()

        return view_func(request, *args, **kwargs)
    return wrapper