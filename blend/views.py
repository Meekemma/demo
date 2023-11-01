from django.core.mail import EmailMessage, send_mail
from django.template.loader import render_to_string
from django.shortcuts import render, redirect
from django.conf import settings
from .forms import DemoForm,ContactForm,EmailForm
from .decorators import common_functionality,newsUpdate
from.models import Newsletter


# Create your views here.

@common_functionality
@newsUpdate
def Index(request):
    if request.method == 'POST':
        form=DemoForm(request.POST)
        if form.is_valid():
            email = request.POST.get('email')
            template = render_to_string('blend/email_template.html')

        email_message=EmailMessage(
            'Thanks for checking out the app Demo',
            template,
            settings.EMAIL_HOST_USER,
            [email]
        )  
        email_message.fail_silently = False  
        email_message.send()

        form.save()

        return redirect('home')
    else:
        form=DemoForm()
    context = {'form':form}
    return render (request, 'blend/index.html', context)


def newsletter_info(request):
    if request.method == 'POST':
        form=EmailForm(request.POST)
        if form.is_valid():
            subject=form.cleaned_data['subject']
            receivers = form.cleaned_data['receivers'].split(',')
            message=form.cleaned_data['message']

            from_email=settings.EMAIL_HOST_USER

            email_message=EmailMessage(
                subject,
                message,
                from_email,
                receivers,
            )
            email_message.send()

    form=EmailForm()
    form.fields['receivers'].initial = ','.join([active.email for active in Newsletter.objects.all()])
	
    context = {'form': form }
    return render(request, 'blend/newsletter.html', context)    


@common_functionality
@newsUpdate
def questions(request):

    context={}
    return render(request, 'blend/faq.html', context)