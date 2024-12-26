from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm, LoginForm
from .models import Dog, SavedDog, AdoptedDog, QuizResponse
import joblib
from django.http import HttpResponseRedirect
from django.urls import reverse

@login_required
def dashboard(request):
    # Fetch saved and adopted dogs for the current user
    saved_dogs = SavedDog.objects.filter(user=request.user)
    adopted_dogs = AdoptedDog.objects.filter(user=request.user)
    return render(request, 'dashboard.html', {
        'saved_dogs': saved_dogs,
        'adopted_dogs': adopted_dogs,
    })

@login_required
def save_dog(request, dog_id):
    dog = get_object_or_404(Dog, id=dog_id)
    if not SavedDog.objects.filter(user=request.user, dog=dog).exists():
        SavedDog.objects.create(user=request.user, dog=dog)
        messages.success(request, f'{dog.name} has been saved to your list!')
    else:
        messages.info(request, f'{dog.name} is already in your saved list.')
    return redirect('dashboard')

@login_required
def adopt_dog(request, dog_id):
    dog = get_object_or_404(Dog, id=dog_id)
    if not AdoptedDog.objects.filter(user=request.user, dog=dog).exists():
        AdoptedDog.objects.create(user=request.user, dog=dog)
        messages.success(request, f'Congratulations! You have adopted {dog.name}!')
    else:
        messages.info(request, f'You have already adopted {dog.name}.')
    return redirect('dashboard')

@login_required
def logout_user(request):
    logout(request)
    messages.info(request, 'You have successfully logged out.')
    return redirect('home')

def index(request):
    # Render the home page
    return render(request, 'index.html')

def browse(request):
    # Fetch all available dogs
    dogs = Dog.objects.all()
    return render(request, 'browse.html', {'dogs': dogs})

def contact(request):
    # Render the contact page
    return render(request, 'contact.html')

def quiz(request):
    # Render the quiz page
    return render(request, 'quiz.html')


def dog_details(request, dog_id):
    # Fetch the dog object using its ID
    dog = get_object_or_404(Dog, id=dog_id)
    return render(request, "dog_details.html", {"dog": dog})

MODEL_PATH = "D://S7//Full Stack//FINAL PROJECT//final//furevermate//models//expanded_fixed_breeds_model.pkl"
ENCODER_PATH = "D://S7//Full Stack//FINAL PROJECT//final//furevermate//models//expanded_fixed_breeds_encoder.pkl"

model = joblib.load(MODEL_PATH)
encoder = joblib.load(ENCODER_PATH)

def quiz_submit(request):
    if request.method == "POST":
        user_input = [
            request.POST.get("time_dedication"),
            request.POST.get("living_space"),
            request.POST.get("grooming"),
            request.POST.get("children"),
            request.POST.get("activity_level"),
            request.POST.get("dog_size"),
        ]
        try:
            user_data = encoder.transform([user_input])
        except ValueError as e:
            return render(request, "quiz.html", {"error": f"Invalid input: {e}"})

        # Predict the suitable dog breed
        predicted_breed = model.predict(user_data)[0]

        # Query the database for all matching dogs
        dogs = Dog.objects.filter(breed=predicted_breed)

        # Render the results template with the breed and matching dogs
        return render(request, "quiz_results.html", {"breed": predicted_breed, "dogs": dogs})

    # Redirect to quiz if the request method is not POST
    return HttpResponseRedirect(reverse("quiz"))

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                messages.success(request, f"Welcome, {user.username}!")
                return redirect('dashboard')  # Redirect to dashboard after login
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Please fill out the form correctly.")
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def user_register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Create the user with hashed password
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  # Hash the password
            user.save()
            messages.success(request, 'Account created successfully. You can now log in.')
            return redirect('login')
        else:
            messages.error(request, "There was an error in your registration. Please try again.")
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

def user_logout(request):
    logout(request)
    messages.info(request, 'You have successfully logged out.')
    return redirect('home')

