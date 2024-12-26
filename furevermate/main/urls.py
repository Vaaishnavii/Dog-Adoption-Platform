from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),  # Home page
    path('browse/', views.browse, name='browse'),  # Browse dogs page
    path('contact/', views.contact, name='contact'),  # Contact page
    path('quiz/', views.quiz, name='quiz'),  # Quiz page
    path('quiz/submit/', views.quiz_submit, name='quiz_submit'),  # Quiz submission
    path('register/', views.user_register, name='register'),  # User registration
    path('login/', views.user_login, name='login'),  # User login
    path('dashboard/', views.dashboard, name='dashboard'),  # User dashboard
    path('logout/', views.user_logout, name='logout'),  # User logout
    path('save/<int:dog_id>/', views.save_dog, name='save_dog'),  # Save a dog
    path('adopt/<int:dog_id>/', views.adopt_dog, name='adopt_dog'),  # Adopt a dog
    path("dog/<int:dog_id>/", views.dog_details, name="dog_details"),
]
