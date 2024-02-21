from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            send_contact_email(form.cleaned_data)
            return redirect('contact_success')
    else:
        form = ContactForm()
    return render(request, 'contact_form/contact.html', {'form': form})

def send_contact_email(data):
    subject = data['subject']
    message = f"Message from: {data['name']} <{data['email']}>\n\n{data['message']}"
    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [settings.CONTACT_EMAIL])