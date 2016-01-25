'''
Created on Jan 10, 2016

@author: sohi
'''

from django.db import models
from django.utils import timezone
import datetime

class Question(models.Model):
    question_text = models.CharField(max_length = 200)
    pub_date = models.DateTimeField('data published')
    
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1)<=self.pub_date <= now
    
class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length = 200)
    votes = models.IntegerField(default = 0)
    