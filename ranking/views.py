from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Score

def global_ranking(request):
    scores = Score.objects.all().order_by('-score')
    return render(request, 'ranking/global_ranking.html', {'scores': scores})

@login_required
def personal_ranking(request):
    scores = Score.objects.filter(user=request.user).order_by('-score')
    return render(request, 'ranking/personal_ranking.html', {'scores': scores})
