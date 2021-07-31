from django.contrib import admin
from django.urls import path

from notes import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('note/<int:note_id>/', views.note_details, name='note'),
    path('remove/<int:note_id>/', views.note_remove, name='note_remove'),
]
