from django.contrib import admin
from django.urls import path, include

from first import views

urlpatterns = [
    path('first/', include('first.urls')),
    path('second/', include('second.urls')),
    path('third/', include('third.urls')),
    path('admin/', admin.site.urls),
]

