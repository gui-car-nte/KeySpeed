from django.db import models
from home.models import UserProfile

class Score(models.Model):
    user = models.ForeignKey(UserProfile, on_delete = models.CASCADE)
    score = models.IntegerField()
    date = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        return f'{self.user} - {self.score} - {self.date}'
