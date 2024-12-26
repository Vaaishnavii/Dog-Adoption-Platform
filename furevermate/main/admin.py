from django.contrib import admin
from .models import QuizResponse, Dog, SavedDog, AdoptedDog

admin.site.register(QuizResponse)
admin.site.register(Dog)
admin.site.register(SavedDog)
admin.site.register(AdoptedDog)
