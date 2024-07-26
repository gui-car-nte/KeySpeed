from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.views.decorators.csrf import csrf_exempt
from .models import UserProfile
from django.http import JsonResponse
from ranking.models import Score
import json

TEST_TEXT = "This is a test"

def home(request):
    return render(request, 'home/home.html', {'test_text': TEST_TEXT})

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'home/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'home/login.html', {'form': form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')

@csrf_exempt
def submit_test(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            user_input = data.get('user_input', '')
            time_taken = data.get('time_taken', 0)

            correct_chars = sum(1 for a, b in zip(user_input, TEST_TEXT) if a == b)
            accuracy = correct_chars / len(TEST_TEXT) if TEST_TEXT else 0

            score = max(0, int((accuracy * 100) / (time_taken / 60)))

            user_profile = UserProfile.objects.get(username=request.user.username)
            Score.objects.create(user=user_profile, score=score)

            return JsonResponse({'score': score})
        except UserProfile.DoesNotExist:
            return JsonResponse({'error': 'UserProfile does not exist'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({'error': 'Invalid request'}, status=400)
