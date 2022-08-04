from django.urls import path
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls import static

from . import views

app_name = 'home'

urlpatterns = [

    path('',  views.Home.as_view(), name='home'),
    path('works/', views.Works.as_view(), name='works'),
    path('services/', views.WebsiteServicesView.as_view(), name='services'),
    path('testimonials/', views.Testimonials.as_view(), name='testimonials'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('privacy/', TemplateView.as_view(template_name="privacy.html"), name='privacy'),
    path('terms/', TemplateView.as_view(template_name="terms.html"), name='terms'),

]

if settings.DEBUG:
    urlpatterns += static.static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static.static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
