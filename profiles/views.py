from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from home.forms import CustomUserChangeForm

@login_required
def profiles(request):
    return render(request, 'profile/profile.html', {'user': request.user})

@login_required
def profile_view(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profiles')
    else:
        form = CustomUserChangeForm(instance=request.user)
    return render(request, 'profile/profile.html', {'form': form})