from django.contrib import admin
from django.urls import path

from notes import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('note/<int:note_id>/', views.note_details, name='note'),
    path('add/', views.add_note, name='add_note'),
    path('remove/<int:note_id>/', views.remove_note, name='remove_note'),
    path('edit/<int:note_id>/', views.edit_note, name='edit_note'),
]
