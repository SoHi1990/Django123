'''
Created on Jan 24, 2016

@author: sohi
'''
from django.test.testcases import TestCase
import datetime
from django.utils import timezone
from Django123.models import Question

class QuestionMethodTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        time = timezone.now() + datetime.timedelta(days = 30)
        future_questions = Question(pub_date = time)
        self.assertEqual(future_questions.was_published_recently(),False)
