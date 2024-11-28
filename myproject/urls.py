# myproject/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),  # Admin route
    path('', include('myapp.urls')),  # Includes routes from myapp's urls.py
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
