from django.contrib import admin
from django.urls import path

from notes import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('note/<int:note_id>/', views.note_detail, name='note'),
]
