from django.urls import path

from . import views
from .views import contact_form, contact
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('contact', contact, name='contact_form'),
    path('contact', contact, name='contact'),
    path('contact_process.php', views.contact_process, name='contact_process.php'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)