from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Home page
    path('', views.home, name='my_index'),

    # About Us page
    path('about/', views.about, name='my_about'),

    # Services pages
    path('services/', views.services, name='my_services'),
    path('services/logo-design/', views.logo_design, name='my_logo_design'),
    path('services/branding/', views.branding, name='my_branding'),
    path('services/web-design/', views.web_design, name='my_web_design'),
    path('services/social-media/', views.social_media, name='my_social_media'),
    path('services/print-design/', views.print_design, name='my_print_design'),

    # Contact page
    path('contact/', views.contact, name='my_contact'),

    # Contact Success page
    path('contact-success/', views.contact_success, name='my_contact_success'),
]

# Serve static files during development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
