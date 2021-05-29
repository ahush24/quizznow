from django.contrib import admin
from django.urls import path
from quiz.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home)
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
