from django.urls import path
from . import views


urlpatterns = [
    path('notes/', views.getNotes, name="Notes"),    
    path('note/<int:pk>/update/', views.updateNote, name="update-note"),   
    path('note/create/', views.createNote, name='create'), 
    path('note/<int:pk>/delete/', views.deleteNote, name="delete"),   
    path('note/<int:pk>/', views.getNote, name="Note" ),   
     
]
