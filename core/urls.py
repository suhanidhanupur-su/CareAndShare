from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('people/', views.people, name='people'),
    path('people-behind/', views.people, name='people_behind'),
    path('programmes/', views.programmes, name='programmes'),
    path('initiatives/', views.programmes, name='initiatives'),
    path('gallery/', views.gallery, name='gallery'),
    path('media/', views.media, name='media'),
    path('contact/', views.contact, name='contact'),
    path('contact-us/', views.contact, name='contact_us'),
]
