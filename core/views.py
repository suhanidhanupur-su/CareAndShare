from django.shortcuts import render, redirect
from django.contrib import messages
from .models import ContactMessage

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def people(request):
    return render(request, 'people.html')

def gallery(request):
    return render(request, 'gallery.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        phone = request.POST.get('phone', '').strip()
        subject = request.POST.get('subject', '').strip()
        message_text = request.POST.get('message', '').strip()

        if name and email and message_text:
            ContactMessage.objects.create(
                name=name,
                email=email,
                phone=phone,
                subject=subject or 'General Inquiry',
                message=message_text
            )
            messages.success(request, 'Thank you! Your message has been received. Our team will get back to you shortly.')
            return redirect('contact')
        else:
            messages.error(request, 'Please fill in all required fields (Name, Email, and Message).')

    return render(request, 'contact.html')
