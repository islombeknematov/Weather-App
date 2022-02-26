
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from weather.views import get_weather

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('weather.urls')),
]
