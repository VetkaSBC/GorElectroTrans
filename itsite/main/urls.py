from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views
from .views import register, logout_view

urlpatterns = [
    path('', views.main, name = 'home'),
    path('about', views.about),
    path('register/', register, name='register'),
    path('logout/', logout_view, name='logout'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)