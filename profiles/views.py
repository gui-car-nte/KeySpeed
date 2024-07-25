from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def profiles(request):
    return render(request, 'profile/profile.html', {'user': request.user})
