from django.shortcuts import render, redirect
from django.contrib import messages
from .models import ContactMessage, GalleryImage, MediaPost

def home(request):
    home_gallery = GalleryImage.objects.filter(is_active=True).order_by('order', '-created_at')[:4]
    return render(request, 'home.html', {'home_gallery': home_gallery})

def about(request):
    return render(request, 'about.html')

def people(request):
    return render(request, 'people.html')

def programmes(request):
    return render(request, 'programmes.html')

def gallery(request):
    gallery_images = GalleryImage.objects.filter(is_active=True).order_by('order', '-created_at')
    return render(request, 'gallery.html', {'gallery_images': gallery_images})

def media(request):
    featured_post = MediaPost.objects.filter(is_active=True, is_featured=True).order_by('order', '-date', '-created_at').first()
    media_posts_qs = MediaPost.objects.filter(is_active=True)
    if featured_post:
        media_posts = media_posts_qs.exclude(id=featured_post.id).order_by('order', '-date', '-created_at')
    else:
        media_posts = media_posts_qs.order_by('order', '-date', '-created_at')

    return render(request, 'media.html', {
        'featured_post': featured_post,
        'media_posts': media_posts,
    })

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
