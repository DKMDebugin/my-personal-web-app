# project views module
from django.conf import settings
from django.contrib import messages
from decouple import  config, Csv
from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404

from .forms import ContactForm


def contact(request):
    form = ContactForm(request.POST or None)

    if form.is_valid():
        instance = request.POST
        messages.success(request,
                        'Your message has been passed across. I\'ll get back to you as soon as possible.',
                        'alert alert-success alert-dismissible')
        subject         = f'Message From My Website'
        message         = f"FROM: {instance['name']}\nMESSAGE: {instance['message']}\nEMAIl: {instance['email']}"
        from_email      = config('from_email')
        to              = [config('to')]
        send_mail(subject=subject, message=message, from_email=from_email,
        recipient_list=to, fail_silently=True)


    template = 'contact.html'
    context = {
        'form': form,
    }
    return render(request, template, context)
