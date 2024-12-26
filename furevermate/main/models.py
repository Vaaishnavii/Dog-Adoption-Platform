from django.db import models
from django.contrib.auth.models import User  # Ensure User is imported correctly

class Dog(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    traits = models.TextField()
    image = models.CharField(max_length=255)  # Use CharField for static image paths

    def __str__(self):
        return self.name


class SavedDog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='saved_dogs')  # User relation
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE, related_name='saved_by_users')  # Dog relation
    
    def __str__(self):
        return f"{self.user.username} - {self.dog.name}"


class AdoptedDog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='adopted_dogs')  # User relation
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE, related_name='adopted_by_users')  # Dog relation

    def __str__(self):
        return f"{self.user.username} - {self.dog.name}"


class QuizResponse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    time_dedication = models.CharField(max_length=100)
    living_space = models.CharField(max_length=100)
    grooming = models.CharField(max_length=100)
    children = models.CharField(max_length=100)
    activity_level = models.CharField(max_length=100)

    def __str__(self):
        return f"QuizResponse for {self.user.username}: {self.time_dedication}, {self.living_space}"
